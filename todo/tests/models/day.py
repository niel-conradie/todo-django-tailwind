from django.test import TestCase

from todo.models import DayModel


class DayModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create DayModel data for testing
        cls.monday = DayModel.objects.create(
            title="monday",
            slug="monday",
        )
        cls.tuesday = DayModel.objects.create(
            title="tuesday",
            slug="tuesday",
        )
        cls.wednesday = DayModel.objects.create(
            title="wednesday",
            slug="wednesday",
        )
        cls.thursday = DayModel.objects.create(
            title="thursday",
            slug="thursday",
        )
        cls.friday = DayModel.objects.create(
            title="friday",
            slug="friday",
        )
        cls.saturday = DayModel.objects.create(
            title="saturday",
            slug="saturday",
        )
        cls.sunday = DayModel.objects.create(
            title="sunday",
            slug="sunday",
        )

    def test_create_day(self):
        self.assertEqual(self.monday.title, "monday")
        self.assertEqual(self.monday.slug, "monday")

        self.assertEqual(self.tuesday.title, "tuesday")
        self.assertEqual(self.tuesday.slug, "tuesday")

        self.assertEqual(self.wednesday.title, "wednesday")
        self.assertEqual(self.wednesday.slug, "wednesday")

        self.assertEqual(self.thursday.title, "thursday")
        self.assertEqual(self.thursday.slug, "thursday")

        self.assertEqual(self.friday.title, "friday")
        self.assertEqual(self.friday.slug, "friday")

        self.assertEqual(self.saturday.title, "saturday")
        self.assertEqual(self.saturday.slug, "saturday")

        self.assertEqual(self.sunday.title, "sunday")
        self.assertEqual(self.sunday.slug, "sunday")
