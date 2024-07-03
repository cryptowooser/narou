from django.urls import path
from . import views

urlpatterns = [
    path('preferences/', views.user_preferences, name='user_preferences'),
    path('unhide_story/<int:story_id>/', views.unhide_story, name='unhide_story'),
]