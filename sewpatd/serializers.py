#  Copyright (c) 2020. Jean-Pierre Merx All rights reserved.

from rest_framework import serializers

from .models import SewingPattern, Drawing


# Sewing patterns header serializer
class SewingPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = SewingPattern
        fields = '__all__'


class DrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        fields = ['id', 'name', 'description', 'image']

    def create(self, data):
        sewing_pattern = SewingPattern.objects.get(pk=self.context["view"].kwargs["pattern_pk"])
        data['sewing_pattern'] = sewing_pattern
        obj = super().create(data)
        return obj
