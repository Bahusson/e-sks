class Langmenu(object):
    ''' Zwraca tyle języków ile mamy zainstalowane
    w ustawieniach w zakładce LANGUAGES w formacie naprzemiennym
    pasującym do wzornika z dwoma wyjściowymi
    (ID_Języka, Ścieżka_Flagi_Języka) '''
    def __init__(self,a,b):
        lang_id = []
        langsl = []
        self.langslist = []
        locations = list(a.objects.all())
        self.items1 = locations[0]
        for item in b :
            lang_id.append("lang_flag_" + str(item[0]))

        x = len(lang_id) -1
        y = 0

        while x+1 > 0 :
            z = self.items1.__dict__[lang_id[y]]
            langsl.append(z)
            x = x-1
            y = y+1

        self.langslist = zip(lang_id, langsl)

    def flag(self):
        return self.items1

    def list(self):
        return self.langslist

class PageLoad(object):
    ''' Ładuje wszystkie podstawowe elementy w widoku strony
    Ogólnie rzecz biorąc oszczędza kod'''

    def __init__(self,P,L,F,I,B,G404,info_id,blog_id):
        self.items = Langmenu(P,L).flag
        self.langs = Langmenu(P,L).list
        self.files = F.objects
        self.infos = I.objects
        self.blogs = B.objects

        if info_id == None:
            pass
        else:
            self.info = G404(I, pk=info_id)

        if blog_id == None:
            pass
        else:
            self.blog = G404(B, pk=blog_id)

    def items(self):
        return self.items

    def langs(self):
        return self.langs

    def files(self):
        return self.files

    def infos(self):
        return self.infos

    def info(self):
        return self.info

    def blogs(self):
        return self.blogs

    def blog(self):
        return self.blog
