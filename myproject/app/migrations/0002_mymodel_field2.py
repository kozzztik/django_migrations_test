# Generated by Django 4.0.4 on 2022-05-17 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='field2',
            field=models.CharField(default='1', max_length=255),
        ),
    ]