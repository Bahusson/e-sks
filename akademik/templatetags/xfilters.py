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


# Wyszukuje po słowniku
@register.filter(name='lookupdict')
def lookupdict(d, key):
    return d.__getattribute__(key)

# Wyszukuje po liście bezwzględny integer
@register.filter(name='lookupint')
def lookupint(d, key):
    return d[int(key)]


# Wyszukuje po liście bezwzględny integer
@register.filter(name='actionint')
def actionint(d, key):
    return d[int(key)-1]


# Zwraca wartość do filtrowania malejąco
@register.filter(name='negator')
def negator(var):
    neg = '-' + str(var)
    return neg

# Cztery poniżej do wywalenie jak poprawię menu na lepszą logikę.
# Podnosi wartość samego siebie o 1 za każdym razem. (Dla Linków)
@register.filter(name='setlinkadder')
def setlinkadder(var):
    global linkaddpoint
    linkaddpoint = 0
    return var[linkaddpoint]


# Podnosi wartość samego siebie o 1 za każdym razem. (Dla Linków)
@register.filter(name='linkadder')
def linkadder(var):
    global linkaddpoint
    linkaddpoint += 1
    return var[linkaddpoint]


# Podnosi wartość samego siebie o 1 za każdym razem. (Dla Menu)
@register.filter(name='setmenuadder')
def setmenuadder(var):
    global menuaddpoint
    menuaddpoint = 0
    return var[menuaddpoint]


# Podnosi wartość samego siebie o 1 za każdym razem. (Dla Menu)
@register.filter(name='menuadder')
def menuadder(var):
    global menuaddpoint
    menuaddpoint += 1
    return var[menuaddpoint]


# Podnosi wartość samego siebie o 1 za każdym razem. (Dla Menu)
@register.filter(name='zip_lists')
def zip_lists(a, b):
    return zip(a, b)
