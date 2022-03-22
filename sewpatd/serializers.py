#  Copyright (c) 2020. Jean-Pierre Merx All rights reserved.

from rest_framework import serializers

from .models import SewingPattern


# Sewing patterns header serializer
class SewingPatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = SewingPattern
        fields = '__all__'
