# coding: utf-8

import os
from django.conf import settings as django_settings

"""
FLOOR MAP SETTINGS
------------------
- These settings apply to the general display of the floor map
- Replaced by settings provided during initialization
- For settings on individual rooms see section below
"""

"""
Django installation (DO NOT CHANGE MANUALLY HERE!)
"""
DEBUG = django_settings.DEBUG

BASE_DIR = django_settings.BASE_DIR
FLOOR_MAP_DIR = os.path.join(BASE_DIR, 'app', 'floorMap')
STATIC_DIR = os.path.join(FLOOR_MAP_DIR, 'static')

"""
Media
"""
INPUT_FILENAME = "floor_map_base.jpg"
OUTPUT_FILENAME = "floor_map.jpg"
FONT_FACE = "arial.ttf"

FONT_DIR = os.path.join(STATIC_DIR, 'fonts')
IMAGE_DIR = os.path.join(STATIC_DIR, 'img')

FONT_TYPE = os.path.join(FONT_DIR, FONT_FACE)
INPUT_IMAGE = os.path.join(IMAGE_DIR, INPUT_FILENAME)
OUTPUT_IMAGE = os.path.join(IMAGE_DIR, OUTPUT_FILENAME)

"""
Optimization options
"""
FONT_SIZE_STEP = 1
# Acceptable values range from 0 to 100
#   100 being the best
IMAGE_QUALITY = 100
# Amount of combinations needed for script to skip
MAX_BUMP_JOB = 5000

"""
Label transformations
"""
ALLOW_WORD_SPLIT = True
ALLOW_WORD_TRUNCATE = True

SMALLEST_WORD_SPLIT = 3
# Also the display string if the options above are False
TRUNCATE_STRING = '...'

"""
Label text
"""
FONT_COLOR = "#000000"
FONT_SIZE_MIN = 10
FONT_SIZE_MAX = 24
FONT_LINE_SPACING = 4

"""
Global room display
- See room settings section for individual room options
"""
ROOM_DEFAULT_BACKGROUND = "#FFFFFF"
ROOM_TEXT_PADDING = (0.05, 0.05)
ROOM_TEXT_ALIGN = 'center'

"""
ROOM SETTINGS
-------------
- Sets default values for individual rooms
- Replaced by settings provided during initialization
"""

ROOM_SHOW_CODE = True
