from django.urls import path
from . import views

urlpatterns = [
    path('top/', views.top_stories, name='top_stories'),
]