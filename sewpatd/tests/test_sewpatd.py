import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from ..models import SewingPattern
from ..views import SewingPatternViewSet


# Helper for sewing pattern creation - without db save
def create_sp(name):
    return SewingPattern(name=name, description='A dress from Jeanne Lanvin, circa 1955')


# Sewing pattern creation without save
@pytest.mark.django_db
def test_sewing_pattern_create():
    sp_name = 'lanvin-dress-1955'
    sp = create_sp(sp_name)
    assert sp_name in str(sp)


# Sewing pattern creation with save
@pytest.mark.django_db
def test_sewing_pattern_create_save():
    sp_name = 'lanvin-dress-1955'
    sp = create_sp(sp_name)
    sp.save()
    assert sp_name in str(sp)


# Sewing pattern creation and retrieval from APIs
@pytest.mark.django_db
def test_sewing_pattern_create_api_retrieval(sewpat_user):
    sp_name = 'lanvin-dress-1955'
    sp = create_sp(sp_name)
    sp.save()

    factory = APIRequestFactory()
    request = factory.get(reverse('sewpatd:pattern-list'), format='json')
    force_authenticate(request, user=sewpat_user)
    view = SewingPatternViewSet.as_view({'get': 'list'})
    response = view(request)

    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]['name'] == sp_name
