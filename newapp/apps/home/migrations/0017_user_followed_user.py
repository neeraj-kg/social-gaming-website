# Generated by Django 3.1 on 2020-10-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followed_user',
            field=models.IntegerField(default=0),
        ),
    ]
