from django import template

register = template.Library()

@register.filter(name='cut_own')
def cut_own(value, arg):
    return value.replace(arg, 'asd')

