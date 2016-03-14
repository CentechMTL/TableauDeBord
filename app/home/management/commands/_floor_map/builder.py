# coding: utf-8

from __future__ import division
from __future__ import print_function

import math
import os
import re
from itertools import combinations
from PIL import Image, ImageDraw, ImageFont

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
            os.path.join(settings.MEDIA_ROOT, settings.PROJECT_DIR, settings.INPUT_FILENAME)
        )
        self.floor_map_image = Image.open(input_file)
        self.canvas = ImageDraw.Draw(self.floor_map_image)

    def add_room(self, **kwargs):
        new_room = Room(self.canvas, **kwargs)
        self._rooms.append(new_room)

    def render_image(self):
        if settings.DEBUG or settings.FORCE_DEBUG:
            print("****************************************")
            print("Rendering %d entities:" % len(self._rooms))

        for room in self._rooms:
            room.draw()
            room.print_label()

        if settings.DEBUG or settings.FORCE_DEBUG:
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
            os.path.join(settings.MEDIA_ROOT, settings.PROJECT_DIR, settings.OUTPUT_FILENAME)
        )
        quality = kwargs.pop('quality', settings.IMAGE_QUALITY)

        self.floor_map_image.save(output_file, quality=quality)

        if settings.DEBUG or settings.FORCE_DEBUG:
            print("[SUCCESS] A new copy was saved at %s" % output_file)


