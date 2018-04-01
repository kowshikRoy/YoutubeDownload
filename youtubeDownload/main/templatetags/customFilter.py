from django import template

register = template.Library()

@register.filter(name = 'toMB')
def toMB(value):
    return round(value / 1024. / 1024 , 1)



@register.filter(name = 'height')
def height(value):
    return value.split('x')[1]
