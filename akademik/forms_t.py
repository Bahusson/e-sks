# Formularze tłumaczenia strony dla panelu tłumacza.
from django import forms
from strona.models import Pageitem
from .models import TranslatorMenuItem


# Klasa tłumaczeniowa tłumacza dla elementów szeregowych (Pageitem)
class PageItemForm(forms.ModelForm):

    def __init__(self, *args, upd_fields=0, **kwargs):
        super(PageItemForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
        self.upda_fields = upd_fields

    class Meta:
        model = Pageitem
        fields = '__all__'

    def save(self, commit=True):
        p_item = super(PageItemForm, self).save(commit=False)

        if commit:
            p_item.save(update_fields=self.upda_fields)
        return p_item


# Klasa tłumaczeniowa tłumacza dla listy rozwijanej ()
class TMIListForm(forms.ModelForm):

    def __init__(self, *args, upd_fields=0, **kwargs):
        super(TMIListForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
        self.upda_fields = upd_fields

    class Meta:
        model = TranslatorMenuItem
        fields = '__all__'

    def save(self, commit=True):
        p_item = super(TMIListForm, self).save(commit=False)

        if commit:
            p_item.save(update_fields=self.upda_fields)
        return p_item
