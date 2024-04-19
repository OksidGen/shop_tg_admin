from django.contrib import admin
from django.shortcuts import render

from .forms import PhotoAdminForm, MessageForm
from .models import Category, Subcategory, Photo, Item, User, Order, FAQ
from .widgets import ImageWidget


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('tg_id',)
    search_fields = ('tg_id',)
    readonly_fields = ('tg_id',)

    actions = ['send_message']

    def send_message(self, request, queryset):
        # Получаем список выбранных tg_id
        selected_tg_ids = list(queryset.values_list('tg_id', flat=True))

        # Заполнение формы и передача значения выбранных tg_id
        form = MessageForm(initial={'tg_ids': ','.join(map(str, selected_tg_ids))})

        # Отображение формы для ввода сообщения и выбранных tg_id
        context = {
            'form': form,
            'title': "Отправить сообщение",
            'selected_tg_ids': selected_tg_ids,
        }
        return render(request, 'admin/send_message_form.html', context)

    send_message.short_description = "Отправить сообщение"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    readonly_fields = ('id',)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    search_fields = ('id', 'name', 'category')
    readonly_fields = ('id',)


class PhotoAdmin(admin.ModelAdmin):
    form = PhotoAdminForm
    list_display = ('id', 'photo_display')
    readonly_fields = ('id',)
    search_fields = ('id',)

    def photo_display(self, obj):
        return ImageWidget().render('photo', obj.photo)

    photo_display.short_description = 'Photo Preview'

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        photo = self.get_object(request, object_id)
        if photo and photo.photo:
            extra_context['current_photo'] = photo.photo
        return super().change_view(request, object_id, form_url, extra_context=extra_context)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('id', 'name', 'price')
    readonly_fields = ('id',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item')
    search_fields = ('id', 'user', 'item')
    readonly_fields = ('id', 'user', 'item')


class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')
    search_fields = ('id', 'question', 'answer')
    readonly_fields = ('id',)


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(FAQ, FAQAdmin)
