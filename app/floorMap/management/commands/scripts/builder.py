# coding: utf-8

from __future__ import division
from __future__ import print_function

import math
import os
import re
from itertools import combinations
from PIL import Image, ImageDraw, ImageFont, ImageColor

import _settings as settings
import _utils as utils


class FloorMapBuilder:
    canvas = None
    floor_map_image = None
    _rooms = []

    def __init__(self, **kwargs):
        # Overrides default settings with provided settings
        for attr, value in kwargs.iteritems():
            if hasattr(settings, attr):
                setattr(settings, attr, value)

        input_file = kwargs.pop(
            'input',
            os.path.join(
                settings.MEDIA_ROOT,
                settings.PROJECT_DIR,
                settings.INPUT_FILENAME
            )
        )
        self.floor_map_image = Image.open(input_file)
        self.canvas = ImageDraw.Draw(self.floor_map_image)

    def add_room(self, **kwargs):
        new_room = Room(self.canvas, **kwargs)
        self._rooms.append(new_room)

    def render_image(self):
        if settings.DEBUG:
            print("****************************************")
            print("Rendering %d entities:" % len(self._rooms))

        for room in self._rooms:
            room.draw()
            room.print_label()

        if settings.DEBUG:
            print("****************************************")
            print("[SUCCESS] Render has completed.")

    def save(self, **kwargs):
        """
        Saves the rendered image
        :param kwargs: options include 'output' and 'quality'
        :return:
        """
        output_file = kwargs.pop(
            'output',
            os.path.join(
                settings.MEDIA_ROOT,
                settings.PROJECT_DIR,
                settings.OUTPUT_FILENAME
            )
        )
        quality = kwargs.pop('quality', settings.IMAGE_QUALITY)

        self.floor_map_image.save(output_file, quality=quality)

        if settings.DEBUG:
            print("[SUCCESS] A new copy was saved at %s" % output_file)


