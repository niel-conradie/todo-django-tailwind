from django.test import TestCase

from todo.models import DayModel


class DayModelTests(TestCase):
    """
    The DayModelTests class is a test case class that is used for writing tests for the DayModel model.

    Parameters:
    - TestCase (class): TestCase is a class provided by Django for writing tests for your Django applications.

    Methods:
    - setUpTestData(cls): Set up the test data for the class.
    - test_create_day(self): Test the creation of the days of the week.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data for the class.

        This class method is responsible for creating DayModel data for testing purposes.
        It creates instances of the DayModel class with different titles and slugs representing each day of the week.

        Parameters:
        - cls: The class object.

        Returns:
        - None
        """

        # Create DayModel instances for each day of the week
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
        """
        Test the creation of the days of the week.

        This function asserts that the titles and slugs of each day of the week
        are correctly set after their creation.

        Parameters:
        - self: The instance of the test class.

        Returns:
            None
        """

        # Assert that the title and slug of each day of the week are correctly set
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
