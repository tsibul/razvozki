# Generated by Django 4.0.4 on 2022-04-24 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razvozki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='razvozka',
            name='date',
            field=models.DateField(verbose_name='date of transportation'),
        ),
    ]
