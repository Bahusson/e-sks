# Formularze tłumaczenia strony dla panelu tłumacza.
from django import forms
from strona.models import Pageitem


# Klasa tłumaczeniowa tłumacza dla Pageitem
class PageItemForm(forms.ModelForm):

    # Tymczasowy fix do czasu jak zrobię tę metaklasę na poważnie tak, żeby
    # brała te argumenty w locie albo zrobię obejście.
    # Na razie, ponieważ nadpisuje co nie trzeba to takie obejście z hardkodem.
    class Meta:
        model = Pageitem
        fields = (
         'headtitle_en', 'mainpage_en', 'information_en', 'akamap_en',
         'contact_en', 'logout_en', 'news_en', 'docs_en', 'login_en',
         'panel_user_en', 'panel_council_en', 'panel_staff_en',
         'panel_translator_en', 'backtouserpanel_en', 'see_more_en',
         'pagemap_en', 'addblog_en', 'addinfo_en', 'addfile_en', 'editme_en')

    # Sprawia, że wszystkie elementy (tutaj) nie są wymagane.
    def __init__(self, *args, **kwargs):
        super(PageItemForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    def save(self, commit=True):
        p_item = super(PageItemForm, self).save(commit=False)
    #    for field in self.fields:
        #    field_value = self.cleaned_data[field]
            #if field_value is not None:
                #p_item.__getattr__(field) = field_value
# https://stackoverflow.com/questions/1355150/django-when-saving-how-can-you-check-if-a-field-has-changed
        if commit:
            p_item.save()
        return p_item
