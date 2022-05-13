# Create your views here.

import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Razvozka, Customer, Customer_clr, Razvozka_import
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.core.files import File
from django.views.generic import ListView
import csv


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
        if self.to_do_take != '':
            to_do_take = ' ЗАБРАТЬ: ' + str(self.to_do_take)
        if self.to_do_deliver != '':
            to_do_deliver = ' СДАТЬ: ' + str(self.to_do_deliver)
        return f"{to_do_take} {to_do_deliver}"


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
        try:
            date_tmp = datetime.datetime.strptime(str(page_obj2.object_list[0][0]), '%Y-%m-%d').strftime('%d.%m.%Y')
            date_range.append([i + 1, 'до ' + date_tmp])
        except:
            date_range.append(['нет данных'])

    context = {'f_rzv': f_rzv, 'datenew': datenew, 'navi': navi, 'cust': cust, 'page_obj': page_obj,
               'date_range': date_range}
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
        cst1.clr = 'text-secondary'
        if find_dubl_cst(cst1, cust):
            cst1.clr = 'text-danger'
        cst1.save()

    paginator = Paginator(cust, 30)  # Show 30.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'navi': navi, 'page_obj': page_obj}
    return render(request, 'razvozki/customers.html', context)


def customers_clr(request):
    cust = Customer.objects.order_by('name')
    razv = Razvozka.objects.order_by('-date')
    # add customers to Customer_clr if not exist
    for cst in cust:
        try:
            tmp = Customer_clr.objects.get(id=cst.id)
        except Customer_clr.DoesNotExist:
            tmp = None
        if tmp is None:
            cst_clr = cst.Customer_clr(id=cst.id, name=cst.name, address=cst.address, contact=cst.contact,
                                       mappoint=cst.mappoint, clr='text-secondary')
            cst_clr.save()
    ## end of adding Customer_clr

    # return Customer names if dissapeared
    for cst in cust:
        if cst.name == '':
            rr2 = Razvozka.objects.filter(customer_id=cst.id).first()
            if rr2 is not None:
                cst.name = rr2.customer_name
                cst.address = rr2.address
                cst.contact = rr2.contact
                #                cst.mappoint = rr2.mappoint
                cst.save()
    ## end of returning customers
    # collect customers from razvozki
    for rzv in razv:
        if rzv.customer is None and find_dubl_cst(rzv.customer, cust):
            new_customer = Customer_clr(name=rzv.customer_name, address=rzv.address,
                                        contact=rzv.contact, clr='text-secondary')
            new_customer.save()
            rzv.customer = new_customer
            rzv.save()
    return HttpResponseRedirect(reverse('razvozki:customers'))


def find_dubl_cst(cst1, cust):
    result = False
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

        if ((cst1_name == cst2_name or cst1_address == cst2_address or cst1.mappoint == cst2.mappoint
             and cst1.mappoint != '') and cst1.id != cst2.id):
            result = True
    return result

def find_dubl_cst_id(cst1, cust):
    result = ''
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

        if ((cst1_name == cst2_name or cst1_address == cst2_address or cst1.mappoint == cst2.mappoint
             and cst1.mappoint != '') and cst1.id != cst2.id):
            result = cst2.id
    return result


