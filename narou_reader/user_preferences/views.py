from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserPreferencesForm
from story_fetcher.models import Story

@login_required
def user_preferences(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserPreferencesForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user_preferences')
    else:
        form = UserPreferencesForm(instance=user_profile)
    
    hidden_stories = user_profile.hidden_stories.all()
    
    return render(request, 'user_preferences/preferences.html', {
        'form': form,
        'hidden_stories': hidden_stories
    })

@login_required
def unhide_story(request, story_id):
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)
        story = Story.objects.get(id=story_id)
        user_profile.hidden_stories.remove(story)
    return redirect('user_preferences')