# Parent class for rooms
class Room:
    canvas = None
    options = None

    label = ""  # Text to display on the room
    code = ""  # physical room code

    # Coordinates of the room shape. ALWAYS turned into a polygon.
    # Will be converted if rectangle received
    _coords = []

    # Coordinates of the rectangle defining the zone where label can be printed
    _text_area_coords = []

    _log__room_format = []  # Stores all explored formats
    _log__room_bump = {}  # Stores already calculated bumped texts

    def __init__(self, canvas, **kwargs):
        if settings.DEBUG:
            print("Adding new entity with attributes: %s" % kwargs)

        self.canvas = canvas
        self.code = kwargs.pop('code', '')
        self.label = kwargs.pop('label', '')
        self.set_coords(*kwargs.pop('coords', ()))
        self.set_area_coords(*kwargs.pop('text_coords', ()))

        # Room optional settings

        option_show_code = kwargs.pop(
            'show_code',
            settings.ROOM_SHOW_CODE
        )

        option_bg_color = kwargs.pop(
            'bg_color', settings.ROOM_DEFAULT_BACKGROUND
        )

        self.options = {
            'show_code': bool(option_show_code),
            'bg_color': option_bg_color,
        }

        self.options.update(kwargs)  # Adds the rest

        # Hides code label if it's too wide
        if self.options['show_code']:
            code_width = self.text_size(settings.FONT_SIZE_MIN, self.code)[0]
            max_width = self.get_area_size(include_padding=True)[0]

            if code_width > max_width:
                self.options['show_code'] = False

    def set_coords(self, *coords):
        if len(coords) < 4 or len(coords) % 2 == 1:
            ex = "Invalid coordinates received : %s" % str(coords)
            raise ValueError(ex)
        elif len(coords) == 4:
            # Cleans received rectangle
            coords = utils.boundary_box(*coords)
            # Transforms rectangle into polygon
            self._coords = utils.rect_to_poly(*coords)
        else:
            self._coords = coords

    def get_coords(self):
        return self._coords

    def set_area_coords(self, *coords):
        if len(coords) < 4 or len(coords) % 2 == 1:
            # Invalid text area coords, use room coords instead
            area_coords = self.get_coords()
        else:
            area_coords = coords

        # Cleans coords to be used
        cleaned_coords = utils.boundary_box(*area_coords)

        self._text_area_coords = cleaned_coords

    def get_area_coords(self):
        return self._text_area_coords

    def get_area_size(self, include_padding=False):
        """
        Gets the size of the text area
        :param include_padding: If room padding should be included
        :return: tuple(width, height)
        """
        area_coords = self.get_area_coords()

        width = area_coords[2] - area_coords[0]  # maxX - minX
        height = area_coords[3] - area_coords[1]  # maxY - minY

        if include_padding:
            padding_size = self.get_padding_size()

            width -= padding_size[0] * 2
            height -= padding_size[1] * 2

        return width, height

    def get_padding_size(self):
        """
        Gets the size of the room text padding
        :return: list(width, height)
        """
        padding_w = settings.ROOM_TEXT_PADDING[0]
        padding_h = settings.ROOM_TEXT_PADDING[1]

        # Applies % padding on width if necessary
        if padding_w < 1:
            padding_w *= self.get_area_size()[0]
        if padding_h < 1:
            padding_h *= self.get_area_size()[1]

        return math.floor(padding_w), math.floor(padding_h)

    def get_display_text(self, label):
        """
        Returns the text as it would appear on the final image
        :param label: The processed label string
        :return:
        """
        # Applies room code if required
        if self.options['show_code']:
            if label:
                return "\n".join((label, self.code))
            else:
                return self.code
        else:
            return label

    def text_size(self, size, text):
        """
        Gets the size of the room label on the canvas
        :param size: The font size
        :param text: The text to display
        :return: tuple(width, height)
        """
        return self.canvas.multiline_textsize(
            text,
            font=font_size(size),
            spacing=settings.FONT_LINE_SPACING
        )

    def get_label_pos(self, size, text):
        """
        Gets the position of the room label to be draw at
        :param size: The size of the font
        :param text: The label text
        :return: tuple(x, y)
        """
        area_coords = self.get_area_coords()
        text_size = self.text_size(size, text)

        label_pos = (
            (area_coords[0] + area_coords[2] - text_size[0]) / 2,
            (area_coords[1] + area_coords[3] - text_size[1]) / 2
        )

        return label_pos

    def get_room_format(self):
        """
        Processes all string transformations on the room label
        and returns final display format
        :return: dict(size, text)
        """

        best_format = None
        truncate_attempt_nb = 0

        room_label = self.label

        # Important: Do NOT put inside below loop below!
        #   Will result in infinite loop if room size is too small!
        if settings.ALLOW_WORD_SPLIT:
            room_label = self.split_long_words(room_label)

        while best_format is None:
            truncate_attempt_nb += 1

            # New label, so empty old label logs
            self._log__room_format = []
            self._log__room_bump = {}

            # Fetches the right text format to fit in the text area
            if settings.DEBUG:
                print("****************************************")
                print("Searching for best result for \"%s\" :" %
                      room_label.replace("\n", "\\n"))

            best_format = self.get_best_format(
                settings.FONT_SIZE_MAX,
                room_label
            )

            if settings.DEBUG:
                print("Done.")

            # No format fits in text area
            if best_format is None:
                # Attempts to truncate text
                if settings.ALLOW_WORD_TRUNCATE:
                    if settings.DEBUG:
                        print("[WARNING] Text couldn't fit. "
                              "Truncating (attempt #%d)..." %
                              truncate_attempt_nb, end="")

                    if room_label == settings.TRUNCATE_STRING:
                        best_format = {
                            'size': settings.FONT_SIZE_MAX,
                            'text': settings.TRUNCATE_STRING
                        }
                    else:
                        room_label = truncate_text(room_label)

                    if settings.DEBUG:
                        print("Done.")
                        print("[WARNING] Text truncated to \"%s\"." %
                              room_label.replace("\n", "\\n"))
                else:
                    if settings.DEBUG:
                        print("[WARNING] Text couldn't fit and truncating "
                              "isn't allowed! Returning invalid string.")

                    best_format = {
                        'size': settings.FONT_SIZE_MAX,
                        'text': settings.TRUNCATE_STRING
                    }

        if settings.DEBUG:
            print("[SUCCESS] Result found: (%s, \"%s\")" %
                  (
                      best_format['size'],
                      best_format['text'].replace("\n", "\\n"))
                  )

        return best_format

    def get_best_format(self, size, text, depth=0):
        """
        Recursively gets the best font size and text settings
            that fits in the room
        :param size: The font size
        :param text: The text to display
        :param depth: Recursion level
        :return: dict(size, text)
        """
        depth += 1

        # Performs checks

        if not settings.FONT_SIZE_MIN <= size <= settings.FONT_SIZE_MAX:
            ex = "[ERROR] Invalid font size! " \
                 "Expected value to be [%d, %d] but got %d." %\
                 (settings.FONT_SIZE_MIN, settings.FONT_SIZE_MAX, size)
            raise ValueError(ex)

        # Checks if branch is already explored
        if (size, text) in self._log__room_format:
            if settings.DEBUG:
                print("Skipping; Already explored. ", end="")

            return None
        else:
            # New branch: proceed to the rest of the function
            self._log__room_format.append((size, text))

        # Checks completed; continue recursive process

        format_options = []

        text_size = self.text_size(size, self.get_display_text(text))
        area_size = self.get_area_size(include_padding=True)

        # text fits in text area, return as best format
        if (text_size[0] <= area_size[0]) & (text_size[1] <= area_size[1]):
            if settings.DEBUG:
                print("Fits at size %d! [%d] " % (size, depth), end="")

            return dict(size=size, text=text)
        elif settings.DEBUG:
            print("Fetching [%d]..." % depth, end="")

        # Shrink text option

        shrunk_size = size - settings.FONT_SIZE_STEP

        if shrunk_size >= settings.FONT_SIZE_MIN:
            if settings.DEBUG:
                print("Shrinking %d => %d..." % (size, shrunk_size), end="")

            option = self.get_best_format(shrunk_size, text, depth)
            if option:
                format_options.append(option)

        # Bump text option

        bumped_text = self.bump_text(text)

        if bumped_text != text:
            option = self.get_best_format(size, bumped_text, depth)
            if option:
                format_options.append(option)

        # Chooses best option and returns result
        best_format = choose_best_option(*format_options)

        return best_format

    def bump_text(self, text, bumps_wanted=None, store_result=True):
        """
        Bumps text to a new line and re-balances text
            to have the smallest width
        :param text: The text to be bumped
        :param bumps_wanted: Number of bumps wanted; defaults to +1
        :param store_result: If the method should store results found
                            (useful for unit testing)
        :return:
        """
        words = re.split(r"[ \n]+", text.strip())

        # Performs checks

        if bumps_wanted is None:
            # Default bumps_wanted
            bumps_wanted = text.count("\n") + 1

        if not 1 <= bumps_wanted <= len(words) - 1:
            # Nothing to do here!
            if settings.DEBUG:
                print("Skipping; Nothing to bump! ", end="")
            return text

        if bumps_wanted in self._log__room_bump:
            # Bump already calculated; Fetch results
            if settings.DEBUG:
                print("Try bump #%d! " % bumps_wanted, end="")
            return self._log__room_bump[bumps_wanted]

        # Checks completed; Proceed to bump text

        if len(words) == 2:
            # Text only has 1 bump option
            if settings.DEBUG:
                print("Bump!", end="")
            return text.replace(" ", "\n")
        elif len(words) > 2:
            # Text has multiple bump options, find best option
            # Discards previous bumps to get new optimized bump balance

            cmb_count = utils.combinations_count(len(words), bumps_wanted)
            total_bump_count = cmb_count * bumps_wanted

            if total_bump_count > settings.MAX_BUMP_JOB:
                if settings.DEBUG:
                    print("\n[WARNING] Too many combinations! "
                          "(%s) Skipping. " % total_bump_count, end="")
                return " ".join(words)

            # Everything is set; proceed with splitting

            if settings.DEBUG:
                print("\nProcessing %s bumps..." % total_bump_count, end="")

            best_option = {'text': text, 'width': 0}

            # Loops on bump options and finds smallest size
            for splits in combinations(range(1, len(words)), bumps_wanted):
                option = {'text': ''}
                prev_ind = 0

                for split_ind in splits:
                    bump_part = " ".join(words[prev_ind:split_ind]) + "\n"
                    option['text'] += bump_part

                    prev_ind = split_ind

                option['text'] += " ".join(words[prev_ind:len(words)])
                option['width'] = self.text_size(
                    settings.FONT_SIZE_MAX,
                    option['text']
                )[0]

                is_smaller = option['width'] < best_option['width']

                if is_smaller or best_option['width'] == 0:
                    best_option = option

            if settings.DEBUG:
                print("Bump! ", end="")

            # Logs bump for future usage
            if store_result:
                self._log__room_bump[bumps_wanted] = best_option['text']

            return best_option['text']

    def split_long_words(self, text):
        """
        Splits in half words that would be too long even at minimum font size
        :param text: Room text
        :return: Room text with splits on long words
        """
        max_width = self.get_area_size(include_padding=True)[0]
        words = re.split(r"[ \n]+", text.strip())

        for ind, word in enumerate(words):
            label_width = self.text_size(settings.FONT_SIZE_MIN, word)[0]

            if label_width > max_width:
                split = int(math.ceil(len(word) / 2))
                words[ind] = "-\n".join((word[:split], word[split:]))

        return " ".join(words)

    def draw(self):
        """
        Prints the room shape on the canvas
        :return:
        """
        self.canvas.polygon(
            self.get_coords(),
            fill=ImageColor.getrgb(self.options['bg_color'])
        )

    def print_label(self):
        """
        Prints the label on the canvas
        :return:
        """
        if not self.label and not self.code:
            return  # No label to display

        room_format = self.get_room_format()

        display_text = self.get_display_text(room_format['text'])

        label_pos = self.get_label_pos(
            room_format['size'],
            display_text
        )

        self.canvas.multiline_text(
            label_pos,
            display_text,
            font=font_size(room_format['size']),
            fill=ImageColor.getrgb(settings.FONT_COLOR),
            spacing=settings.FONT_LINE_SPACING,
            align=settings.ROOM_TEXT_ALIGN
        )


