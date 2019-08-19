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

    # Funkcji używaj jeśli chcesz używać zmiennych skórek.
    # Defaultuje do 0 jeśli nie wybierzesz żadnej.
    def page_dress(self, **kwargs):
        c = 0
        s = kwargs['skins']
        if 'choice' in kwargs:
            c = int(kwargs['choice'])
        self.skins = list(s.objects.all())
        self.skin = self.skins[c]
        self.skinctx = {'skin': self.skin, }
        return self.skinctx

    # Funkcja tworzy za nas podstwwowy kontekst,
    # który rozszerza się o dany w funkcji.
    def lazy_context(self, **kwargs):
        self.context = {
         'items': self.items,
         'langs': self.langs, }
        if 'skins' in kwargs:
            self.page_dress(**kwargs)
            self.context.update(self.skinctx)
        if 'context' in kwargs:
            self.context.update(kwargs['context'])
        return self.context


# Klasa ładowania widoków /strony/
class PageElement(object):
    def __init__(self, *args, **kwargs):
        self.x = args[0]
        self.listed = list(self.x.objects.all())
        self.elements = self.x.objects

    def list_specific(self, num):
        self.listed_specific = self.listed[num]
        return self.listed_specific

    def by_id(self, **kwargs):
        G404 = kwargs['G404']
        x_id = kwargs['id']
        self.one_by_id = G404(self.x, pk=x_id)
        return self.one_by_id


'''
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
'''
