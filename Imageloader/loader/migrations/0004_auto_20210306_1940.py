# Generated by Django 3.1.7 on 2021-03-06 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0003_auto_20210306_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='file',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]