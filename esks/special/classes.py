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


# Subklasa aktualności.
class Blog(PageLoad):
    def __init__(self, *args, **kwargs):
        if args:
            super().__init__(*args)

    def gen(self, **kwargs):
        b = kwargs['B']
        self.bloglist = list(b.objects.all())
        self.blogs = b.objects

        if 'blogid' in kwargs:
            G404 = kwargs['G404']
            blog_id = kwargs['blogid']
            self.blog = G404(b, pk=blog_id)


# Subklasa informacji.
class Info(PageLoad):
    def __init__(self, *args, **kwargs):
        if args:
            super().__init__(*args)

    def gen(self, **kwargs):
        inf = kwargs['In']
        self.infos = inf.objects

        if 'infoid' in kwargs:
            G404 = kwargs['G404']
            info_id = kwargs['infoid']
            self.info = G404(inf, pk=info_id)


# Subklasa pliku strony głównej.
class File(PageLoad):
    def __init__(self, *args, **kwargs):
        if args:
            super().__init__(*args)

    def gen(self, **kwargs):
        fil = kwargs['F']
        self.files = fil.objects

        if 'fileid' in kwargs:
            G404 = kwargs['G404']
            file_id = kwargs['fileid']
            self.file = G404(fil, pk=file_id)
