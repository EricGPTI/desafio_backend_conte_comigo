from django.contrib import admin
from django.db import router
from django.urls import path
from django.urls.conf import include
from rest_framework.authtoken import views as authtoken_views
from api.urls import router

from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Calculator API",
        default_version='v1',
        description="Calculator API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ericgpti@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', authtoken_views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
]

# swagger_urls
urlpatterns += [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
