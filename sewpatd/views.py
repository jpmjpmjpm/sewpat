from rest_framework import viewsets

from .models import SewingPattern, Drawing
from .serializers import SewingPatternSerializer, DrawingSerializer


class SewingPatternViewSet(viewsets.ModelViewSet):
    queryset = SewingPattern.objects.all()
    serializer_class = SewingPatternSerializer


class DrawingViewSet(viewsets.ModelViewSet):
    queryset = Drawing.objects.all().select_related('sewing_pattern')
    serializer_class = DrawingSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(sewing_pattern=self.kwargs.get('pattern_pk'))
        return qs
