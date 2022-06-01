# Create your views here.

import datetime
from datetime import date, timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Razvozka, Customer, Customer_clr, Razvozka_import
from django.db.models import F, Q, Case, Value, When
from django.db.models.lookups import GreaterThan, LessThan
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.db import transaction
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
#    for rzv1 in rzv:
#        if rzv1.customer is None:
#            rzv_clr.append(
#                Razvozka_clr(rzv1.id, rzv1.date, rzv1.date_id, rzv1.customer, rzv1.customer_name, rzv1.address,
#                             rzv1.contact, rzv1.to_do_take, rzv1.to_do_deliver, 'text-dark'))
#        else:
#            rzv_clr.append(
#                Razvozka_clr(rzv1.id, rzv1.date, rzv1.date_id, rzv1.customer, rzv1.customer_name, rzv1.address,
#                             rzv1.contact, rzv1.to_do_take, rzv1.to_do_deliver, 'text-success'))

    f_rzv0 = {}
    for r in rzv:
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
    page_num = request.POST['page_number_add']
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
    clr = 'text-secondary'
    razvozka = Razvozka(date=date, date_id=date_id, customer_name=customer_name, customer=customer, address=address,
                        contact=contact,
                        to_do_take=to_do_take, to_do_deliver=to_do_deliver, clr=clr)
    razvozka.save()
    if page_num != '':
        page_num = '?page=' + page_num
    return HttpResponseRedirect(reverse('razvozki:index') + page_num)


def delete_rzv(request, id):
    razvozka = Razvozka.objects.get(id=id)
    razvozka.delete()
    return HttpResponseRedirect(reverse('razvozki:index'))


def updaterecord_rzv(request, id):
    page_num = request.POST['page_number_upd']
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
    if page_num != '':
        page_num = '?page=' + page_num
    return HttpResponseRedirect(reverse('razvozki:index') + page_num)


def main_rzv(request):
    template = loader.get_template('razvozki/main.html')
    return HttpResponse(template.render({}, request))


def newdate_rzv(request):
    datenew = request.POST['date']
    datenew = datetime.datetime.strptime(datenew, '%d.%m.%Y').strftime('%Y-%m-%d')
    razvozka = Razvozka(date=datenew, date_id=1, customer_name='', customer=None, address='', contact='',
                        to_do_take='', to_do_deliver='', clr='text-secondary')
    razvozka.save()
    return HttpResponseRedirect(reverse('razvozki:index'))


def customers(request, order):
    navi = 'customers'
    cust = Customer_clr.objects.order_by(order)

    paginator = Paginator(cust, 30)  # Show 30.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'navi': navi, 'page_obj': page_obj, 'order': order}
    return render(request, 'razvozki/customers.html', context)


@transaction.atomic()
def cst_double_search(request):
    order = request.POST['order_doub']
    cust = Customer_clr.objects.all()
    for cst1 in cust:
        cst1.clr = ''
        if find_dubl_cst(cst1, cust)[0]:
            cst1.clr = 'text-danger'
        Customer_clr.objects.filter(id=cst1.id).update(clr=cst1.clr)
    context = {'order': order}
    return HttpResponseRedirect(reverse('razvozki:customers', args=[order]), context)


def customers_clr(request):
    #    return

    # def customers_checks(request):
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
        if rzv.customer is None and find_dubl_cst(rzv.customer, cust)[0]:
            new_customer = Customer_clr(name=rzv.customer_name, address=rzv.address,
                                        contact=rzv.contact, clr='text-secondary')
            new_customer.save()
            rzv.customer = new_customer
            rzv.save()
    return HttpResponseRedirect(reverse('razvozki:customers', args=['name']))


