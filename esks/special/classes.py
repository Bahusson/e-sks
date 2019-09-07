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
        self.listed = list(self.x.objects.all())  # Lista obiektów
        self.elements = self.x.objects  # Obiekty
        self.baseattrs = self.listed[0]  # Pierwsze obiekty na liście

    # Konkretnte obiekty na liście (nie pierwsze).
    def list_specific(self, num):
        self.listed_specific = self.listed[num]
        return self.listed_specific

    # Działa tylko jeśli wszystkie atrybuty są tłumaczone.
    # Zwraca gołe nazwy atrybutów bez względu na ilość języków.
    def get_attrnames(self, langs):
        preqlist = list(self.baseattrs.__dict__.keys())
        preqlist2 = preqlist[2:]  # Obetnij czołówkę.
        self.attrnames = preqlist2[0::len(langs)+1]
        return self.attrnames

    # Zwraca pojedynczy przetłumaczony obiekt.
    def get_setter(self, place, quarter, langs):
        attrnames = self.get_attrnames(langs)
        attrobjects = self.list_specific(place)
        self.setter = attrobjects.__getattribute__(attrnames[int(quarter)-1])
        return self.setter

    # Zwraca listę przetłumaczonych atrybutów
    def get_setlist(self, place, langs):
        attrnames = self.get_attrnames(langs)
        attrobjects = self.list_specific(place)
        self.setlist = []
        for item in attrnames:
            self.setlist.append(attrobjects.__getattribute__(item))
        return self.setlist

    # Elementy po Id.
    def by_id(self, **kwargs):
        G404 = kwargs['G404']
        x_id = kwargs['id']
        self.one_by_id = G404(self.x, pk=x_id)
        return self.one_by_id


class PortalLoad(PageLoad):
    def __init__(self, *args):
        super().__init__(*args)
        d = args[2]
        place = args[3]
        menus = args[4]
        links = args[5]
        loc_d = list(d.objects.all())
        self.portal = loc_d[place]
        self.menu = list(menus.objects.all())
        self.link = list(links.objects.all())

    def page_dress(self, **kwargs):
        super().page_dress(**kwargs)

    def lazy_context(self, **kwargs):
        self.context = {
         'items': self.items,
         'langs': self.langs,
         'portals': self.portal,
         'menu': self.menu,
         'link': self.link, }
        if 'skins' in kwargs:
            self.page_dress(**kwargs)
            self.context.update(self.skinctx)
        if 'context' in kwargs:
            self.context.update(kwargs['context'])
        return self.context


class PartyMaster(object):
    # Podstawka zwraca wszystkie akcje kwaterunkowe
    def __init__(self, *args):
        H_Party = args[0]
        py_tz = args[1]
        dt = args[2]
        self.all_parties = PageElement(H_Party)
        tz_UTC = py_tz.timezone('Europe/Warsaw')
        self.dt_now = dt.datetime.now(tz_UTC)
        self.list_parties = self.all_parties.listed

    # Zwraca wszystkie akcje bez względu na czas serwera (atrybuty)
    def full_party(self, **kwargs):
        full_parties = []
        attrname = kwargs['attrname']
        x = 0
        for item in self.list_parties:
            full_parties.append(
             str(self.list_parties[x].__dict__[attrname]))
            x = x+1
        return full_parties

    # Zwraca tylko aktywne akcje względem czasu serwera (atrybuty)
    def active_party(self, **kwargs):
        active_parties = []
        attrname = kwargs['attrname']
        x = 0
        for item in self.list_parties:
            if self.list_parties[x].__dict__['date_start'] <= self.dt_now <= self.list_parties[x].__dict__['date_end']:
                active_parties.append(
                 str(self.list_parties[x].__dict__[attrname]))
            x = x+1
        return active_parties

    # Tylko nieaktywne akcje względem czasu serwera (atrybuty)
    def past_party(self, **kwargs):
        inactive_parties = []
        attrname = kwargs['attrname']
        x = 0
        for item in self.list_parties:
            if self.list_parties[x].__dict__['date_end'] < self.dt_now:
                inactive_parties.append(
                 str(self.list_parties[x].__dict__[attrname]))
            x = x+1
        return inactive_parties

    # Tylko zaplanowane akcje względem czasu serwera (atrybuty)
    def future_party(self, **kwargs):
        future_parties = []
        attrname = kwargs['attrname']
        x = 0
        for item in self.list_parties:
            if self.list_parties[x].__dict__['date_start'] > self.dt_now:
                future_parties.append(
                 str(self.list_parties[x].__dict__[attrname]))
            x = x+1
        return future_parties
