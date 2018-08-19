from django import forms
from .models import Image
from django.core.files.base import ContentFile
from urllib import request
from django.utils.text import slugify


class ImagesCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {'url': forms.HiddenInput,
                   }

    # check poprawnosc formatu Zdjec
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_ex = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_ex:
            raise forms.ValidationError('the given url does not match valid image extensions')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImagesCreateForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title),
                                    image_url.rsplit('.', 1)[1].lower())
        # download z url dane
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)

        if commit:
            image.save()
        return image
