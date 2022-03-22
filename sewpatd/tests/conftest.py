import pytest

from django.contrib.auth.models import User


# Fixture to create the 'pytest' test user
@pytest.fixture
def sewpat_user():
    sewpat_user = User.objects.create_user(username='pytest')
    sewpat_user.set_password('password')
    return sewpat_user
