# Generated by Django 2.1.5 on 2019-02-19 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190219_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='textfile',
            name='file_name',
            field=models.CharField(default='NA', max_length=200),
        ),
    ]
