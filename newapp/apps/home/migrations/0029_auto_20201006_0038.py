# Generated by Django 3.1 on 2020-10-05 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20201006_0022'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date']},
        ),
    ]