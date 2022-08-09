import datetime
from django.utils import timezone
from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    mappoint = models.CharField(max_length=255, default='', help_text="Yandex mappoint")
    subcontractor = models.BooleanField(default=False, help_text='True if subcontractor')

    def __repr__(self):
        return f"Customer(name={self.name!r}, contact={self.contact!r})"

    def __str__(self):
        return self.name


class Customer_clr(Customer):
    clr = models.CharField(max_length=30, default='text-secondary')

    def __repr__(self):
        return f"Customer_clr(name={self.name!r}, contact={self.contact!r})"

    def __str__(self):
        return self.name


class Razvozka(models.Model):
    date = models.DateField(help_text='date of transportation')
    date_id = models.SmallIntegerField(default=0, help_text='order inside date')
    customer = models.ForeignKey(Customer, models.SET_NULL, null=True, blank=True, help_text='customer base if exist')
    customer_name = models.CharField(max_length=100, help_text='customer as text could differ from db')
    address = models.CharField(max_length=255, help_text='real address')
    contact = models.CharField(max_length=255, help_text='real contacts')
    to_do_deliver = models.CharField(max_length=255, help_text='things for delivery')
    to_do_take = models.CharField(max_length=255, help_text='things to take from')
    map_point = models.CharField(max_length=255, help_text='Yandex mappoint')
    clr = models.CharField(max_length=30, default='', help_text='text color')
    fulfilled = models.BooleanField(default=False, help_text='True is fulfilled')
    deliver_to = models.BooleanField(default=False, help_text='transportation to processing')
    return_from = models.BooleanField(default=False, help_text='return products from processing')
    return_all = models.BooleanField(default=False, help_text='False if some part was not return')
    return_goods = models.ForeignKey('self', models.SET_NULL, null=True, blank=True,
                                     help_text='from which delivery return')


    def __str__(self):
        return str(self.date) + '| ' + str(self.customer_name) + '| ' + str(self.to_do_deliver)+ '| ' + str(self.to_do_take)

    def __repr__(self):
        return f"razvozka_list(date={self.date!r}, customer={self.customer_name!r}, deliver={self.to_do_deliver!r}, " \
               f"take={self.to_do_take!r}) "

    def get_all_todo(self):
        to_do_take = ''
        to_do_deliver = ''
        if self.to_do_take != '':
            to_do_take = ' ЗАБРАТЬ: ' + str(self.to_do_take)
        if self.to_do_deliver != '':
            to_do_deliver = ' СДАТЬ: ' + str(self.to_do_deliver)
        return f"{to_do_take} {to_do_deliver}"


class Razvozka_import (models.Model):
    date = models.DateField('date of transportation')
    date_id = models.SmallIntegerField(default=1)
    customer = models.ForeignKey(Customer_clr, models.SET_NULL, null=True, blank=True)
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    to_do_deliver = models.CharField(max_length=255, default='')
    to_do_take = models.CharField(max_length=255, default='')
    map_point = models.CharField(max_length=255)
    clr = models.CharField(max_length=30, default='')
    fulfilled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date) + '| ' + str(self.customer_name) + '| ' + str(self.to_do_deliver)+ '| ' + str(self.to_do_take)

    def __repr__(self):
        return f"razvozka_list(date={self.date!r}, customer={self.customer_name!r}, deliver={self.to_do_deliver!r}, " \
               f"take={self.to_do_take!r}) "


class Razvozka_plan (models.Model):
    status = models.BooleanField(default=True, help_text='True if active False if moved to Razvozki')
    date_create = models.DateField(null=True, blank=True, help_text='date when created')
    date_until = models.DateField(null=True, blank=True, help_text='latest date for transportation')
    customer = models.ForeignKey(Customer_clr, models.SET_NULL, null=True, blank=True)
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    to_do_deliver = models.CharField(max_length=255, default='')
    to_do_take = models.CharField(max_length=255, default='')
    map_point = models.CharField(max_length=255)
    deliver_to = models.BooleanField(default=False, help_text='transportation to processing')
    return_from = models.BooleanField(default=False, help_text='return products from processing')
    return_goods = models.ForeignKey('self', models.SET_NULL, null=True, blank=True,
                                     help_text='from which delivery return')

    def __repr__(self):
        return f"razvozka_list(customer={self.customer_name!r}, deliver={self.to_do_deliver!r}, take={self.to_do_take!r}) "


    def get_all_todo(self):
        to_do_take = ''
        to_do_deliver = ''
        if self.to_do_take != '':
            to_do_take = ' ЗАБРАТЬ: ' + str(self.to_do_take)
        if self.to_do_deliver != '':
            to_do_deliver = ' СДАТЬ: ' + str(self.to_do_deliver)
        return f"{to_do_take} {to_do_deliver}"
