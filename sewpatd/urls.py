from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework_nested import routers

from .views import SewingPatternViewSet, DrawingViewSet

router = routers.DefaultRouter()
router.register(r'patterns', SewingPatternViewSet, basename='pattern')

patterns_router = routers.NestedSimpleRouter(router, r'patterns', lookup='pattern')
patterns_router.register(r'drawings', DrawingViewSet, basename='drawing')

app_name = 'sewpatd'
urlpatterns = [
    path('', include(router.urls)),
    path('', include(patterns_router.urls)),
    path('token/', views.obtain_auth_token)
]
