from django.contrib import admin
from django.urls import include, path
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from users_api.views import RegisterView, LoginView, LogoutView, UserProfileView
from bikes_rent_api.views import ListBikeView, RentStartView, RentEndView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/users/register', RegisterView.as_view(), name='register'),
    path('api/users/login', LoginView.as_view(), name='login'),
    path('api/users/logout', LogoutView.as_view(), name='logout'),
    path('api/users/profile', UserProfileView.as_view(), name='profile'), # history include
    path('api/bikes/list', ListBikeView.as_view(), name='bikes'),
    path('api/bikes/rent_start', RentStartView.as_view(), name='rent_start'),
    path('api/bikes/rent_end', RentEndView.as_view(), name='rent_end'),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
