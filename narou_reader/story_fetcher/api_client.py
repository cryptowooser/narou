import requests
from datetime import datetime, timedelta

API_BASE_URL = 'https://api.syosetu.com/novelapi/api/'

def fetch_top_stories(limit=20):
    # Calculate the timestamp for 24 hours ago
    yesterday = datetime.now() - timedelta(days=1)
    timestamp = int(yesterday.timestamp())

    # Prepare the API request parameters
    params = {
        'out': 'json',  # Request JSON output
        'lim': limit,  # Number of results to return
        'order': 'dailypoint',  # Sort by daily point ranking
        'lastup': f'{timestamp}-',  # Stories updated in the last 24 hours
        'of': 'n-t-w-s-g-k-gf-dp-l',  # Fields to return
    }

    # Make the API request
    response = requests.get(API_BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # The first item in the response is always the total count, so we remove it
        return data[1:]
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None

def parse_story(story):
    return {
        'ncode': story['ncode'],
        'title': story['title'],
        'author': story['writer'],
        'synopsis': story['story'],
        'genre': story['genre'],
        'keywords': story['keyword'],
        'first_published': story['general_firstup'],
        'daily_point': story['daily_point'],
        'length': story['length']
    }

def get_top_stories(limit=20):
    stories = fetch_top_stories(limit)
    if stories:
        return [parse_story(story) for story in stories]
    return []