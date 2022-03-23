from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework import routers

from .views import SewingPatternViewSet

router = routers.DefaultRouter()
router.register(r'patterns', SewingPatternViewSet, basename='pattern')

app_name = 'sewpatd'
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token-auth/', views.obtain_auth_token)
]
