from django.db import models
from django.utils.translation import gettext_lazy as _


class SewingPattern(models.Model):
    NAME_LENGTH = 60
    name = models.CharField(max_length=NAME_LENGTH, blank=False, unique=True,
                            verbose_name=_('Name'), db_index=True,
                            help_text=_(f'Unique name (maximum {NAME_LENGTH} characters)'))
    # TODO: look at transforming the name to a slug

    DESCRIPTION_LENGTH = 300
    description = models.CharField(max_length=DESCRIPTION_LENGTH, blank=True,
                                   verbose_name=_('Description'),
                                   help_text=_(f'Description (maximum {DESCRIPTION_LENGTH} characters)'))

    DRAWING_LENGTH = 100000
    drawing = models.JSONField(max_length=DRAWING_LENGTH, blank=True, null=True, verbose_name=_('drawing'),
                               help_text=_('JSON representation of the drawing'))

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
