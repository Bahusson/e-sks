# Formularze obsługi strony dla panelu admina.
from django import forms
from .models import Blog, Info, Fileserve
import datetime


# Dla tworzenia i edycji aktualności.
class BlogForm(forms.ModelForm):
    title_pl = forms.CharField(max_length=200)
    title_en = forms.CharField(max_length=200)
    pubdate = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M:%S'])
    body_pl = forms.CharField(widget=forms.Textarea, required=False)
    body_en = forms.CharField(widget=forms.Textarea, required=False)
    image_pl = forms.ImageField(required=False)
    image_en = forms.ImageField(required=False)
    video_pl = forms.CharField(max_length=500, required=False)
    video_en = forms.CharField(max_length=500, required=False)

    class Meta:
        model = Blog
        fields = (
         'title_pl', 'title_en', 'pubdate', 'body_pl', 'body_en', 'image_pl',
         'image_en', 'video_pl', 'video_en',
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
        blog.image_pl = self.cleaned_data["image_pl"]
        blog.image_en = self.cleaned_data["image_en"]
        blog.video_pl = self.cleaned_data["video_pl"]
        blog.video_en = self.cleaned_data["video_en"]

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
    image_pl = forms.ImageField(required=False)
    image_en = forms.ImageField(required=False)

    class Meta:
        model = Info
        fields = (
         'title_pl', 'title_en', 'pubdate', 'body_pl', 'body_en',  'image_pl',
         'image_en',
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
        info.image_pl = self.cleaned_data["image_pl"]
        info.image_en = self.cleaned_data["image_en"]

        if commit:
            info.save()
        return info


# Dla dla tworzenia i edycji plików.
class FileserveForm(forms.ModelForm):
    title_pl = forms.CharField(max_length=200)
    title_en = forms.CharField(max_length=200)
    pubdate = forms.DateTimeField(input_formats=['%d.%m.%Y %H:%M:%S'])
    body_pl = forms.CharField(widget=forms.Textarea, required=False)
    body_en = forms.CharField(widget=forms.Textarea, required=False)
    file_pl = forms.FileField(required=False)
    file_en = forms.FileField(required=False)

    class Meta:
        model = Fileserve
        fields = (
         'title_pl', 'title_en', 'pubdate', 'body_pl', 'body_en', 'file_pl',
         'file_en',
         )

    def save(self, uid, commit=True):
        filesv = super(FileserveForm, self).save(commit=False)
        filesv.owner = uid
        filesv.lastmod = datetime.datetime.now()
        filesv.title_pl = self.cleaned_data["title_pl"]
        filesv.title_en = self.cleaned_data["title_en"]
        filesv.pubdate = self.cleaned_data["pubdate"]
        filesv.body_pl = self.cleaned_data["body_pl"]
        filesv.body_en = self.cleaned_data["body_en"]
        filesv.file_pl = self.cleaned_data["file_pl"]
        filesv.file_en = self.cleaned_data["file_en"]

        if commit:
            filesv.save()
        return filesv
