from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import SewingPatternViewSet

router = routers.DefaultRouter()
router.register(r'patterns', SewingPatternViewSet, basename='pattern')

app_name = 'sewpatd'
urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.obtain_auth_token)
]
