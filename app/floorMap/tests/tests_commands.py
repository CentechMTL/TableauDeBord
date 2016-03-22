# coding: utf-8

from __future__ import division

import datetime
import os

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase

from app.company.factories import CompanyFactory, CompanyStatusFactory
from app.floorMap.management.commands.scripts.builder import FloorMapBuilder, \
    font_size, truncate_text
from app.floorMap.factories import RentFactory, RoomFactory, RoomTypeFactory


class UpdateFloorMap(TestCase):
    ImageIn = "floor_map_base.jpg"
    ImageOut = "floor_map_test.jpg"
    ImagePathIn = os.path.join(settings.MEDIA_ROOT, "floor_map", ImageIn)
    ImagePathOut = os.path.join(settings.MEDIA_ROOT, "floor_map", ImageOut)

    def setUp(self):
        self.room_type_1 = RoomTypeFactory(id=1)
        self.room_type_2 = RoomTypeFactory(id=2)
        self.room_type_3 = RoomTypeFactory(id=3, is_rental=True)
        self.room_type_4 = RoomTypeFactory(id=4)

        self.room = RoomFactory(type=self.room_type_1)

    def test_room_types(self):
        """
        Tests script execution with all room types
        """

        self.room_1 = RoomFactory(type=self.room_type_1)
        self.room_2 = RoomFactory(type=self.room_type_2)
        self.room_3 = RoomFactory(type=self.room_type_3)
        self.room_4 = RoomFactory(type=self.room_type_4)
        call_command(
            'updateFloorMap',
            input=self.ImagePathIn,
            output=self.ImagePathOut
        )
        self.assertTrue(os.path.isfile(self.ImagePathOut))
        os.remove(self.ImagePathOut)

    def test_rooms(self):
        """
        Tests script execution with room data to display
        """

        # Rectangles
        self.room.coords = [0, 0, 100, 100]
        self.room.save()
        call_command('updateFloorMap', output=self.ImagePathOut)
        self.assertTrue(os.path.isfile(self.ImagePathOut))
        os.remove(self.ImagePathOut)

        # Polygons
        self.room.coords = [0, 0, 100, 100, 200, 200, 300, 300, 0, 300]
        self.room.text_coords = [100, 200, 200, 300]
        self.room.save()
        call_command('updateFloorMap', output=self.ImagePathOut)
        self.assertTrue(os.path.isfile(self.ImagePathOut))
        os.remove(self.ImagePathOut)

        """ String transformations """

        self.room.coords = [0, 0, 100, 100]
        self.room.text_coords = None

        # With static label and code
        self.room.code = "C-0000"
        self.room.static_label = "Xyz Xyz"
        self.room.save()
        call_command('updateFloorMap', output=self.ImagePathOut)
        self.assertTrue(os.path.isfile(self.ImagePathOut))
        os.remove(self.ImagePathOut)

        # No label and no code
        self.room.static_label = ""
        self.room.code = ""
        self.room.save()
        call_command('updateFloorMap', output=self.ImagePathOut)
        self.assertTrue(os.path.isfile(self.ImagePathOut))
        os.remove(self.ImagePathOut)

        # With static label but no code
        self.room.static_label = "Xyz Xyz"
        self.room.code = ""
        self.room.save()
        call_command('updateFloorMap', output=self.ImagePathOut)
        self.assertTrue(os.path.isfile(self.ImagePathOut))
        os.remove(self.ImagePathOut)

    def test_rentals(self):
        """
        Tests script execution with rentals to display
        """

        self.status = CompanyStatusFactory()
        self.company = CompanyFactory(companyStatus=self.status)

        self.rent = RentFactory(company=self.company, room=self.room)

        self.room.type = self.room_type_3
        self.room.coords = [0, 0, 500, 100]
        self.room.save()

        # Rental currently in application
        time_diff = datetime.timedelta(days=10)
        self.rent.date_start = datetime.datetime.today() - time_diff
        self.rent.date_end = datetime.datetime.today() + time_diff
        self.rent.save()
        call_command('updateFloorMap', output=self.ImagePathOut)
        self.assertTrue(os.path.isfile(self.ImagePathOut))
        os.remove(self.ImagePathOut)

    def test_floor_map(self):
        """
        Tests FloorMap class from the script
        """

        options = {
            'input': self.ImagePathIn,
            'output': os.path.join(
                settings.MEDIA_ROOT,
                "floor_map",
                "floor_map.jpg"
            ),
            'DEBUG': True,
            'ROOM_TEXT_PADDING': (0.05, 0.05),
            'FONT_FACE': 'arial.ttf',
            'FONT_LINE_SPACING': 4,
            'TRUNCATE_STRING': '...',
            'SMALLEST_WORD_SPLIT': 3,
            'MAX_BUMP_JOB': 1000,
            'FONT_SIZE_MIN': 10,
            'FONT_SIZE_MAX': 24,
        }

        floor_map = FloorMapBuilder(**options)
        canvas = floor_map.canvas

        data = {
            'label': "COMPANY",
            'code': "C-0000000000000000000000000000000000000",
            'coords': (0, 0, 200, 200),
            'show_code': True,
            'bg_color': "#434343",
            'fake_option': 42,
        }

        floor_map.add_room(**data)

        self.assertEqual(1, len(floor_map._rooms))
        room = floor_map._rooms[0]

        font_24 = font_size(24)

        # Test room variable initialization
        self.assertEqual(room.label, "COMPANY")
        self.assertEqual(room.code, "C-0000000000000000000000000000000000000")
        self.assertTupleEqual(
            room.get_coords(),
            (0, 0, 200, 0, 200, 200, 0, 200)
        )
        self.assertTupleEqual(room.get_area_coords(), (0, 0, 200, 200))

        self.assertDictEqual(
            room.options,
            {
                'show_code': False,
                'bg_color': "#434343",
                'fake_option': 42
            }
        )

        # Test accessors
        self.assertTupleEqual(
            room.get_area_size(include_padding=False),
            (200, 200)
        )
        self.assertTupleEqual(
            room.get_area_size(include_padding=True),
            (180, 180)
        )
        self.assertTupleEqual(
            room.get_padding_size(), (10, 10)
        )

        # Test text_size()

        # Without room code
        room.options['show_code'] = False
        self.assertTupleEqual(
            room.text_size(24, room.get_display_text("Label")),
            canvas.multiline_textsize("Label", font=font_24, spacing=4)
        )

        # With room code
        room.code = "C-1230"
        room.options['show_code'] = True
        self.assertTupleEqual(
            room.text_size(24, room.get_display_text("A")),
            canvas.multiline_textsize("A\nC-1230", font=font_24, spacing=4)
        )

        # Test get_label_pos()
        room.set_area_coords(100, 100, 400, 200)
        room.set_coords(100, 100, 400, 200)
        room.options['show_code'] = True
        room.code = "C-0000"
        text_size = canvas.multiline_textsize(
            "Label\nCode\nC-0000",
            font=font_24,
            spacing=4
        )
        display_text = room.get_display_text("Label\nCode")

        self.assertEqual(display_text, "Label\nCode\nC-0000")
        self.assertTupleEqual(
            room.get_label_pos(24, display_text),
            (250 - text_size[0] / 2, 150 - text_size[1] / 2)
        )

        # Test long word splitting
        room.set_area_coords(0, 0, 50, 50)
        room.set_coords(0, 0, 50, 50)
        self.assertEqual(
            room.split_long_words("123456789 12345"),
            "12345-\n6789 12345"
        )

        # Test word truncate
        self.assertEqual(truncate_text("0000 0000"), "0000 000...")
        self.assertEqual(truncate_text("0000 000"), "0000 ...")
        self.assertEqual(truncate_text("0000"), "000...")
        self.assertEqual(truncate_text("000"), "...")
        self.assertEqual(truncate_text("0000 0000 ..."), "0000 000...")
        self.assertEqual(truncate_text("0000 000 ..."), "0000 ...")
        self.assertEqual(truncate_text("0000 000..."), "0000 ...")
        self.assertEqual(truncate_text("0000 ..."), "000...")
        self.assertEqual(truncate_text("000 ..."), "...")
        self.assertEqual(truncate_text("000..."), "...")
        self.assertEqual(truncate_text("..."), "...")

        # Test text bumping
        room._log__room_bump = {}
        self.assertEqual(room.bump_text("000", 1, False), "000")
        self.assertEqual(room.bump_text("000 111", 0, False), "000 111")
        self.assertEqual(room.bump_text("000 111", 2, False), "000 111")
        self.assertEqual(room.bump_text("000 111", 1, False), "000\n111")
        self.assertEqual(room.bump_text("000\n111", 1, False), "000\n111")
        self.assertEqual(room.bump_text(
            "000\n111 222", 1, False),
            "000\n111 222")
        self.assertEqual(room.bump_text(
            "000 111\n222", 1, False),
            "000\n111 222")
        self.assertEqual(room.bump_text(
            "000 111 222", 2, False),
            "000\n111\n222")
        self.assertEqual(room.bump_text(
            "000\n111 222", 2, False),
            "000\n111\n222")
        self.assertEqual(room.bump_text(
            "000\n111\n222", 2, False),
            "000\n111\n222")
        self.assertEqual(room.bump_text(
            "0 111 2 3 44 555555", 1, False),
            "0 111 2 3\n44 555555")
        self.assertEqual(room.bump_text(
            "0 111 2 3 44 555555", 2, False),
            "0 111\n2 3 44\n555555")
        self.assertEqual(room.bump_text(
            "1 1 1 1 1 1 1 1", 1, False),
            "1 1 1 1\n1 1 1 1")
        self.assertEqual(room.bump_text(
            "1 1 1 1 1 1 1 1", 2, False),
            "1 1\n1 1 1\n1 1 1")
        self.assertEqual(room.bump_text(
            "1 1 1 1 1 1 1 1", 3, False),
            "1 1\n1 1\n1 1\n1 1")
        self.assertEqual(room.bump_text(
            "1 1 1 1 1 1 1 1", 4, False),
            "1\n1\n1 1\n1 1\n1 1")
        self.assertEqual(room.bump_text(
            "1 1 1 1 1 1 1 1 1 1", 5, False),
            "1 1 1 1 1 1 1 1 1 1")

        # Test bump result logging
        room._log__room_bump = {}
        room.bump_text("A B C D", 1, store_result=True)
        room.bump_text("A B C D", 2, store_result=True)
        room.bump_text("A B C D", 2, store_result=True)
        self.assertEqual(len(room._log__room_bump), 2)
        self.assertEqual(room._log__room_bump[1], "A B\nC D")
        self.assertEqual(room._log__room_bump[2], "A B\nC\nD")

        # Test final format

        room.set_coords(0, 0, 100, 100)
        room.set_area_coords(0, 0, 100, 100)

        room.label = ""
        room.code = ""
        room.options['show_code'] = False
        self.assertDictEqual(room.get_room_format(), dict(size=24, text=""))

        room.label = "000 111"
        room.code = ""
        self.assertDictEqual(
            room.get_room_format(),
            {'size': 24, 'text': "000 111"}
        )

        room.label = ""
        room.code = "C-1230"
        room.options['show_code'] = True
        self.assertDictEqual(
            room.get_room_format(),
            {'size': 24, 'text': ""}
        )

        room.label = "000000 111111"
        self.assertDictEqual(
            room.get_room_format(),
            {'size': 24, 'text': "000000\n111111"}
        )

        room.label = "000000000000.0.0 11"
        self.assertDictEqual(
            room.get_room_format(),
            {'size': 11, 'text': "000000000000.0.0\n11"}
        )

        # When best_format() fails
        room.label = "One Fish Two Fish Red Fish Blue Fish"
        room.set_area_coords(0, 0, 10, 10)
        self.assertDictEqual(room.get_room_format(), dict(size=24, text="..."))

        del floor_map

        # Tests with ALLOW_WORD_TRUNCATE set to off

        options = {
            'input': self.ImagePathIn,
            'ALLOW_WORD_TRUNCATE': False
        }

        floor_map = FloorMapBuilder(**options)

        data = {
            'label': "COMPANY",
            'coords': (0, 0, 10, 10),
        }

        floor_map.add_room(**data)
        room = floor_map._rooms[0]

        self.assertDictEqual(room.get_room_format(), dict(size=24, text="..."))

        # Test ValueError exceptions

        with self.assertRaises(ValueError):
            room.get_best_format(9, "")
        with self.assertRaises(ValueError):
            room.get_best_format(25, "")
        with self.assertRaises(ValueError):
            room.set_coords(0, 0)
        with self.assertRaises(ValueError):
            room.set_coords(0, 0, 10, 10, 11)

        del floor_map
