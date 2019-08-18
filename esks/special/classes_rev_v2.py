from django.shortcuts import render

class PageLoad(object):
    ''' Zwraca tyle języków ile mamy zainstalowane
    w ustawieniach w zakładce LANGUAGES w formacie naprzemiennym
    pasującym do wzornika z dwoma wyjściowymi
    (ID_Języka, Ścieżka_Flagi_Języka), oraz
    Ładuje wszystkie podstawowe elementy w widoku strony. '''

    def __init__(self, *args):
        lang_id = []
        langsl = []
        a = args[0]
        b = args[1]
        self.langs = []
        locations = list(a.objects.all())
        self.items = locations[0]
        for item in b:
            lang_id.append("lang_flag_" + str(item[0]))

        x = len(lang_id)-1
        y = 0

        while x+1 > 0:
            z = self.items.__dict__[lang_id[y]]
            langsl.append(z)
            x = x-1
            y = y+1

        self.langs = zip(lang_id, langsl)

# Klasa ładowania widoków /strony/
class PageElement(object):
    def init(self, *args, **kwargs)
        x = args[0]
        self.listed = list(x.objects.all())
        self.elements = x.objects
        if 'list_specific' in kwargs:
            n = kwargs['list_specific']
            self.listed_specific = self.listed[n]
            
class PageElementById(PageElement):
    def init(self, *args, **kwargs)
        super().__init__(*args, **kwargs)
        G404 = kwargs['G404']
        x_id = kwargs['id']
        self.by_id = G404(x, pk=x_id)        
 

# Subklasa pozwająca na dowolne zmienianie skórek przez Usera
# Spośród dostępnych w adminie.
class PageSkinner(PageLoad):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        s = kwargs['skins']
        c = int(kwargs['choice'])
        self.skins = list(s.objects.all())
        self.skin = self.skins[c]
        self.context = {
         'items': self.items,
         'langs': self.langs,
         'skin': self.skin, }
    
        if 'context' in kwargs:
            self.context.update(kwargs['context'])
      