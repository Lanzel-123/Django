from django.shortcuts import render
from .recommender import get_recommendations

def home(request):
    recommended_titles = get_recommendations('Django for Beginners')
    
    context = {
        'base_title': 'Django for Beginners',
        'recommendations': recommended_titles
    }
    return render(request, 'home.html', context)