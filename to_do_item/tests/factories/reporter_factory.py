import factory
from django.conf import settings
from factory.django import DjangoModelFactory
from django.contrib.auth.hashers import make_password


class ReporterFactory(DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    username = factory.Faker("email")
    password = factory.LazyFunction(lambda: make_password("1"))
    is_staff = True
    is_superuser = True
