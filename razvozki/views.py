# Create your views here.

import datetime
from django.http import HttpResponse, HttpResponseRedirect
from .models import Razvozka, Customer
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse


def index(request):
    navi = 'razvozka'
    datenew = datetime.date.today() + datetime.timedelta(days=1)
#    date = datetime.date.today()
    razv = Razvozka.objects.order_by('-date', 'date_id')
    f_rzv = {}
    for r in razv:
        if r.date not in f_rzv:
            f_rzv[r.date] = []
        f_rzv[r.date].append(r)
    context = {'f_rzv': f_rzv, 'datenew': datenew, 'navi': navi}
    return render(request, 'razvozki/index.html', context)


#def detail(request, razvozka_id):
#    try:
#        razvozka = Razvozka.objects.get(pk=razvozka_id)
#   except Razvozka.DoesNotExist:
#        raise Http404("Razvozka does not exist")
#    return render(request, 'razvozki/detail.html', {'razvozka': razvozka})


#def date_detail(request, razvozka_date):
#    try:
#        razvozka_d = Razvozka.objects.filter(date=razvozka_date)
#    except Razvozka.DoesNotExist:
#        raise Http404("Razvozka does not exist")
#    return render(request, 'razvozki/date_detail.html', {'razvozka_date': razvozka_d})


#def results(request, razvozka_date):
#    response = "Развозка на %s."
#    return HttpResponse(response % razvozka_date)


def add_razv(request, id):
    navi = 'razvozka'
    rzv = Razvozka.objects.get(id=id)
    date_out = rzv.date
    razv = Razvozka.objects.order_by('-date', 'date_id')
    f_rzv = {}
    for r in razv:
        if r.date not in f_rzv:
            f_rzv[r.date] = []
        f_rzv[r.date].append(r)
    context = {'f_rzv': f_rzv, 'date_out': date_out, 'navi': navi}
    return render(request, 'razvozki/add_razv.html', context)


def addrecord_razv(request):
    date = request.POST['date']
    date = datetime.datetime.strptime(date, '%B %d, %Y').strftime('%Y-%m-%d')
    date_id = request.POST['date_id']
    customer_name = request.POST['customer_name']
    address = request.POST['address']
    contact = request.POST['contact']
    to_do_take = request.POST['to_do_take']
    to_do_deliver = request.POST['to_do_deliver']
    razvozka = Razvozka(date=date, date_id=date_id, customer_name=customer_name, customer=None, address=address, contact=contact,
                        to_do_take=to_do_take, to_do_deliver=to_do_deliver)
    razvozka.save()
    return HttpResponseRedirect(reverse('razvozki:index'))

def delete_rzv(request, id):
    razvozka = Razvozka.objects.get(id=id)
    razvozka.delete()
    return HttpResponseRedirect(reverse('razvozki:index'))

def update_rzv(request, id):
    navi = 'razvozka'
    rzv = Razvozka.objects.get(id=id)
    template = loader.get_template('razvozki/update_rzv.html')
    razv = Razvozka.objects.order_by('-date', 'date_id')
    f_rzv = {}
    for r in razv:
        if r.date not in f_rzv:
            f_rzv[r.date] = []
        f_rzv[r.date].append(r)
    context = {'f_rzv': f_rzv, 'rzv': rzv, 'id': id, 'navi': navi}
    return HttpResponse(template.render(context, request))

def updaterecord_rzv(request, id):
    date = request.POST['date']
    date = datetime.datetime.strptime(date, '%d.%m.%Y').strftime('%Y-%m-%d')
    date_id = request.POST['date_id']
    customer_name = request.POST['customer_name']
    address = request.POST['address']
    contact = request.POST['contact']
    to_do_take = request.POST['to_do_take']
    to_do_deliver = request.POST['to_do_deliver']
    razvozka = Razvozka.objects.get(id=id)
    razvozka.date = date
    razvozka.date_id = date_id
    razvozka.customer_name = customer_name
    razvozka.address = address
    razvozka.contact = contact
    razvozka.to_do_take = to_do_take
    razvozka.to_do_deliver = to_do_deliver
    razvozka.save()
    return HttpResponseRedirect(reverse('razvozki:index'))


def main_rzv(request):
    template = loader.get_template('razvozki/main.html')
    return HttpResponse(template.render({}, request))

def newdate_rzv(request):
    datenew = request.POST['date']
    datenew = datetime.datetime.strptime(datenew, '%d.%m.%Y').strftime('%Y-%m-%d')
    razvozka = Razvozka(date=datenew, date_id=1, customer_name='', customer=None, address='', contact='',
                        to_do_take='', to_do_deliver='')
    razvozka.save()
    return HttpResponseRedirect(reverse('razvozki:index'))

def customers(request):
    navi = 'customers'
    cust = Customer.objects.order_by('name')
    class Customer_clr:
        def __init__(self, id, name, address, contact, mappoint, clr):
            self.id = id
            self.name = name
            self.address = address
            self.contact = contact
            self.mappoint = mappoint
            self.clr = clr

    i = 0
    cust_clr = []
    for cst1 in cust:
        cust_clr.append(Customer_clr(cst1.id, cst1.name, cst1.address, cst1.contact, cst1.mappoint, 'text-dark'))
        for cst2 in cust:
            if (cst1.name == cst2.name or cst1.address == cst2.address) and cst1.id != cst2.id:
                cust_clr[i].clr = 'text-danger'
        i = i + 1
    context = {'cust': cust_clr, 'navi': navi }
    return render(request, 'razvozki/customers.html', context)

def delete_cst(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return HttpResponseRedirect(reverse('razvozki:customers'))

def add_cst(request):
    navi = 'customers'
    cust = Customer.objects.order_by('name')
    context = {'cust': cust, 'navi': navi}
    return render(request, 'razvozki/add_cst.html', context)

def updaterecord_cst(request, id):
    name = request.POST['cst_name']
    address = request.POST['address']
    contact = request.POST['contact']
    mappoint = request.POST['mappoint']
    customer = Customer.objects.get(id=id)
    customer.name = name
    customer.address = address
    customer.contact = contact
    customer.mappoint = mappoint
    customer.save()
    return HttpResponseRedirect(reverse('razvozki:customers'))


def addrecord_cst(request):
    name = request.POST['name']
    address = request.POST['address']
    contact = request.POST['contact']
    mappoint = request.POST['mappoint']
    customer = Customer(name=name, address=address, contact=contact, mappoint=mappoint)
    customer.save()
    return HttpResponseRedirect(reverse('razvozki:customers'))

