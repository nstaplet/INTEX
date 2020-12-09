from django.shortcuts import render
from django.http import HttpResponse
from .models import message, offers_review, applicant_skills
from person.models import applicant
from organization.models import listing_skills, skill


# will retrieve the skills from the listings and put them into a sorted list to suggest which skills are most in demand by companies
def display_top_skills(request):
    try:
        if request.session['topskills']:
            print('Go')
    except Exception:
        request.session['topskills'] = None
    
    if not request.session['topskills']:
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
        try:
            for i, j in skills_occurances_sorted:
                print(i, j)
                skill_row = skill.objects.all().get(skill_id=j)
                skills_names.append(skill_row.skill_name)
        except Exception:
            for i, j in skills_occurances_sorted:
                skills_names.append(i)

        # returns the skill names
        
        request.session['topskills'] = skills_names

        return skills_names
    else:
        return request.session['topskills']


def get_applicant_skills(userid):
    oApplicant = applicant.objects.get(applicant_id=userid)
    print(userid)
    print(oApplicant.applicant_id)

    list_skills = applicant_skills.objects.all().filter(applicant_id=oApplicant.applicant_id)
    list_skills_ = []

    for skill_obj in list_skills:
        skill_name_ = skill.objects.all().get(skill_id=skill_obj.skill_id)
        list_skills_.append(skill_name_.skill_name)

    return list_skills_

    # return set(list_skills)


def recommend_listings(organization, listing):
    import urllib.request
    import json 


    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["organization_id", "id"],
                        "Values": [ [organization, listing], ]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/50d1b4f10dc9438fb84cc79ea8615275/services/cc206f6d21ff4d9890b6e33363d184a4/execute?api-version=2.0&details=true'
    api_key = '6KBCycFC/bQXVHOM6Ae+RgOQJy6K3gnGO/dj8uKclPh3JkJR+D7VJmOcSjF0bxkGtNU+3U6CItnoiNlnqpA06w==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers) 

    response = urllib.request.urlopen(req)

    result = response.read()
    result = json.loads(result)

    itemsResults = result['Results']['output1']['value']['Values'][0]

    # for i in range(len(itemsResults)):
    #     print(f'Applicant #{i + 1}: {itemsResults[i]}')

    return itemsResults 