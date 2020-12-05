from django.shortcuts import render
from django.http import HttpResponse
# from .models import 

def recommend_skills(request):

    recommended_skills = {}

    context = {
        'rec_skills': recommended_skills
    }

    return HttpResponse('Recommend skills function')