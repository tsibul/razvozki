# Generated by Django 4.0.4 on 2022-04-29 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('razvozki', '0004_razvozka_date_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='razvozka',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='razvozki.customer'),
        ),
    ]
