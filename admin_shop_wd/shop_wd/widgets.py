from django.utils.safestring import mark_safe

from django import forms


class ImageWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None, **kwargs):
        if value:
            return mark_safe('<img src="data:image/jpeg;base64,{}" width="150" />'.format(value))
        else:
            return '-'
