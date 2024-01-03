from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase


CustomUser = get_user_model()


class CustomUserTests(TestCase):
    """
    The CustomUserTests class is a test case class that is used for writing tests for the CustomUser model.

    Parameters:
    - TestCase (class): TestCase is a class provided by Django for writing tests for your Django applications.

    Methods:
    - setUpTestData(cls): Set up the test data for the class.
    - test_create_user(self): A test case that verifies the creation of a user.
    - test_create_superuser(self): A test case that verifies the creation of a superuser.
    - test_create_user_empty_username(self): Test case to check if a ValueError is raised when creating a user with an empty username.
    - test_create_user_duplicate_username(self): Test case for creating a user with a duplicate username.
    - test_get_user_by_username(self): Test the functionality of retrieving a user by username.
    - test_get_user_by_email(self): Test the functionality of retrieving a user by email.
    - test_update_user_username(self): Test case to update the username of a user.
    - test_update_user_email(self): Test case to update the email of a user.
    - test_update_user_password(self): Test case to ensure that updating the password of a user is reflected in the database.
    - test_delete_user(self): Test case to ensure that deleting a user removes it from the database.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up the test data for the class.

        This class method creates a superuser and a regular user for testing purposes.
        The regular user has the username "user", email "user@email.com", and password "testpassword1234".
        The superuser has the username "superuser", email "superuser@email.com", and password "testpassword1234".

        Parameters:
        - cls: The class object.

        Returns:
        - None
        """

        # Define the data for the regular user
        user_data = {
            "username": "user",
            "email": "user@email.com",
            "password": "testpassword1234",
        }

        # Define the data for the superuser
        superuser_data = {
            "username": "superuser",
            "email": "superuser@email.com",
            "password": "testpassword1234",
        }

        # Create the regular user
        cls.user = CustomUser.objects.create_user(**user_data)

        # Create the superuser
        cls.superuser = CustomUser.objects.create_superuser(**superuser_data)

    def test_create_user(self):
        """
        A test case that verifies the creation of a user.

        This test case checks if the attributes of the user created match the expected values.
        It iterates over the expected_attributes dictionary and asserts that each attribute of the
        user matches the corresponding expected value.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """

        # Define the expected attributes of the user
        expected_values = {
            "username": "user",
            "email": "user@email.com",
            "is_active": True,
            "is_staff": False,
            "is_superuser": False,
        }

        # Verify that each attribute of the user matches the expected values
        for attr, expected_value in expected_values.items():
            self.assertEqual(getattr(self.user, attr), expected_value)

    def test_create_superuser(self):
        """
        A test case that verifies the creation of a superuser.

        This test case checks if the attributes of the superuser created match the expected values.
        It iterates over the expected_attributes dictionary and asserts that each attribute of the
        superuser matches the corresponding expected value.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """

        # Define the expected attributes of the superuser
        expected_attributes = {
            "username": "superuser",
            "email": "superuser@email.com",
            "is_active": True,
            "is_staff": True,
            "is_superuser": True,
        }

        # Verify that each attribute of the superuser matches the expected values
        for attribute, expected_value in expected_attributes.items():
            self.assertEqual(getattr(self.superuser, attribute), expected_value)

    def test_create_user_empty_username(self):
        """
        Test case to check if a ValueError is raised when creating a user with an empty username.

        This test case uses the `create_user` method of the `CustomUser` model to create a user with an empty username.
        The expected behavior is that a `ValueError` exception should be raised.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None

        Raises:
        - ValueError: If an empty username is provided.
        """

        # Assert that a `ValueError` is raised when creating a user with an empty username
        self.assertRaises(
            ValueError,
            CustomUser.objects.create_user,
            "",
            "test@email.com",
            "testpassword1234",
        )

    def test_create_user_duplicate_username(self):
        """
        Test case for creating a user with a duplicate username.

        This function tests the behavior of the `create_user` method of the `CustomUser` model when a
        user with a duplicate username is attempted to be created. The function asserts that calling
        `create_user` with the same username as an existing user raises an `IntegrityError` exception.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None

         Raises:
        - IntegrityError: If an duplicate username is provided.
        """

        # Verify that calling `create_user` with the same username as an existing user raises an `IntegrityError` exception
        self.assertRaises(
            IntegrityError,
            CustomUser.objects.create_user,
            "user",
            "test@email.com",
            "testpassword1234",
        )

    def test_get_user_by_username(self):
        """
        Test the functionality of retrieving a user by username.

        This function tests the functionality of retrieving a user object from the
        database based on their username.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """

        # Retrieve user object from the database based on username
        user = CustomUser.objects.get(username="user")

        # Verify that the user object has the expected properties
        self.assertTrue(
            user.email == "user@email.com"
            and user.is_active
            and not user.is_staff
            and not user.is_superuser
        )

    def test_get_user_by_email(self):
        """
        Test the functionality of retrieving a user by email.

        This function tests the functionality of retrieving a user object from the
        database based on their email.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """

        # Retrieve user object from the database based on email
        user = CustomUser.objects.get(email="user@email.com")

        # Verify that the user object has the expected properties
        self.assertTrue(
            user.username == "user"
            and user.is_active
            and not user.is_staff
            and not user.is_superuser
        )

    def test_update_user_username(self):
        """
        Test case to update the username of a user.

        This function tests whether the username of a user can be successfully updated and saved to the database.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """

        # Update the user's username
        new_username = "newusername"
        self.user.username = new_username
        self.user.save()

        # Retrieve the updated user from the database
        updated_user = CustomUser.objects.get(id=self.user.id)

        # Verify that the username has been successfully updated
        self.assertEqual(updated_user.username, new_username)

    def test_update_user_email(self):
        """
        Test case to update the email of a user.

        This function tests whether the email of a user can be successfully updated and saved to the database.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """

        # Update the user's email
        new_email = "newemail@example.com"
        self.user.email = new_email
        self.user.save()

        # Retrieve the updated user from the database
        updated_user = CustomUser.objects.get(id=self.user.id)

        # Verify that the email has been successfully updated
        self.assertEqual(updated_user.email, new_email)

    def test_update_user_password(self):
        """
        Test case to ensure that updating the password of a user is reflected in the database.

        This test checks if the password of a user is correctly updated and reflected in the database.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """

        # Update the user's password
        self.user.set_password("newpassword1234")
        self.user.save()

        # Retrieve the updated user from the database
        updated_user = CustomUser.objects.get(id=self.user.id)

        # Verify that the password has been successfully updated
        self.assertTrue(updated_user.check_password("newpassword1234"))

    def test_delete_user(self):
        """
        Test case to ensure that deleting a user removes it from the database.

        This test checks if the delete method correctly removes the user from the database.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """

        # Retrieve and delete the user from the database
        CustomUser.objects.filter(username="user").delete()

        # Verify that the user has been successfully deleted
        self.assertFalse(CustomUser.objects.filter(username="user").exists())
