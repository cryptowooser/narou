from django.shortcuts import render
from .api_client import get_top_stories
from django.utils import timezone
from .models import Story, DailyRanking
def top_stories(request):
    stories = get_top_stories()
    return render(request, 'story_fetcher/top_stories.html', {'stories': stories})

def home(request):
    today = timezone.now().date()
    top_stories = DailyRanking.objects.filter(date=today).order_by('rank')[:20]  # Get top 20 stories
    context = {
        'top_stories': top_stories,
    }
    return render(request, 'story_fetcher/home.html', context)