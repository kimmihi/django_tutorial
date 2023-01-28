from django.urls import path
from . import views


app_name = "articles"

urlpatterns = [
    path('', views.article_list_or_create, name="article_list_or_create"),
]