from django.db import models, connections

from .widgets import ImageWidget


# Create your models here.
class User(models.Model):
    tg_id = models.BigIntegerField(primary_key=True, auto_created=False)

    class Meta:
        db_table = 'users'
        managed = False
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Category(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=25)

    class Meta:
        db_table = 'categories'
        managed = False
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category')

    class Meta:
        db_table = 'subcategories'
        managed = False
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


#
class Photo(models.Model):
    id = models.AutoField(primary_key=True, db_index=True)
    photo = models.TextField()

    class Meta:
        db_table = 'photos'
        managed = False
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class Item(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    name = models.CharField(max_length=25)
    description = models.TextField(max_length=100)
    price = models.BigIntegerField()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, db_column='photo', null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, db_column='subcategory')

    class Meta:
        db_table = 'items'
        managed = False
        verbose_name = 'Итем'
        verbose_name_plural = 'Итемы'


class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, db_column='item',)

    class Meta:
        db_table = 'orders'
        managed = False
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class FAQ(models.Model):
    id = models.IntegerField(primary_key=True, db_index=True)
    question = models.CharField(max_length=100)
    answer = models.TextField(max_length=1000)

    class Meta:
        db_table = 'faqs'
        managed = False
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
