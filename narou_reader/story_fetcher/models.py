from django.db import models

GENRE_CHOICES = {
    0: '未選択〔未選択〕',
    101: '異世界〔恋愛〕',
    102: '現実世界〔恋愛〕',
    201: 'ハイファンタジー〔ファンタジー〕',
    202: 'ローファンタジー〔ファンタジー〕',
    301: '純文学〔文芸〕',
    302: 'ヒューマンドラマ〔文芸〕',
    303: '歴史〔文芸〕',
    304: '推理〔文芸〕',
    305: 'ホラー〔文芸〕',
    306: 'アクション〔文芸〕',
    307: 'コメディー〔文芸〕',
    401: 'VRゲーム〔SF〕',
    402: '宇宙〔SF〕',
    403: '空想科学〔SF〕',
    404: 'パニック〔SF〕',
    9901: '童話〔その他〕',
    9902: '詩〔その他〕',
    9903: 'エッセイ〔その他〕',
    9904: 'リプレイ〔その他〕',
    9999: 'その他〔その他〕',
    9801: 'ノンジャンル〔ノンジャンル〕',
}

class Genre(models.Model):
    code = models.IntegerField(unique=True, choices=[(k, v) for k, v in GENRE_CHOICES.items()])
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = GENRE_CHOICES.get(self.code, 'Unknown')
        super().save(*args, **kwargs)

        
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