def cust_trim_replace(cst1, cst2):
    cst1_name = cst1.name.replace('ИП ', '')
    cst1_name = cst1_name.replace(' ', '')
    cst1_name = cst1_name.replace('-', '')
    cst1_name = cst1_name.replace('.', '')
    cst1_name = cst1_name.replace(',', '')
    cst1_name = cst1_name.replace('"', '')
    cst1_name = cst1_name.replace('?', '')

    cst2_name = cst2.name.replace('ИП ', '')
    cst2_name = cst2_name.replace(' ', '')
    cst2_name = cst2_name.replace('-', '')
    cst2_name = cst2_name.replace('.', '')
    cst2_name = cst2_name.replace(',', '')
    cst2_name = cst2_name.replace('"', '')
    cst2_name = cst2_name.replace('?', '')

    cst1_address = cst1.address.replace('г.', '')
    cst1_address = cst1_address.replace(' ', '')
    cst1_address = cst1_address.replace('-', '')
    cst1_address = cst1_address.replace('.', '')
    cst1_address = cst1_address.replace(',', '')
    cst1_address = cst1_address.replace('?', '')

    cst2_address = cst2.address.replace('г.', '')
    cst2_address = cst2_address.replace(' ', '')
    cst2_address = cst2_address.replace('-', '')
    cst2_address = cst2_address.replace('.', '')
    cst2_address = cst2_address.replace(',', '')
    cst2_address = cst2_address.replace('?', '')

    return [cst1_name, cst1_address, cst2_name, cst2_address]


def find_dubl_cst(cst1, cust):
    result = False
    cst_id = ''
    for cst2 in cust:
        cst1_name = cust_trim_replace(cst1, cst2)[0]
        cst1_address = cust_trim_replace(cst1, cst2)[1]
        cst2_name = cust_trim_replace(cst1, cst2)[2]
        cst2_address = cust_trim_replace(cst1, cst2)[3]

        if ((cst1_name.casefold() == cst2_name.casefold() or cst1_address.casefold() == cst2_address.casefold()
             or cst1.mappoint == cst2.mappoint and cst1.mappoint != '') and cst1.id != cst2.id):
            result = True
            cst_id = cst2.id

    return [result, cst_id]


def delete_cst(request, id):
    page_num = request.POST['page_number_del']
    order = request.POST['order_del']
    customer = Customer.objects.get(id=id)
    customer.delete()
    context = {'order': order}
    if page_num != '':
        page_num = '?page=' + page_num
    return HttpResponseRedirect(reverse('razvozki:customers', args=[order]) + page_num, context)


def updaterecord_cst(request, from_where):
    page_num = request.POST['page_number_upd']
    order = request.POST['order_up']
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
    if page_num != '':
        page_num = '?page=' + page_num
    context = {'order': order}
    return HttpResponseRedirect((reverse(out, args=[order]) + page_num), context,)


def addrecord_cst(request):
    page_num = request.POST['page_number_add']
    order = request.POST['order_add']
    name = request.POST['name']
    address = request.POST['address']
    contact = request.POST['contact']
    mappoint = request.POST['mappoint']
    customer_clr = Customer_clr(name=name, address=address, contact=contact, mappoint=mappoint, clr='text-secondary')
    customer_clr.save()
    if page_num != '':
        page_num = '?page=' + page_num
    context = {'order': order}
    return HttpResponseRedirect(reverse('razvozki:customers', args=[order]) +page_num, context)


def print_rzv(request, date_r):
    razvozka = []
    for rzv in Razvozka.objects.filter(date=date_r).order_by('date_id'):
        razvozka.append(rzv)
    date_r = datetime.datetime.strptime(date_r, '%Y-%m-%d').strftime('%d.%m.%Y')
    context = {'date_r': date_r, 'razv': razvozka}
    return render(request, 'razvozki/print.html', context)


def double(request, order):
    navi = 'double'
    cust = []
    #    sust = Customer_clr.objects.filter(clr='text-danger')
    for cst in Customer_clr.objects.filter(clr='text-danger').order_by(order, 'id'):
        cust.append(cst)
    context = {'navi': navi, 'cust': cust, 'order': order}
    return render(request, 'razvozki/double.html', context)


