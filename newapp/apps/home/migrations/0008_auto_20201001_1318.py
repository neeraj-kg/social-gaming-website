# Generated by Django 3.1 on 2020-10-01 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20201001_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(default='', upload_to='home/images'),
        ),
    ]
