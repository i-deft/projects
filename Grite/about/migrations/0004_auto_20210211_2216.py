# Generated by Django 3.1.5 on 2021-02-11 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20210202_0006'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainPagePhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='about/%Y/%m/%d/')),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'фото и слоган для главной страницы',
                'verbose_name_plural': 'фотографии и слоганы для главной страницы',
            },
        ),
        migrations.DeleteModel(
            name='Callback',
        ),
        migrations.AlterField(
            model_name='advantages',
            name='adv',
            field=models.TextField(max_length=400, verbose_name='Описание преимущества'),
        ),
    ]
