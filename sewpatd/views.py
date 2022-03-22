from rest_framework import viewsets

from .serializers import SewingPatternSerializer
from .models import SewingPattern


class SewingPatternViewSet(viewsets.ModelViewSet):
    queryset = SewingPattern.objects.all()
    serializer_class = SewingPatternSerializer
