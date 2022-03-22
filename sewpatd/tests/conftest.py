import pytest

from django.contrib.auth.models import User


# Fixture to create the 'pytest' test user
@pytest.fixture
def pytest_user():
    pytest_user = User.objects.create_user(username='pytest')
    pytest_user.set_password('password')
    return pytest_user