# Parent class for rooms
class Room:
    canvas = None
    options = None

    label = ""  # Text to display on the room
    code = ""  # physical room code
    _coords = []  # Coordinates of the room shape. ALWAYS a polygon. Will be converted if initialized with a rectangle
    _text_area_coords = []  # Coordinates of the rectangle defining the zone where label can be printed

    _log__room_format = []  # Stores all explored formats
    _log__room_bump = {}  # Stores already calculated bumped texts

    def __init__(self, canvas, **kwargs):
        if settings.DEBUG or settings.FORCE_DEBUG:
            print("Adding new entity with attributes: %s" % kwargs)

        self.canvas = canvas
        self.code = kwargs.pop('code', '')
        self.label = kwargs.pop('label', '')
        self.set_coords(*kwargs.pop('coords', ()))
        self.set_area_coords(*kwargs.pop('text_coords', ()))

        self.options = {
            'show_code': bool(kwargs.pop('show_code', settings.ROOM_SHOW_CODE)),
            'bg_color': kwargs.pop('bg_color', settings.ROOM_DEFAULT_BACKGROUND),
        }

        self.options.update(kwargs)

        # Hides code label if it's too wide
        if self.options['show_code']:
            code_width = self.text_size(settings.FONT_SIZE_MIN, self.code)[0]
            max_width = self.get_area_size()[0]

            if code_width > max_width:
                self.options['show_code'] = False

    def set_coords(self, *coords):
        if len(coords) < 4 or len(coords) % 2 == 1:
            ex = "Invalid coordinates received : %s" % str(coords)
            raise ValueError(ex)

        if len(coords) == 4:
            # Transforms rectangle into polygon
            coords = utils.rect_to_poly(*coords)

        self._coords = coords

    def get_coords(self):
        return self._coords

    def set_area_coords(self, *coords):
        if len(coords) >= 4 and len(coords) % 2 == 0:
            # Cleans received text area & makes sure the coords are in the correct order
            cleaned_coords = utils.boundary_box(*coords)
        else:
            # Generates a default text area around the room coordinates
            cleaned_coords = utils.boundary_box(*self.get_coords())

        self._text_area_coords = cleaned_coords

    def get_area_coords(self):
        return self._text_area_coords

    def get_area_size(self, include_padding=True):
        """
        Gets the size of the text area
        :param include_padding: If room padding should be included
        :return: tuple[width, height]
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
        :return: list[width, height]
        """
        padding_w = settings.ROOM_TEXT_PADDING[0]
        padding_h = settings.ROOM_TEXT_PADDING[1]

        # Applies % padding on width if necessary
        if padding_w < 1:
            padding_w *= self.get_area_size(include_padding=False)[0]
        if padding_h < 1:
            padding_h *= self.get_area_size(include_padding=False)[1]

        return math.floor(padding_w), math.floor(padding_h)

    def get_display_text_size(self, size, text):
        """
        Returns the size of text as it would appear on the final image
        Not to be confused with text_size() which does not include all final settings like room code display
        :param size: The font size of the text
        :param text: The text to display (excluding label, if any)
        :return: tuple(width, height)
        """
        # Applies room code if required
        if self.options['show_code']:
            if self.label:
                display_text = "\n".join((text, self.code))
            else:
                display_text = self.code
        else:
            display_text = text

        return self.text_size(size, display_text)

    def get_text_size(self, size, text):
        """
        Gets the size of the room label + code
        :param size: The font size of the text
        :param text: The text to display (excluding label, if any)
        :return: tuple[width, height]
        """
        font = ImageFont.truetype(settings.FONT_FACE, size=size)
        text_size = self.canvas.multiline_textsize(text, font=font, spacing=settings.FONT_LINE_SPACING)

        return text_size

    def get_label_pos(self, size, text):
        room_coords = self.get_coords()
        area_size = self.get_area_size(include_padding=False)
        label_size = self.get_display_text_size(size, text)

        label_pos = (
            room_coords[0] + (area_size[0] - label_size[0]) / 2,
            room_coords[1] + (area_size[1] - label_size[1]) / 2
        )

        return label_pos

    def get_room_format(self):
        """
        Processes all string transformations on the room label and returns final display format
        :return: dict(size, text)
        """

        best_format = None
        truncate_attempt_nb = 0

        room_label = self.label

        # Important: Do NOT put inside below loop! Will result in infinite loop if room size is too small!
        if settings.ALLOW_WORD_SPLIT:
            room_label = self.split_long_words(room_label)

        while best_format is None:
            truncate_attempt_nb += 1

            # New label, so empty old label logs
            self._log__room_format = []
            self._log__room_bump = {}

            # Fetches the right text format to fit in the text area
            if settings.DEBUG or settings.FORCE_DEBUG:
                print("****************************************")
                print("Searching for best result for \"%s\" :" % room_label.replace("\n", "\\n"))

            best_format = self.get_best_format(settings.FONT_SIZE_MAX, room_label)

            if settings.DEBUG or settings.FORCE_DEBUG:
                print("Done.")

            # No format fits in text area
            if best_format is None:
                # Attempts to truncate text
                if settings.ALLOW_WORD_TRUNCATE:
                    if settings.DEBUG or settings.FORCE_DEBUG:
                        print("[WARNING] Text couldn't fit. Truncating (attempt #%d)..." % truncate_attempt_nb, end="")

                    if room_label == settings.TRUNCATE_STRING:
                        best_format = {'size': settings.FONT_SIZE_MAX, 'text': settings.TRUNCATE_STRING}
                    else:
                        room_label = self.truncate_text(room_label)

                    if settings.DEBUG or settings.FORCE_DEBUG:
                        print("Done.")
                        print("[WARNING] Text truncated to \"%s\"." % room_label.replace("\n", "\\n"))
                else:
                    if settings.DEBUG or settings.FORCE_DEBUG:
                        print("[WARNING] Text couldn't fit and truncating isn't allowed! Returning invalid string.")

                    best_format = {'size': settings.FONT_SIZE_MAX, 'text': settings.TRUNCATE_STRING}

        if settings.DEBUG or settings.FORCE_DEBUG:
            print("[SUCCESS] Result found: (%s, \"%s\")" %
                  (best_format['size'], best_format['text'].replace("\n", "\\n")))

        if self.options['show_code']:
            if room_label:
                display_text = "\n".join((best_format['text'], self.code))
            else:
                display_text = self.code
        else:
            display_text = best_format['text']

        format_final = {
            'size': best_format['size'],
            'text': display_text,
        }

        return format_final

    def get_best_format(self, size, text, depth=0):
        """
        Recursively gets the best font size and text settings to fit in the room
        :param size: The font size
        :param text: The text to display
        :param depth: Recursion level
        :return: dict(size, text)
        """
        depth += 1

        # Performs checks

        if not settings.FONT_SIZE_MIN <= size <= settings.FONT_SIZE_MAX:
            ex = "[ERROR] Invalid font size! Expected value to be [%d, %d] but got %d." %\
                 (settings.FONT_SIZE_MIN, settings.FONT_SIZE_MAX, size)
            raise ValueError(ex)

        # Checks if branch is already explored
        if (size, text) in self._log__room_format:
            if settings.DEBUG or settings.FORCE_DEBUG:
                print("Skipping; Already explored. ", end="")

            return None
        else:
            # New branch: proceed to the rest of the function
            self._log__room_format.append((size, text))

        # Checks completed; continue recursive process

        format_options = []

        text_size = self.get_display_text_size(size, text)
        area_size = self.get_area_size()

        # text fits in text area, return as best format
        if (text_size[0] <= area_size[0]) & (text_size[1] <= area_size[1]):
            if settings.DEBUG or settings.FORCE_DEBUG:
                print("Fits at size %d! [%d] " % (size, depth), end="")

            return dict(size=size, text=text)
        elif settings.DEBUG or settings.FORCE_DEBUG:
            print("Fetching [%d]..." % depth, end="")

        # Shrink text option

        shrunk_size = size - settings.FONT_SIZE_STEP

        if shrunk_size >= settings.FONT_SIZE_MIN:
            if settings.DEBUG or settings.FORCE_DEBUG:
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
        best_format = self.choose_best_option(*format_options)

        return best_format

    def choose_best_option(self, *format_opts):
        """
        Chooses which option should take priority over the others
        Typically, which option looks the best in the end result
        :param format_opts: list of dict(size, text)
        :return: dict(size, text) or None if list is empty
        """
        if format_opts:
            best_opt = format_opts[0]  # Defaults to the first option

            for opt in format_opts:
                is_bigger = opt['size'] > best_opt['size']
                is_same_size = opt['size'] == best_opt['size']
                is_taller = len(opt['text'].splitlines()) > len(best_opt['text'].splitlines())

                if is_bigger or (is_same_size and is_taller):
                    best_opt = opt

            return best_opt
        else:
            return None

    def bump_text(self, text, bumps_wanted=None, store_result=True):
        """
        Bumps text to a new line and re-balances text to have the smallest width
        :param text: The text to be bumped
        :param bumps_wanted: Number of bumps wanted; defaults to +1
        :param store_result: If the method should store results found (useful for unit testing)
        :return:
        """
        words = re.split(r"[ \n]+", text.strip())

        # Performs checks

        if bumps_wanted is None:
            # Default bumps_wanted
            bumps_wanted = text.count("\n") + 1

        if not 1 <= bumps_wanted <= len(words) - 1:
            # Nothing to do here!
            if settings.DEBUG or settings.FORCE_DEBUG:
                print("Skipping; Nothing to bump! ", end="")
            return text

        if bumps_wanted in self._log__room_bump:
            # Bump already calculated; Fetch results
            if settings.DEBUG or settings.FORCE_DEBUG:
                print("Try bump #%d! " % bumps_wanted, end="")
            return self._log__room_bump[bumps_wanted]

        # Checks completed; Proceed to bump text

        if len(words) == 2:
            # Text only has 1 bump option
            if settings.DEBUG or settings.FORCE_DEBUG:
                print("Bump!", end="")
            return text.replace(" ", "\n")
        elif len(words) > 2:
            # Text has multiple bump options, find best option
            # Discards previous bumps to get new optimized bump balance

            total_bump_count = utils.combinations_count(len(words), bumps_wanted) * bumps_wanted

            if total_bump_count > settings.MAX_BUMP_JOB:
                if settings.DEBUG or settings.FORCE_DEBUG:
                    print("\n[WARNING] Too many combinations! (%s) Skipping. " % total_bump_count, end="")
                return " ".join(words)

            # Everything is set; proceed with splitting

            if settings.DEBUG or settings.FORCE_DEBUG:
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
                option['width'] = self.text_size(settings.FONT_SIZE_MAX, option['text'])[0]

                if option['width'] < best_option['width'] or best_option['width'] == 0:
                    best_option = option

            if settings.DEBUG or settings.FORCE_DEBUG:
                print("Bump! ", end="")

            # Logs bump for future usage
            if store_result:
                self._log__room_bump[bumps_wanted] = best_option['text']

            return best_option['text']

    def truncate_text(self, text):
        """
        Truncates the room text by removing either the last word or parts of it
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

        if last_word.endswith(truncate_string) or len(last_word) <= smallest_word_split:
            # Fully truncates truncated last word
            last_word = truncate_string
        else:
            last_word = truncated

        # Applies truncated last word
        words.append(last_word)
        return " ".join(words)

    def split_long_words(self, text):
        """
        Splits in half words that would be too long even at the minimum font size
        :param text: Room text
        :return: Room text with splits on long words
        """
        max_width = self.get_area_size()[0]
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
        self.canvas.polygon(self.get_coords(), fill=self.options['bg_color'])

    def print_label(self):
        """
        Prints the label on the canvas
        :return:
        """
        if not self.label and not self.code:
            return  # No label to display

        room_format = self.get_room_format()
        label_pos = self.get_label_pos(room_format['size'], room_format['text'])

        self.canvas.multiline_text(
            label_pos,
            room_format['text'],
            font=ImageFont.truetype(settings.FONT_FACE, size=room_format['size']),
            fill=settings.FONT_COLOR,
            spacing=settings.FONT_LINE_SPACING,
            align=settings.ROOM_TEXT_ALIGN
        )
