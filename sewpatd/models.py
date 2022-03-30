from django.db import models
from django.utils.translation import gettext_lazy as _

NAME_LENGTH = 60
DESCRIPTION_LENGTH = 300
GEOMETRY_LENGTH = 100000


class SewingPattern(models.Model):
    name = models.CharField(max_length=NAME_LENGTH, blank=False, unique=True,
                            verbose_name=_('Name'), db_index=True,
                            help_text=_('Unique name (maximum %(length)s characters)') % {'length': NAME_LENGTH})
    # TODO: look at transforming the name to a slug

    description = models.CharField(max_length=DESCRIPTION_LENGTH, blank=True,
                                   verbose_name=_('Description'),
                                   help_text=_('Description (maximum %(length)s characters)') % {
                                       'length': DESCRIPTION_LENGTH})

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Drawing(models.Model):
    name = models.CharField(max_length=NAME_LENGTH, blank=False,
                            verbose_name=_('Name'), db_index=True,
                            help_text=_('Unique name (maximum %(length)s characters)') % {'length': NAME_LENGTH})

    description = models.CharField(max_length=DESCRIPTION_LENGTH, blank=True,
                                   verbose_name=_('Description'),
                                   help_text=_('Description (maximum %(length)s characters)') % {
                                       'length': DESCRIPTION_LENGTH})

    sewing_pattern = models.ForeignKey(SewingPattern, on_delete=models.CASCADE, related_name='drawings',
                                       verbose_name=_('Link to pattern'))

    points = models.JSONField(max_length=GEOMETRY_LENGTH, blank=True, null=True, verbose_name=_('Points'),
                              help_text=_('Points in custom JSON format (maximum %(length)s bytes)') % {
                                  'length': GEOMETRY_LENGTH})

    segments = models.JSONField(max_length=GEOMETRY_LENGTH, blank=True, null=True, verbose_name=_('Segments'),
                                help_text=_('Segments in custom JSON format (maximum %(length)s bytes)') % {
                                    'length': GEOMETRY_LENGTH})

    curves = models.JSONField(max_length=GEOMETRY_LENGTH, blank=True, null=True, verbose_name=_('Curves'),
                              help_text=_('Curves in custom JSON format (maximum %(length)s bytes)') % {
                                  'length': GEOMETRY_LENGTH})

    class Meta:
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(fields=['sewing_pattern', 'name'], name=_('Unique name per sewing pattern'))]

    def __str__(self):
        return self.name
