import pytest
from ..models import SewingPattern


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
