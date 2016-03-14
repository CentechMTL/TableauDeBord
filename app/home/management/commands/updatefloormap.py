# coding: utf-8

from django.core.management.base import BaseCommand
from django.conf import settings
from app.home.models import Room
from floor_map.builder import FloorMapBuilder
from ast import literal_eval

# ToDo: Add color field in RoomType
# Colors
CLR_GREY = (200, 200, 200)
CLR_ORANGE = (250, 147, 29)
CLR_VIOLET = (175, 41, 76)
CLR_RED = (240, 61, 67)
# ToDo end


class Command(BaseCommand):
    help = 'Force refresh the floor map image(s)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--input',
            default=False,
            help='Input filename')
        parser.add_argument(
            '--output',
            default=False,
            help='Output filename'
        )

    def handle(self, *args, **options):
        map_settings = {
            'MEDIA_ROOT': settings.MEDIA_ROOT,
            'DEBUG': settings.DEBUG
        }

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
                else:
                    room_label = "Libre"
            else:
                room_label = room.static_label

            # ToDo: Fetch color from color field in RoomType options
            if room.type_id == 1:
                bg_color = CLR_GREY
            elif room.type_id == 2:
                bg_color = CLR_VIOLET
            elif room.type_id == 3:
                if company:
                    bg_color = CLR_ORANGE
                else:
                    bg_color = CLR_RED
            else:
                bg_color = CLR_GREY
            # ToDo end

            # Required data:

            data = {
                'label': room_label,
                'code': room.code,
                'coords': literal_eval(room.coords),
                'show_code': bool(room.code),
                'bg_color': bg_color,
            }

            # Optional data:

            if room.text_coords:
                data['text_coords'] = literal_eval(room.text_coords)

            # Sends data to the map builder
            floor_map.add_room(**data)

        floor_map.render_image()
        floor_map.save(**options)
