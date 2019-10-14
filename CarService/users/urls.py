from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from users import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token/obtain', obtain_jwt_token),
    path('api-token/refresh', refresh_jwt_token),
    path('api-token/verify', verify_jwt_token)
]