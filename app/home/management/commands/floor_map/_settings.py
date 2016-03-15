# coding: utf-8

from django.conf import settings as django_settings

# FLOOR MAP SETTINGS
#
# These settings apply to the general display of the floor map
# See section below for the room settings display to set a default option for room settings

# Django installation
# DO NOT CHANGE!
DEBUG = django_settings.DEBUG
MEDIA_ROOT = django_settings.MEDIA_ROOT

# Media
PROJECT_DIR = "floor_map"
FONTS_DIR = "fonts"
INPUT_FILENAME = "floor_map_base.jpg"
OUTPUT_FILENAME = "floor_map.jpg"

# Optimization
FONT_SIZE_STEP = 1
IMAGE_QUALITY = 100  # Acceptable values = [0, 100]
MAX_BUMP_JOB = 5000  # Script will skip if amount of combinations to do is greater than this value

# Label transformations
ALLOW_WORD_SPLIT = True
ALLOW_WORD_TRUNCATE = True

SMALLEST_WORD_SPLIT = 3
TRUNCATE_STRING = '...'

# Label font
FONT_FACE = 'arial.ttf'
FONT_COLOR = (0, 0, 0, 255)  # RGBA support
FONT_SIZE_MIN = 10
FONT_SIZE_MAX = 24
FONT_LINE_SPACING = 4

# Room displaying
ROOM_DEFAULT_BACKGROUND = (255, 255, 255, 255)
ROOM_TEXT_PADDING = (0.05, 0.05)
ROOM_TEXT_ALIGN = 'center'

# ROOM SETTINGS
#
# Sets a default value for individual room options if none was given at their creation

ROOM_SHOW_CODE = True
