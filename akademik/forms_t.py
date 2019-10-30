# Formularze tłumaczenia strony dla panelu tłumacza.
from django import forms
from strona.models import Pageitem


# Klasa tłumaczeniowa tłumacza dla Pageitem
class PageItemForm(forms.ModelForm):

    class Meta:
        model = Pageitem
        fields = '__all__'

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

        if commit:
            p_item.save()
        return p_item