def truncate_text(text):
    """
    Truncates the room text by removing either the last word
        or parts of it
    :param text: Text to be truncated
    :return: Truncated text
    """
    truncate_string = settings.TRUNCATE_STRING
    smallest_word_split = settings.SMALLEST_WORD_SPLIT

    if text == truncate_string:
        return text  # Can't truncate anything

    words = re.split(r"[ \n]+", text.strip())

    last_word = words.pop()

    # Skips fully truncated string
    if last_word == truncate_string:
        last_word = words.pop()

    truncated = last_word[0:smallest_word_split] + truncate_string

    is_too_short = len(last_word) <= smallest_word_split

    if is_too_short or last_word.endswith(truncate_string):
        # Fully truncates truncated last word
        last_word = truncate_string
    else:
        last_word = truncated

    # Applies truncated last word
    words.append(last_word)
    return " ".join(words)


def choose_best_option(*format_opts):
    """
    Chooses which option should take priority over the others
    Typically, which option looks the best in the end result
    :param format_opts: list of options as {size, text}
    :return: dict(size, text) or None if no options
    """
    if format_opts:
        best_opt = format_opts[0]  # Defaults to the first option

        for opt in format_opts:
            opt_length = len(opt['text'].splitlines())
            best_opt_length = len(best_opt['text'].splitlines())

            is_bigger = opt['size'] > best_opt['size']
            is_same_size = opt['size'] == best_opt['size']
            is_taller = opt_length > best_opt_length

            if is_bigger or (is_same_size and is_taller):
                best_opt = opt

        return best_opt
    else:
        return None


def font_size(size):
    return ImageFont.truetype(
        os.path.join(
            settings.MEDIA_ROOT,
            settings.FONTS_DIR,
            settings.FONT_FACE
        ), size=size
    )
