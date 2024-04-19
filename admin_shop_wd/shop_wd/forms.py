from django import forms

from .models import Photo
import base64

from .widgets import ImageWidget


class PhotoAdminForm(forms.ModelForm):
    new_photo = forms.ImageField(required=False,
                                 widget=forms.FileInput(attrs={'onchange': 'displayCurrentImage(this);'}))
    current_photo = forms.CharField(widget=ImageWidget(), required=False)

    class Meta:
        model = Photo
        exclude = ['photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and instance.photo:
            self.fields['current_photo'].initial = instance.photo

    def clean_new_photo(self):
        new_photo = self.cleaned_data.get('new_photo', None)
        if new_photo:
            try:
                # Читаем содержимое загруженного файла и кодируем его в формат base64
                with new_photo.open('rb') as f:
                    binary_data = f.read()
                    base64_data = base64.b64encode(binary_data).decode('utf-8')
                return base64_data
            except Exception as e:
                raise forms.ValidationError("Ошибка при кодировании файла в base64: {}".format(e))
        return None

    def save(self, commit=True):
        # Обновляем поле photo только если загружено новое фото
        if self.cleaned_data.get('new_photo', None):
            self.instance.photo = self.cleaned_data['new_photo']
        return super().save(commit)


class MessageForm(forms.Form):
    tg_ids = forms.CharField(widget=forms.HiddenInput())
    message = forms.CharField(widget=forms.Textarea)
