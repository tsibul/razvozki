# Generated by Django 4.0.4 on 2022-05-07 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('razvozki', '0006_customer_mappoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_clr',
            fields=[
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='razvozki.customer')),
                ('clr', models.CharField(default='text-dark', max_length=30)),
            ],
            bases=('razvozki.customer',),
        ),
    ]
