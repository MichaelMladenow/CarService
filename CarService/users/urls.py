from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from users import views

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('register', views.RegisterUser.as_view(), name='register'),
    path('user', views.current_user, name='get-current-user'),

    # make sure login and logout are accessible only
    # via post requests from rest_framework
    path('', include('rest_framework.urls', namespace='rest_framework')),

    path('api-token/obtain', obtain_jwt_token, name='obtain-api-token'),
    path('api-token/refresh', refresh_jwt_token, name='refresh-api-token'),
    path('api-token/verify', verify_jwt_token, name='verify-api-token')
]
