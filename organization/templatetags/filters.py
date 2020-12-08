from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='skill')
@stringfilter
def skill(string):
    string = string.replace('_', ' ')
    string = string[6:len(string)]
    string = string.title()

    return string

# register.filter('skill', skill)