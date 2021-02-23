from django.db import models
from ckeditor.fields import RichTextField


class Contacts(models.Model):
    contact_phone = models.CharField('Контактный телефон', max_length=25)
    contact_phone2 = models.CharField('Контактный телефон-2', max_length=25, blank=True)
    contact_mail = models.EmailField('Контактная почта', max_length=250)
    location = models.CharField('Адрес', max_length=100)
    text = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return 'Контакты'


class Company(models.Model):
    company = RichTextField('Описание компании', blank=True)
    photo = models.FileField('Фото компании', upload_to= 'about/%Y/%m/%d/')

    class Meta:
       verbose_name = 'Описание и фото компании'
       verbose_name_plural = 'Описание и фото компании'

    def __str__(self):
        return 'Описание и фотография компании'


class Production(models.Model):
    production = RichTextField('Описание производства', blank=True)
    photo = models.FileField('Фото производства', upload_to= 'about/%Y/%m/%d/')

    class Meta:
       verbose_name = 'Производство'
       verbose_name_plural = 'Производство'

    def __str__(self):
        return 'Описание и фотография производства'


class Laboratory(models.Model):
    lab = RichTextField('Описание лаборатории', blank=True)
    photo = models.FileField('Фото лаборатории', upload_to='about/%Y/%m/%d/')

    class Meta:
        verbose_name = 'Лаборатория'
        verbose_name_plural = 'Лаборатория'

    def __str__(self):
        return 'Описание лаборатории'


class Advantages(models.Model):

    title = RichTextField('Преимущество', max_length=100)
    adv = RichTextField('Описание преимущества')

    class Meta:
       verbose_name = 'Преимущество'
       verbose_name_plural = 'Преимущества'

    def __str__(self):
        return self.title


class MainPagePhoto(models.Model):
    photo = models.FileField('фото', upload_to='uploads')
    title = models.CharField('название', max_length=200)
    description = models.CharField('краткое описание для отображения на фото на главной (не обязательно)', max_length=200, blank=True)
    slogan = models.CharField('слоган для фото на главной (не обязательно)', max_length=100, blank=True)

    class Meta:
        verbose_name = 'фото и слоган для главной страницы'
        verbose_name_plural = 'фотографии и слоганы для главной страницы'

    def __str__(self):
        return self.title


class MainPageDescription(models.Model):
    title = models.CharField('название', max_length=200)
    description = RichTextField('Краткое описание компании для главной страницы')

    class Meta:
        verbose_name = 'Краткое описание компании главной страницы'
        verbose_name_plural = 'Краткие описания компании для главной страницы'

    def __str__(self):
        return self.title
