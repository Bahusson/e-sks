from django import template

register = template.Library()


# Wyszukuje po liście -1
@register.filter(name='action')
def action(d, key):
    return d[key-1]


# Wyszukuje po liście
@register.filter(name='lookup')
def lookup(d, key):
    return d[key]


# Wyszukuje po liście bezwzględny integer
@register.filter(name='lookupint')
def lookupint(d, key):
    return d[int(key)]


@register.filter(name='intvar')
def intvar(l, var):
    attribute = getattr(var, 1)
    integerated = int(attribute)
    return integerated
