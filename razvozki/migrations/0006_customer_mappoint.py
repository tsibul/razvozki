# Generated by Django 4.0.4 on 2022-05-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razvozki', '0005_alter_razvozka_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mappoint',
            field=models.CharField(default='', max_length=255),
        ),
    ]
