# Generated by Django 3.1.5 on 2021-02-11 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_auto_20210211_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpagephoto',
            name='description',
            field=models.CharField(blank=True, max_length=200, verbose_name='подпись или слоган для фото, на сайте, если требуется'),
        ),
        migrations.AlterField(
            model_name='mainpagephoto',
            name='photo',
            field=models.FileField(upload_to='about/%Y/%m/%d/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='mainpagephoto',
            name='title',
            field=models.CharField(max_length=200, verbose_name='название'),
        ),
    ]