def unite_cst(request):
    order = request.POST['order_un']
    cst_lv = request.POST['cst_lv']
    cst_dt = request.POST['cst_dt']
    customer_lv = Customer_clr.objects.get(id=cst_lv)
    customer_dlt = Customer_clr.objects.get(id=cst_dt)
    for rzv in Razvozka.objects.filter(customer=customer_dlt):
        rzv.customer = customer_lv
        rzv.save()
    customer_dlt.delete()
    context = {'order': order}
    return HttpResponseRedirect(reverse('razvozki:double', args=[order]), context)


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
#        file_name = 'razvozki/files/' + file_name
        with open(file_name, newline='') as csvfile:
            exract_file = csv.reader(csvfile, delimiter=';')
            for row in exract_file:
                if 'Развозка' in row[0]:
                    y_r = (row[0][-4:])
                    m_r = (row[0][-7:-5])
                    d_r = (row[0][-10:-8])
                    date_r = y_r + '-' + m_r + '-' + d_r
                elif (row[1] != '' or row[2] != '' or row[3] != '' or row[4] != '') and row[0] != '№':
                    deliver = ['Сдать', 'сдать', 'СДАТЬ', 'ОТДАТЬ', 'Отдать', 'отдать', 'Доставка:', 'доставка']
                    take = ['Забрать', 'забрать', 'ЗАБРАТЬ']
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
                            to_do_deliver=to_do_deliver,
                            clr='text-secondary')
                        razv_import.save()
    return HttpResponseRedirect(reverse('razvozki:admin'))


def import_cst(request):
    razv_imp = Razvozka_import.objects.order_by('-date', '-date_id')
    cust_clr = Customer_clr.objects.order_by('name')
    for rzv in razv_imp:
        new_customer = Customer_clr(name=rzv.customer_name, address=rzv.address,
                                    contact=rzv.contact, clr='text-secondary')
        new_customer.name = trim_cst(new_customer)[0]
        new_customer.address = trim_cst(new_customer)[1]
        new_customer.contact = trim_cst(new_customer)[2]

        tmp = find_dubl_cst(new_customer, cust_clr)[0]
        if rzv.customer is None and not tmp and new_customer.name != '':
            new_customer.save()
            rzv.customer = new_customer
            rzv.save()
        elif rzv.customer is None and tmp:
            id_cst = find_dubl_cst(new_customer, cust_clr)[1]
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

@transaction.atomic()
def clean_cst(request):
    cust_clr = Customer_clr.objects.order_by('name')
    for cst1 in cust_clr:
        cst1_name = trim_cst(cst1)[0]
        cst1_address = trim_cst(cst1)[1]
        cst1_contact = trim_cst(cst1)[2]
        Customer_clr.objects.filter(id=cst1.id).update(name=cst1_name, address=cst1_address, contact=cst1_contact)
    return HttpResponseRedirect(reverse('razvozki:admin'))

def trim_cst(cst1):
    cst1_name = cst1.name.replace('ИП ', '')
    cst1_name = cst1_name.replace('  ', ' ')
    cst1_name = cst1_name.replace('"', '')
    cst1_name = cst1_name.replace('?', '')

    cst1_address = cst1.address.replace('г.', '')
    cst1_address = cst1_address.replace('  ', ' ')
    cst1_address = cst1_address.replace('?', '')

    cst1_contact = cst1.contact.replace('  ', ' ')
    cst1_contact = cst1_contact.replace('"', '')
    cst1_contact = cst1_contact.replace('?', '')
    return [cst1_name, cst1_address, cst1_contact]


def trim_rzv(cst1):
    cst1_name = cst1.customer_name.replace('ИП ', '')
    cst1_name = cst1_name.replace('  ', ' ')
    cst1_name = cst1_name.replace('"', '')
    cst1_name = cst1_name.replace('?', '')

    cst1_address = cst1.address.replace('г.', '')
    cst1_address = cst1_address.replace('  ', ' ')
    cst1_address = cst1_address.replace('?', '')

    cst1_contact = cst1.contact.replace('  ', ' ')
    cst1_contact = cst1_contact.replace('"', '')
    cst1_contact = cst1_contact.replace('?', '')

    cst1_to_do_take = cst1.to_do_take.replace('  ', ' ')
    cst1_to_do_take = cst1_to_do_take.replace('"', '')
    cst1_to_do_take = cst1_to_do_take.replace('?', '')

    cst1_to_do_deliver = cst1.to_do_deliver.replace('  ', ' ')
    cst1_to_do_deliver = cst1_to_do_deliver.replace('"', '')
    cst1_to_do_deliver = cst1_to_do_deliver.replace('?', '')
    return [cst1_name, cst1_address, cst1_contact, cst1_to_do_take, cst1_to_do_deliver]

