from rest_framework.test import APITestCase
from faker import Faker
from rest_framework.views import status
from django.urls import reverse
from custom_user.models import CustomUser

fake = Faker()


class CustomUserTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_base = reverse("register")
        cls.new_user = {
            "username": fake.name(),
            "birthdate": fake.date(),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "bio": fake.paragraph(nb_sentences=5),
            "password": "1234",
            "is_critic": True,
        }

    def test_register_user(self):
        register = self.client.post(self.url_base, data=self.new_user)
        code_http = register.status_code

        register_status = status.HTTP_201_CREATED

        self.assertEqual(register_status, code_http)

    def test_return_fields(self):
        register = self.client.post(self.url_base, data=self.new_user)

        fields_return = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "birthdate",
            "bio",
            "is_critic",
            "is_superuser",
            "updated_at",
        )
        for field in fields_return:
            self.assertIn(field, register.data)


class LoginTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.url_base = reverse("login")

        cls.new_user = {
            "username": "Anthoni",
            "email": "Anthoni@mail.com",
            "birthdate": "1999-09-09",
            "first_name": "Anthoni",
            "last_name": "Felipi",
            "password": "1234",
            "is_critic": True,
        }
        cls.validation = {"username": "Anthoni", "password": "1234"}

        cls.new_user = CustomUser.objects.create_user(**cls.new_user)

    def test_login(self):
        login = self.client.post(self.url_base, data=self.validation)
        self.assertEqual(status.HTTP_200_OK, login.status_code)

#EOF