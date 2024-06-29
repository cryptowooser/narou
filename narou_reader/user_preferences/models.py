from django.db import models
from django.contrib.auth.models import User
from story_fetcher.models import Genre, Tag, Story

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_genres = models.ManyToManyField(Genre)
    excluded_tags = models.ManyToManyField(Tag)
    excluded_stories = models.ManyToManyField(Story)

    def __str__(self):
        return f"{self.user.username}'s profile"