# Generated by Django 3.2.8 on 2021-10-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='coment',
            field=models.TextField(blank=True),
        ),
    ]
