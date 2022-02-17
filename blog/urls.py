from django.urls import path
from . import views


urlpatterns = [
    path("blog/", views.blogs),
    # path("blog/get_blog/", views.get_blog),

    
]