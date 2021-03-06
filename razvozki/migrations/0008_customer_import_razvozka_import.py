# Generated by Django 4.0.4 on 2022-05-12 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('razvozki', '0007_customer_clr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_import',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=120)),
                ('mappoint', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Razvozka_import',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date of transportation')),
                ('date_id', models.SmallIntegerField(default=0)),
                ('customer_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=120)),
                ('to_do_deliver', models.CharField(default='', max_length=255)),
                ('to_do_take', models.CharField(default='', max_length=255)),
                ('map_point', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='razvozki.customer')),
            ],
        ),
    ]
