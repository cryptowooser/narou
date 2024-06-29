from django.core.management.base import BaseCommand
from django.utils import timezone
from story_fetcher.models import Story, Genre, Tag, DailyRanking
from story_fetcher.api_client import get_top_stories
from datetime import datetime
from django.utils.timezone import make_aware
from django.conf import settings
from zoneinfo import ZoneInfo

class Command(BaseCommand):
    help = 'Fetches top stories from Narou API and stores them in the database'

    def handle(self, *args, **options):
        self.stdout.write('Fetching top stories from Narou API...')
        stories = get_top_stories(limit=100)  # Adjust the limit as needed

        for story_data in stories:
            genre, _ = Genre.objects.get_or_create(
                code=story_data['genre'],
                defaults={'name': story_data['genre']}  # You might want to map genre codes to names
            )

            story, created = Story.objects.update_or_create(
                ncode=story_data['ncode'],
                defaults={
                    'title': story_data['title'],
                    'author': story_data['author'],
                    'synopsis': story_data['synopsis'],
                    'genre': genre,
                    'keywords': story_data['keywords'],
                    'first_published': make_aware(
                        datetime.strptime(story_data['first_published'], '%Y-%m-%d %H:%M:%S'),
                        timezone=ZoneInfo(settings.TIME_ZONE)
                    ),
                    'last_updated': timezone.now(),
                    'total_characters': story_data['length']
                }
            )

            # Handle tags
            tags = [tag.strip() for tag in story_data['keywords'].split(',')]
            for tag_name in tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                story.tags.add(tag)

            # Create or update daily ranking
            DailyRanking.objects.update_or_create(
                story=story,
                date=timezone.now().date(),
                defaults={
                    'daily_point': story_data['daily_point'],
                    'rank': stories.index(story_data) + 1  # Rank based on position in the list
                }
            )

            if created:
                self.stdout.write(f'Created new story: {story.title}')
            else:
                self.stdout.write(f'Updated story: {story.title}')

        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored top stories'))