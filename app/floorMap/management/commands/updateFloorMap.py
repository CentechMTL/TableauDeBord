# coding: utf-8

import os
import logging

from ast import literal_eval
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from app.floorMap.management.commands.scripts.builder import FloorMapBuilder
from app.floorMap.models import Room


logger = logging.getLogger('django')


class Command(BaseCommand):
    help = 'Force refresh the floor map image(s)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--input',
            default=os.path.join(
                settings.MEDIA_ROOT, "floor_map", "floor_map_base.jpg"
            ),
            help='Input filename'
        )
        parser.add_argument(
            '--output',
            default=os.path.join(
                settings.MEDIA_ROOT, "floor_map", "floor_map.jpg"
            ),
            help='Output filename'
        )

    def handle(self, *args, **options):
        logger.info("{timestamp} Updating floor map image ...".format(
            timestamp=datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"),
        ))

        map_settings = {}

        if options['input']:
            map_settings['input'] = options['input']

        if options['output']:
            map_settings['output'] = options['output']

        floor_map = FloorMapBuilder(**map_settings)

        for room in Room.objects.all():
            company = room.get_owner_name()

            if room.is_rental():
                if company:
                    room_label = company
                    bg_color = room.type.bg_color
                else:
                    room_label = "Libre"
                    bg_color = room.type.alt_bg_color
            else:
                room_label = room.static_label
                bg_color = room.type.bg_color

            # Required data:

            data = {
                'code': room.code,
                'coords': literal_eval(room.coords),
                'show_code': bool(room.code),
                'bg_color': bg_color,
            }

            # Optional data:

            if room.text_coords:
                data['text_coords'] = literal_eval(room.text_coords)

            if room.static_label:
                data['label'] = room_label

            # Sends data to the map builder
            floor_map.add_room(**data)

        floor_map.render_image()
        floor_map.save(**map_settings)

        logger.info("{timestamp} Saved image at {path}".format(
            timestamp=datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"),
            path=os.path.relpath(map_settings['output'], settings.BASE_DIR),
        ))
