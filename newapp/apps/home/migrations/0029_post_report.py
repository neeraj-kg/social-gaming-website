# Generated by Django 3.1 on 2020-10-06 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_merge_20201006_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='report',
            field=models.ManyToManyField(related_name='who_reported', to='home.User'),
        ),
    ]