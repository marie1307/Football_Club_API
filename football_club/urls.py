
from django.contrib import admin
from django.urls import path, include, re_path
from teams.views import LoginAPIView, LogoutAPIView
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Football Club API",
      default_version='v1',
      description="Information about Club, footballers, matches and etc. Also personal page for each footballer getting informations about their results",
   ),
   public=True,
   permission_classes=[AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('teams.urls')),
    path('api/login/', LoginAPIView.as_view(), name = 'login'),
    path('api/logout/', LogoutAPIView.as_view(), name='logout'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
