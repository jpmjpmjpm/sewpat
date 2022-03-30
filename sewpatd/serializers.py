#  Copyright (c) 2020. Jean-Pierre Merx All rights reserved.


from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import SewingPattern, Drawing


# Sewing patterns header serializer
class SewingPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = SewingPattern
        fields = '__all__'


class DrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        fields = ['id', 'name', 'description', 'points', 'segments', 'curves']

    def create(self, data):
        sewing_pattern = SewingPattern.objects.get(pk=self.context["view"].kwargs["pattern_pk"])
        data['sewing_pattern'] = sewing_pattern
        try:
            obj = super().create(data)
        except IntegrityError as e:
            raise ValidationError(repr(e))
        return obj
