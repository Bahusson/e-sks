# Formularze obsługi strony dla panelu admina.
from django import forms
from .models import Blog, Info, FileServe
import datetime


# Dla tworzenia i edycji aktualności.
class BlogForm(forms.ModelForm):
    title_pl = forms.CharField(max_length=200)
    title_en = forms.CharField(max_length=200)
    pubdate = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M:%S'])
    body_pl = forms.CharField(widget=forms.Textarea, required=False)
    body_en = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(upload_to='images', required=False)
    video = forms.CharField(max_length=500, required=False)

    class Meta:
        model = Blog
        fields = (
         'title_pl', 'title_en', 'pubdate', 'body_pl', 'body_en', 'image',
         'video',
         )

    def save(self, uid, commit=True):
        blog = super(BlogForm, self).save(commit=False)
        blog.owner = uid
        blog.lastmod = datetime.datetime.now()
        blog.title_pl = self.cleaned_data["title_pl"]
        blog.title_en = self.cleaned_data["title_en"]
        blog.pubdate = self.cleaned_data["pubdate"]
        blog.body_pl = self.cleaned_data["body_pl"]
        blog.body_en = self.cleaned_data["body_en"]
        blog.image = self.cleaned_data["image"]
        blog.video = self.cleaned_data["video"]

        if commit:
            blog.save()
        return blog


# Dla dla tworzenia i edycji informacji.
class InfoForm(forms.ModelForm):
    title_pl = forms.CharField(max_length=200)
    title_en = forms.CharField(max_length=200)
    pubdate = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M:%S'])
    body_pl = forms.CharField(widget=forms.Textarea, required=False)
    body_en = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(upload_to='images', required=False)

    class Meta:
        model = Blog
        fields = (
         'title_pl', 'title_en', 'pubdate', 'body_pl', 'body_en', 'image',
         )

    def save(self, uid, commit=True):
        info = super(InfoForm, self).save(commit=False)
        info.owner = uid
        info.lastmod = datetime.datetime.now()
        info.title_pl = self.cleaned_data["title_pl"]
        info.title_en = self.cleaned_data["title_en"]
        info.pubdate = self.cleaned_data["pubdate"]
        info.body_pl = self.cleaned_data["body_pl"]
        info.body_en = self.cleaned_data["body_en"]
        info.image = self.cleaned_data["image"]

        if commit:
            info.save()
        return info


# Dla dla tworzenia i edycji plików.
class FileServeForm(forms.ModelForm):
    title_pl = forms.CharField(max_length=200)
    title_en = forms.CharField(max_length=200)
    pubdate = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M:%S'])
    body_pl = forms.CharField(widget=forms.Textarea, required=False)
    body_en = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(upload_to='images', required=False)

    class Meta:
        model = FileServe
        fields = (
         'title_pl', 'title_en', 'pubdate', 'body_pl', 'body_en', 'image',
         )

    def save(self, uid, commit=True):
        filesv = super(FileServeForm, self).save(commit=False)
        filesv.owner = uid
        filesv.lastmod = datetime.datetime.now()
        filesv.title_pl = self.cleaned_data["title_pl"]
        filesv.title_en = self.cleaned_data["title_en"]
        filesv.pubdate = self.cleaned_data["pubdate"]
        filesv.body_pl = self.cleaned_data["body_pl"]
        filesv.body_en = self.cleaned_data["body_en"]
        filesv.image = self.cleaned_data["image"]

        if commit:
            filesv.save()
        return filesv
