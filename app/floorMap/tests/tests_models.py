# coding: utf-8

from datetime import date, timedelta

from django.test import TestCase

from app.company.factories import CompanyFactory, CompanyStatusFactory
from app.floorMap.factories import RoomTypeFactory, RoomFactory, RentFactory

from app.floorMap.models import RoomType, Room, Rent


class CompanyModelsTest(TestCase):

    def setUp(self):
        self.status = CompanyStatusFactory()
        self.company = CompanyFactory(companyStatus=self.status)

        self.room_type_1 = RoomTypeFactory(is_rental=True)
        self.room_type_2 = RoomTypeFactory()

        self.room_1 = RoomFactory(type=self.room_type_1)
        self.room_2 = RoomFactory(type=self.room_type_2)

    def test_room(self):
        self.assertTrue(self.room_1.is_rental())
        self.assertFalse(self.room_2.is_rental())

        yesterday = date.today() - timedelta(1)
        today = date.today()
        tomorrow = date.today() + timedelta(1)

        rent_1 = RentFactory(
            company=self.company,
            room=self.room_1,
            date_start=yesterday,
            date_end=yesterday
        )

        self.assertEqual(1, len(self.room_1.rentals.all()))

        self.assertEqual(rent_1, self.room_1.rentals.all().first())

        self.assertFalse(self.room_1.get_active_rental())
        self.assertFalse(self.room_1.get_upcoming_rentals())
        self.assertFalse(self.room_1.get_owner_name())

        rent_2 = RentFactory(
            company=self.company,
            room=self.room_1,
            date_start=yesterday,
            date_end=today
        )

        self.assertEqual(2, len(self.room_1.rentals.all()))

        self.assertEqual(rent_2, self.room_1.get_active_rental())
        self.assertFalse(self.room_1.get_upcoming_rentals())
        self.assertTrue(self.room_1.get_owner_name())

        rent_3 = RentFactory(
            company=self.company,
            room=self.room_1,
            date_start=tomorrow,
            date_end=tomorrow
        )

        self.assertEqual(3, len(self.room_1.rentals.all()))

        self.assertEqual(rent_2, self.room_1.get_active_rental())
        self.assertEqual(1, len(self.room_1.get_upcoming_rentals()))

        rent_4 = RentFactory(
            company=self.company,
            room=self.room_1,
            date_start=tomorrow,
            date_end=tomorrow
        )

        self.assertEqual(2, len(self.room_1.get_upcoming_rentals()))

        rent_5 = RentFactory(
            company=self.company,
            room=self.room_2,
            date_start=today,
            date_end=today
        )

        rent_6 = RentFactory(
            company=self.company,
            room=self.room_2,
            date_start=tomorrow,
            date_end=tomorrow
        )
        self.assertFalse(self.room_2.get_active_rental())
        self.assertFalse(self.room_2.get_upcoming_rentals())
        self.assertFalse(self.room_2.get_owner_name())
