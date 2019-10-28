# Formularze tłumaczenia strony dla panelu tłumacza.
from django import forms
from strona.models import Pageitem


# Klasa tłumaczeniowa tłumacza dla Pageitem
class PageItemForm(forms.ModelForm):

    # Sprawia, że wszystkie elementy (tutaj) nie są wymagane.
    def __init__(self):
        for field in self.fields.values():
            field.required = False

    class Meta:
        model = Pageitem
        fields = ('__all__')

    def save(self, commit=True):
        p_item = super(PageItemForm, self).save(commit=False)

        if commit:
            p_item.save()
        return p_item
