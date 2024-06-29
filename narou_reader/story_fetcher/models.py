from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Story(models.Model):
    ncode = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    synopsis = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    keywords = models.TextField()
    first_published = models.DateTimeField()
    last_updated = models.DateTimeField()
    total_characters = models.IntegerField()

    def __str__(self):
        return self.title

class DailyRanking(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    date = models.DateField()
    daily_point = models.IntegerField()
    rank = models.IntegerField()

    class Meta:
        unique_together = ('story', 'date')

    def __str__(self):
        return f"{self.story.title} - {self.date} - Rank: {self.rank}"