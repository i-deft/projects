from django.db import models
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField


class Division(models.Model):
    name = models.CharField('Название направления', max_length=100)
    photo = models.FileField(upload_to='products/%Y/%m/%d/')
    description = RichTextField('Описание направления', max_length=800, blank=True)
    slug = models.SlugField(max_length=70, verbose_name='задать уникальный URL латинскими буквами, между словами дефис')

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.name


class Reagent(models.Model):
    title = models.ForeignKey('Division', on_delete=models.CASCADE, verbose_name='Выбрать направление')
    name = models.CharField('Название реагента', max_length=100)
    text = RichTextField('Описание реагента')
    main_photo = models.FileField('Фото для превью', upload_to='products/%Y/%m/%d/')
    short_description = RichTextField('Краткое описание для превью', max_length=600)
    slug = models.SlugField(max_length=70, verbose_name='задать уникальный URL латинскими буквами, между словами дефис')

    class Meta:
        verbose_name = 'Реагент'
        verbose_name_plural = 'Реагенты'

    def __str__(self):
        return self.name


class ReagentsFile(models.Model):
    title = models.ForeignKey('Reagent', on_delete=models.CASCADE, verbose_name='Выбрать реагент')
    description = models.CharField('краткое описание к фото, не обязательно', max_length=200, blank=True)
    photo_name = models.CharField('название фото, не обязательно', max_length=30, blank=True)
    photo = models.FileField('фото', upload_to='products/%Y/%m/%d/', blank=True)
    video = EmbedVideoField('Видео с ютуба', blank=True)

    class Meta:
        verbose_name = 'Медифайл для реагента'
        verbose_name_plural = 'Медиафайлы для реагента'

    def __str__(self):
        return f'Медиафайлы к реагенту {self.title}'







