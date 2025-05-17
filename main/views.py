from django.shortcuts import render
from .recommender import get_recommendations
from django.contrib.auth.decorators import login_required

def home(request):
    recommended_titles = get_recommendations('Django for Beginners')
    
    context = {
        'base_title': 'Django for Beginners',
        'recommendations': recommended_titles
    }
    return render(request, 'main/home.html')

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

