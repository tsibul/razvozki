# Generated by Django 4.0.4 on 2022-04-25 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razvozki', '0003_remove_razvozka_to_do_razvozka_to_do_deliver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='razvozka',
            name='date_id',
            field=models.SmallIntegerField(default=0),
        ),
    ]
