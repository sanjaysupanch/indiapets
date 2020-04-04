from django import template
register=template.Library()

@register.filter
def add(arg1,arg2):
    #print(str(arg1) + str(arg2))
    return str(arg1) + str(arg2)
