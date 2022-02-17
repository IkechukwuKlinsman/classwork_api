from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title= 'Classwork',
        default_version='v1',
        description="""
        THIS IS A CLASSWORK
        """,
        terms_of_service='',
        contact= openapi.Contact(email= 'ikechukwuklinsman@gmail.com'),
        license= openapi.License(name='MIT License')
    ),
    public= True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/account',include('account.urls')),
    path('v1/',include('blog.urls')),
    path('',schema_view.with_ui('swagger',cache_timeout=0),
    name='schema-swagger-ui')]