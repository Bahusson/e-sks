from django import template

register = template.Library()

# Wyszukuje po liście -1
@register.filter(name='action')
def action(d,key):
    return d[key-1]

# Wyszukuje po liście
@register.filter(name='lookup')
def lookup(d,key):
    return d[key]