# Formularze tłumaczenia strony dla panelu tłumacza.
from django import forms
from strona.models import Pageitem

fields2 = (
 'headtitle_en', 'mainpage_en', 'information_en', 'akamap_en',
 'contact_en', 'logout_en', 'news_en', 'docs_en', 'login_en',
 'panel_user_en', 'panel_council_en', 'panel_staff_en',
 'panel_translator_en', 'backtouserpanel_en', 'see_more_en',
 'pagemap_en', 'addblog_en', 'addinfo_en', 'addfile_en', 'editme_en')


# Klasa tłumaczeniowa tłumacza dla Pageitem
class PageItemForm(forms.ModelForm):

    fields2 = (
     'headtitle_en', 'mainpage_en', 'information_en', 'akamap_en',
     'contact_en', 'logout_en', 'news_en', 'docs_en', 'login_en',
     'panel_user_en', 'panel_council_en', 'panel_staff_en',
     'panel_translator_en', 'backtouserpanel_en', 'see_more_en',
     'pagemap_en', 'addblog_en', 'addinfo_en', 'addfile_en', 'editme_en')

    def __init__(self, *args, **kwargs):
        super(PageItemForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    class Meta:
        model = Pageitem
        fields = '__all__'

    def save(self, update_fields=fields2, commit=True):
        p_item = super(PageItemForm, self).save(commit=False)

        if commit:
            p_item.save(update_fields=fields2)
        return p_item
