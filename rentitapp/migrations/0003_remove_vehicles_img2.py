# Generated by Django 3.0.7 on 2020-09-17 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentitapp', '0002_auto_20200618_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicles',
            name='img2',
        ),
    ]