@transaction.atomic()
def clean_rzv(request):
    razv = Razvozka_import.objects.order_by('-date', 'date_id')
    for rzv in razv:
        rzv_name = trim_rzv(rzv)[0]
        rzv_address = trim_rzv(rzv)[1]
        rzv_contact = trim_rzv(rzv)[2]
        rzv_to_do_take = trim_rzv(rzv)[3]
        rzv_to_do_deliver = trim_rzv(rzv)[4]
        Razvozka_import.objects.filter(id=rzv.id).update(customer_name=rzv_name, address=rzv_address, contact=rzv_contact,
                                                  to_do_take=rzv_to_do_take, to_do_deliver=rzv_to_do_deliver)
    return HttpResponseRedirect(reverse('razvozki:admin'))

@transaction.atomic()
def export_rzv(request):
    date_begin = request.POST['date_begin_exp']
    if date_begin != '':
        date_start = datetime.datetime.strptime(date_begin, '%Y-%m-%d') - datetime.timedelta(days=1)
#        date_start = date_start.strftime('%Y-%m-%d')
    date_end = request.POST['date_end_exp']
    if date_end != '':
        date_finish = datetime.datetime.strptime(date_end, '%Y-%m-%d') + datetime.timedelta(days=1)
#        date_finish = date_finish.strftime('%Y-%m-%d')

    if date_begin == '' and date_end == '':
        Razvozka.objects.all().delete()
        Razvozka.objects.bulk_create(Razvozka_import.objects.all())
    elif date_begin != '' and date_end == '':
        for rzv in Razvozka.objects.all():
            if str(rzv.date) >= date_begin:
                rzv.delete()
        for rzv in Razvozka_import.objects.all():
            if str(rzv.date) >= date_begin:
                new_rzv = Razvozka(date_id=rzv.date_id, customer=rzv.customer, customer_name =rzv.customer_name,
                                   address=rzv.address, contact=rzv.contact, to_do_take=rzv.to_do_take,
                                   to_do_deliver=rzv.to_do_deliver, map_point=rzv.map_point, date=rzv.date,
                                   clr=rzv.clr)
                new_rzv.save()
    elif date_begin == '' and date_end != '':
        for rzv in Razvozka.objects.all():
            if str(rzv.date) <= date_end:
                rzv.delete()
        for rzv in Razvozka_import.objects.all():
            if str(rzv.date) <= date_end:
                new_rzv = Razvozka(date_id=rzv.date_id, customer=rzv.customer, customer_name=rzv.customer_name,
                                   address=rzv.address, contact=rzv.contact, to_do_take=rzv.to_do_take,
                                   to_do_deliver=rzv.to_do_deliver, map_point=rzv.map_point, date=rzv.date,
                                   clr=rzv.clr)
                new_rzv.save()
    else:
        for rzv in Razvozka.objects.all():
            if date_begin <= str(rzv.date) <= date_end:
                rzv.delete()
        for rzv in Razvozka_import.objects.all():
            if date_begin <= str(rzv.date) <= date_end:
                new_rzv = Razvozka(date_id=rzv.date_id, customer=rzv.customer, customer_name=rzv.customer_name,
                                   address=rzv.address, contact=rzv.contact, to_do_take=rzv.to_do_take,
                                   to_do_deliver=rzv.to_do_deliver, map_point=rzv.map_point, date=rzv.date,
                                   clr=rzv.clr)
                new_rzv.save()

#    Razvozka.objects.bulk_create(Razvozka_import.objects.All)
    return HttpResponseRedirect(reverse('razvozki:admin'))

