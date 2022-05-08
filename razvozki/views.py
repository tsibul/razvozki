# Create your views here.

import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Razvozka, Customer, Customer_clr
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.views.generic import ListView

class Razvozka_clr:
    def __init__(self, id, date, date_id, customer, customer_name, address, contact, to_do_take, to_do_deliver,
                 clr):
        self.id = id
        self.date = date
        self.date_id = date_id
        self.customer = customer
        self.customer_name = customer_name
        self.address = address
        self.contact = contact
        self.to_do_take = to_do_take
        self.to_do_deliver = to_do_deliver
        self.clr = clr

    def get_all_todo_clr(self):
        to_do_take = ''
        to_do_deliver = ''
        if self.to_do_take is not '':
            to_do_take = ' ЗАБРАТЬ: ' + str(self.to_do_take)
        if self.to_do_deliver is not '':
            to_do_deliver = ' СДАТЬ: ' + str(self.to_do_deliver)
        return f"{to_do_take} {to_do_deliver}"


#class Customer_clr:
#    def __init__(self, id, name, address, contact, mappoint, clr):
#        self.id = id
#        self.name = name
#        self.address = address
#        self.contact = contact
#        self.mappoint = mappoint
#        self.clr = clr


def index(request):
    navi = 'razvozka'
    datenew = datetime.date.today() + datetime.timedelta(days=1)
    #    date = datetime.date.today()
    rzv = Razvozka.objects.order_by('-date', 'date_id')
    cust = Customer.objects.order_by('name')
    rzv_clr = []
    for rzv1 in rzv:
        if rzv1.customer is None:
            rzv_clr.append(
                Razvozka_clr(rzv1.id, rzv1.date, rzv1.date_id, rzv1.customer, rzv1.customer_name, rzv1.address,
                             rzv1.contact, rzv1.to_do_take, rzv1.to_do_deliver, 'text-dark'))
        else:
            rzv_clr.append(
                Razvozka_clr(rzv1.id, rzv1.date, rzv1.date_id, rzv1.customer, rzv1.customer_name, rzv1.address,
                             rzv1.contact, rzv1.to_do_take, rzv1.to_do_deliver, 'text-success'))

    f_rzv0 = {}
    for r in rzv_clr:
        if r.date not in f_rzv0:
            f_rzv0[r.date] = []
        f_rzv0[r.date].append(r)

    f_rzv2 = list(f_rzv0.items())
    paginator = Paginator(f_rzv2, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    f_rzv = dict(page_obj.object_list)

    date_range = []
    for i in range(page_obj.paginator.num_pages):
        page_obj2 = paginator.get_page(i + 1)
        date_tmp = datetime.datetime.strptime(str(page_obj2.object_list[0][0]),'%Y-%m-%d').strftime('%d.%m.%Y')
        date_range.append([i + 1, 'до ' + date_tmp])

    context = {'f_rzv': f_rzv, 'datenew': datenew, 'navi': navi, 'cust': cust, 'page_obj': page_obj, 'date_range': date_range}
    return render(request, 'razvozki/index.html', context)


def addrecord_razv(request):
    date = request.POST['date']
    date = datetime.datetime.strptime(date, '%B %d, %Y').strftime('%Y-%m-%d')
    date_id = request.POST['date_id']
    customer = request.POST['customer']
    if customer == 'None':
        customer = None
    else:
        customer = Customer.objects.get(id=customer)
    customer_name = request.POST['customer_name']
    address = request.POST['address']
    contact = request.POST['contact']
    to_do_take = request.POST['to_do_take']
    to_do_deliver = request.POST['to_do_deliver']
    razvozka = Razvozka(date=date, date_id=date_id, customer_name=customer_name, customer=customer, address=address,
                        contact=contact,
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
    razvozka = Razvozka.objects.get(id=id)
    date = request.POST['date']
    date = datetime.datetime.strptime(date, '%d.%m.%Y').strftime('%Y-%m-%d')
    date_id = request.POST['date_id']
    address = request.POST['address']
    contact = request.POST['contact']
    to_do_take = request.POST['to_do_take']
    to_do_deliver = request.POST['to_do_deliver']
    razvozka.date = date
    razvozka.date_id = date_id
    if razvozka.customer is None:
        customer_name = request.POST['customer_name']
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
    cust = Customer_clr.objects.order_by('name')

#    cust_clr = []
    for cst1 in cust:
#        cst01 = Customer_clr(name=cst1.name, address=cst1.address, contact=cst1.contact,
#                             mappoint=cst1.mappoint, clr='text-secondary')
        cst1.clr = 'text-secondary'
        for cst2 in cust:
            cst1_name = cst1.name.replace(' ', '')
            cst1_name = cst1_name.replace('-', '')
            cst1_name = cst1_name.replace('.', '')
            cst1_name = cst1_name.replace(',', '')

            cst2_name = cst2.name.replace(' ', '')
            cst2_name = cst2_name.replace('-', '')
            cst2_name = cst2_name.replace('.', '')
            cst2_name = cst2_name.replace(',', '')

            cst1_address = cst1.address.replace(' ', '')
            cst1_address = cst1_address.replace('-', '')
            cst1_address = cst1_address.replace('.', '')
            cst1_address = cst1_address.replace(',', '')

            cst2_address = cst2.address.replace(' ', '')
            cst2_address = cst2_address.replace('-', '')
            cst2_address = cst2_address.replace('.', '')
            cst2_address = cst2_address.replace(',', '')

            if (cst1_name == cst2_name or cst1_address == cst2_address) and cst1.id != cst2.id:
                cst1.clr = 'text-danger'
        cst1.save()
#        cust_clr.append(cst01)

    paginator = Paginator(cust, 20)  # Show 20.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'navi': navi, 'page_obj': page_obj}
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
    customer_clr = Customer_clr(name=name, address=address, contact=contact, mappoint=mappoint, clr='text-secondary')
    customer_clr.save()
    return HttpResponseRedirect(reverse('razvozki:customers'))


def print(request, date_r):
    razvozka = []
    for rzv in Razvozka.objects.filter(date=date_r):
        razvozka.append(rzv)
    date_r = datetime.datetime.strptime(date_r, '%Y-%m-%d').strftime('%d.%m.%Y')
    context = {'date_r': date_r, 'razv': razvozka}
    return render(request, 'razvozki/print.html', context)