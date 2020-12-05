from django.shortcuts import render
from django.http import HttpResponse
# from .models import skills, 


# will retrieve the skills from the listings and put them into a sorted list to suggest which skills are most in demand by companies
def display_top_skills(request):

    recommended_skills = {}

    skills_listings = skills_listings_class.objects.all()

    skills_occurances = {}

    for row in skills_listings:
        if skills_listings.skill_id in skills_occurances:
            skills_occurances[skills_listings.skill_id] += 1
        else:
            skills_occurances[skills_listings.skill_id] = 0
    
    skills_occurances_sorted = sorted(skills_occurances.items(), key=lambda x: x[1], reverse=True)

    skills_names = []

    for i, j in skills_occurances_sorted:
        skill_name = skills.objects.all().get(id=i)
        skills_names.append(skill_name)

    return skills_names