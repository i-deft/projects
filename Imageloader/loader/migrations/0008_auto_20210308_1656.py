# Generated by Django 3.1.7 on 2021-03-08 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loader', '0007_auto_20210308_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadimage',
            old_name='image',
            new_name='file',
        ),
    ]