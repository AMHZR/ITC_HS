__author__ = 'aamir'
from django import template

register = template.Library()


@register.filter
def to_list(request, key):
    return request.getlist(key,[])

@register.filter
def previous_page(value):
    if value > 1:
        return int(value)-1
    return 1

@register.filter
def next_page(value):
    if value > 1:
        return int(value)+1
    return 1
