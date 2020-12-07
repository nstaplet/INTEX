from django.shortcuts import render
from django.http import HttpResponse
from .models import applicant, message, offers_review
from organization.models import listing_skills, skill


# will retrieve the skills from the listings and put them into a sorted list to suggest which skills are most in demand by companies
def display_top_skills():

    recommended_skills = {}

    skills_listings = listing_skills.objects.all()

    skills_occurances = {}

    for row in skills_listings:
        if row.skill_id in skills_occurances:
            skills_occurances[row.skill_id] += 1
        else:
            skills_occurances[row.skill_id] = 0
    
    # turns the items into a sorted list based off of occurance : sort descending
    skills_occurances_sorted = sorted(skills_occurances.items(), key=lambda x: x[1], reverse=True)

    skills_names = []

    # puts those skill names into a list since we only have the id
    for i, j in skills_occurances_sorted:
        skill_row = skill.objects.all().get(skill_id=i)
        skills_names.append(skill_row.skill_name)

    # returns the skill names
    return skills_names


def get_applicant_skills(userid):
    oApplicant = applicant.objects.get(id=userid)
    list_skills = oApplicant.skills

    print(set(list_skills))

    # return set(list_skills)