def delete_cst(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return HttpResponseRedirect(reverse('razvozki:customers'))


def add_cst(request):
    navi = 'customers'
    cust = Customer.objects.order_by('name')
    context = {'cust': cust, 'navi': navi}
    return render(request, 'razvozki/add_cst.html', context)


def updaterecord_cst(request, from_where):
    name = request.POST['cst_name']
    address = request.POST['address']
    contact = request.POST['contact']
    mappoint = request.POST['mappoint']
    id = request.POST['cst_id']
    customer = Customer.objects.get(id=id)
    customer.name = name
    customer.address = address
    customer.contact = contact
    customer.mappoint = mappoint
    customer.save()
    out = 'razvozki:' + from_where
    return HttpResponseRedirect(reverse(out))


def addrecord_cst(request):
    name = request.POST['name']
    address = request.POST['address']
    contact = request.POST['contact']
    mappoint = request.POST['mappoint']
    customer_clr = Customer_clr(name=name, address=address, contact=contact, mappoint=mappoint, clr='text-secondary')
    customer_clr.save()
    return HttpResponseRedirect(reverse('razvozki:customers'))


def print_rzv(request, date_r):
    razvozka = []
    for rzv in Razvozka.objects.filter(date=date_r):
        razvozka.append(rzv)
    date_r = datetime.datetime.strptime(date_r, '%Y-%m-%d').strftime('%d.%m.%Y')
    context = {'date_r': date_r, 'razv': razvozka}
    return render(request, 'razvozki/print.html', context)


def double(request):
    navi = 'double'
    cust = []
    #    sust = Customer_clr.objects.filter(clr='text-danger')
    for cst in Customer_clr.objects.filter(clr='text-danger').order_by('name', 'id'):
        cust.append(cst)
    context = {'navi': navi, 'cust': cust}
    return render(request, 'razvozki/double.html', context)


def unite_cst(request):
    cst_lv = request.POST['cst_lv']
    cst_dt = request.POST['cst_dt']
    customer_lv = Customer.objects.get(id=cst_lv)
    customer_dlt = Customer.objects.get(id=cst_dt)
    for rzv in Razvozka.objects.filter(customer=customer_dlt):
        rzv.customer = customer_lv
        rzv.save()
    customer_dlt.delete()
    return HttpResponseRedirect(reverse('razvozki:double'))


def admin(request):
    navi = 'admin'
    cust = Customer_clr.objects.order_by('name')
    razv = Razvozka_import.objects.order_by('-date', '-date_id')
    razv_count_imp = Razvozka_import.objects.all().count()
    customer_count = Customer_clr.objects.all().count()
    razv_count = Razvozka.objects.all().count()
    context = {'cust': cust, 'razv': razv, 'navi': navi, 'razv_count_imp': razv_count_imp,
               'customer_count': customer_count, 'razv_count': razv_count}
    return render(request, 'razvozki/admin.html', context)


def import_csv(request):
    file_name = request.POST['Chosen']
    date_begin = request.POST['date_begin']
    date_end = request.POST['date_end']
    if date_begin == '' and date_end == '':
        Razvozka_import.objects.all().delete()
    elif date_begin != '' and date_end == '':
        for rzv in Razvozka_import.objects.all():
            if str(rzv.date) >= date_begin:
                rzv.delete()
    elif date_begin == '' and date_end != '':
        for rzv in Razvozka_import.objects.all():
            if str(rzv.date) <= date_end:
                rzv.delete()
    else:
        for rzv in Razvozka_import.objects.all():
            if date_begin <= str(rzv.date) <= date_end:
                rzv.delete()

    if file_name != '':
        file_name = 'razvozki/files/' + file_name
        with open(file_name, newline='') as csvfile:
            exract_file = csv.reader(csvfile, delimiter=';')
            for row in exract_file:
                if 'Развозка' in row[0]:
                    y_r = (row[0][-4:])
                    m_r = (row[0][-7:-5])
                    d_r = (row[0][-10:-8])
                    date_r = y_r + '-' + m_r + '-' + d_r
                elif (row[1] != '' or row[2] != '' or row[3] != '' or row[4] != '') and row[0] != '№':
                    deliver = ['Сдать', 'сдать', 'Отдать', 'отдать', 'Доставка:', 'доставка']
                    take = ['Забрать', 'забрать']
                    deliver_pos = -1
                    deliver_len = 0
                    take_pos = -1
                    take_len = 0
                    to_do_len = len(row[4])
                    for d in deliver:
                        if (row[4].rfind(d)) != -1:
                            deliver_pos = row[4].rfind(d)
                            deliver_len = len(d)
                    for t in take:
                        if (row[4].rfind(t)) != -1:
                            take_pos = row[4].rfind(t)
                            take_len = len(t)
                    if deliver_pos < take_pos and deliver_pos != -1:
                        to_do_deliver = row[4][slice((deliver_pos + deliver_len), (take_pos))]
                        to_do_take = row[4][slice((take_pos + take_len), to_do_len)]
                    elif take_pos < deliver_pos and take_pos != -1:
                        to_do_take = row[4][slice((take_pos + take_len), (deliver_pos))]
                        to_do_deliver = row[4][slice((deliver_pos + deliver_len), to_do_len)]
                    elif deliver_pos == -1 and take_pos != -1:
                        to_do_take = row[4][slice((take_pos + take_len), to_do_len)]
                        to_do_deliver = ''
                    elif deliver_pos != -1 and take_pos == -1:
                        to_do_deliver = row[4][slice((deliver_pos + deliver_len), to_do_len)]
                        to_do_take = ''
                    else:
                        to_do_take = row[4]
                        to_do_deliver = ''

                    customer_name = row[1]
                    address = row[2]
                    contact = row[3]
                    while '  ' in customer_name:
                        customer_name = customer_name.replace('  ', ' ')
                    while '  ' in address:
                        address = address.replace('  ', ' ')
                    while '  ' in contact:
                        contact = contact.replace('  ', ' ')
                    while '  ' in to_do_take:
                        to_do_take = to_do_take.replace('  ', ' ')
                    while '  ' in to_do_deliver:
                        to_do_deliver = to_do_deliver.replace('  ', ' ')

                    if date_begin <= date_r <= date_end or date_end == '' and date_r >= date_begin:
                        razv_import = Razvozka_import(
                            date=date_r,
                            date_id=row[0],
                            customer_name=customer_name,
                            address=address,
                            contact=contact,
                            to_do_take=to_do_take,
                            to_do_deliver=to_do_deliver)
                        razv_import.save()
    return HttpResponseRedirect(reverse('razvozki:admin'))


def import_cst(request):
    razv_imp = Razvozka_import.objects.order_by('-date', '-date_id')
    cust_clr = Customer_clr.objects.order_by('name')
    for rzv in razv_imp:
        new_customer = Customer_clr(name=rzv.customer_name, address=rzv.address,
                                    contact=rzv.contact, clr='text-secondary')
        tmp = find_dubl_cst(new_customer, cust_clr)
        if rzv.customer is None and not tmp:
            new_customer.save()
            rzv.customer = new_customer
            rzv.save()
        elif rzv.customer is None and tmp:
            id_cst = find_dubl_cst_id(new_customer, cust_clr)
            new_customer = Customer_clr.objects.get(id=id_cst)
            rzv.customer = new_customer
            rzv.save()
        cust_clr = Customer_clr.objects.order_by('name')
    return HttpResponseRedirect(reverse('razvozki:admin'))

def delete_all_cst(request):
    cust_clr = Customer_clr.objects.order_by('name')
    for cst in cust_clr:
        cst.delete()
    return HttpResponseRedirect(reverse('razvozki:admin'))



