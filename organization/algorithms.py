from django.shortcuts import render
from django.http import HttpResponse
from .models import message, offers_review, applicant_skills
from person.models import applicant
from organization.models import listing_skills, skill


def recommend_users(request):
    import urllib
    import json 

    organization = request.user.id
    applicant_id = request.GET['applicant']

    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["reviewerID", "asin"],
                        "Values": [ [ organization, applicant_id ] ]
                    },        },
                "GlobalParameters": {
    }
        }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/50d1b4f10dc9438fb84cc79ea8615275/services/73f271457c254f05a7e5847109142643/execute?api-version=2.0&details=true'
    api_key = 'RyYXyS4mvm8WFrI0kAAGpV6fA18sSkUgmhHZYzwnoaWm7pjbzoMBy+T0jFU6wevbJHCfxPZXB27nDWKqmajg6g==' # Replace this with the API key for the web service
    headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

    req = urllib.request.Request(url, body, headers) 

    response = urllib.request.urlopen(req)

    result = response.read()
    result = json.loads(result)

    itemsResults = result['Results']['output1']['value']['Values'][0]

    for i in range(len(itemsResults)):
        print(f'Applicant #{i + 1}: {itemsResults[i]}')

    return itemsResults