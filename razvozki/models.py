import datetime
from django.utils import timezone
from django.db import models



class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=120)
    mappoint = models.CharField(max_length=255, default='')

    def __repr__(self):
        return f"Customer(name={self.name!r}, contact={self.contact!r})"

    def __str__(self):
        return self.name


class Customer_clr(Customer):
    clr = models.CharField(max_length=30, default='text-dark')

    def __repr__(self):
        return f"Customer_clr(name={self.name!r}, contact={self.contact!r})"

    def __str__(self):
        return self.name


class Razvozka(models.Model):
    date = models.DateField('date of transportation')
    date_id = models.SmallIntegerField(default=0)
    customer = models.ForeignKey(Customer, models.SET_NULL, null=True, blank=True)
    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=120)
    to_do_deliver = models.CharField(max_length=255, default='')
    to_do_take = models.CharField(max_length=255, default='')
    map_point = models.CharField(max_length=255)

    def __str__(self):
        return str(self.date) + '| ' + str(self.customer_name) + '| ' + str(self.to_do_deliver)+ '| ' + str(self.to_do_take)

    def __repr__(self):
        return f"razvozka_list(date={self.date!r}, customer={self.customer_name!r}, deliver={self.to_do_deliver!r}, " \
               f"take={self.to_do_take!r}) "

    def get_all_todo(self):
        to_do_take = ''
        to_do_deliver = ''
        if self.to_do_take is not '':
            to_do_take = ' ЗАБРАТЬ: ' + str(self.to_do_take)
        if self.to_do_deliver is not '':
            to_do_deliver = ' СДАТЬ: ' + str(self.to_do_deliver)
        return f"{to_do_take} {to_do_deliver}"

#    def was_published_recently(self):
#        return self.date >= timezone.now() - 24.04.2022.timedelta(days=5)
