# Create your views here.

import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Razvozka, Customer, Customer_clr, Razvozka_import
from django.db.models import Q
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.db import transaction
from django.core.files import File
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt



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
    dateold = datetime.date.today() - datetime.timedelta(days=3)
    datenew = datenew.strftime('%Y-%m-%d')
    dateold = dateold.strftime('%Y-%m-%d')
    #    date = datetime.date.today()
    rzv = Razvozka.objects.order_by('-date', 'date_id')
    cust = list(Customer.objects.order_by('name'))

    f_rzv0 = {}
    for r in rzv:
        if r.date not in f_rzv0:
            f_rzv0[r.date] = []
        f_rzv0[r.date].append(r)

    f_rzv2 = list(f_rzv0.items())
    paginator = Paginator(f_rzv2, 7)
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
    date_range.sort(reverse=True)
    rzv_len = []
    for rzv in f_rzv:
        rzv_len.append([rzv, len(f_rzv0[rzv])])
    context = {'f_rzv': f_rzv, 'datenew': datenew, 'navi': navi, 'cust': cust, 'page_obj': page_obj,
               'page_number': page_number, 'date_range': date_range, 'rzv_len': rzv_len, 'active1': 'active',
               'dateold': dateold}
    return render(request, 'razvozki/index.html', context)


def delete_rzv(request, id):
    razvozka = Razvozka.objects.get(id=id)
    razvozka.delete()
    return HttpResponseRedirect(reverse('razvozki:index'))

@csrf_exempt
def updaterecord_rzv(request):
    page_num = request.POST['page_number_upd']
    date = request.POST['date']
    date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')
    date_id = request.POST['date_id']
    address = request.POST['address']
    customer_name = request.POST['customer']
    contact = request.POST['contact']
    mappoint = request.POST['mappoint']
    to_do_take = request.POST['to_do_take']
    to_do_deliver = request.POST['to_do_deliver']
    try:
        rzv_id = request.POST['rzv_id']
        razvozka = Razvozka.objects.get(id=rzv_id)
        razvozka.address = address
        razvozka.contact = contact
        razvozka.map_point = mappoint
        razvozka.to_do_take = to_do_take
        razvozka.to_do_deliver = to_do_deliver
        razvozka.date = date
        razvozka.date_id = date_id
        date_create = razvozka.date_create
    except:
        date_create =datetime.date.today()
        razvozka = Razvozka(address=address, contact=contact, fulfilled=False, date=date, date_id=date_id,
                            map_point=mappoint, to_do_take=to_do_take, to_do_deliver=to_do_deliver,
                            date_create=date_create)

    customer_id = request.POST['customer_id']
    if customer_id != '':
        customer = Customer.objects.get(id=customer_id)
        razvozka.customer = customer
        razvozka.customer_name = customer.name
    else:
        razvozka.customer_name = customer_name
    return_goods_id = request.POST['upd_id']
    if return_goods_id != '':
        razvozka_return = Razvozka.objects.get(id=return_goods_id)
        razvozka.return_goods = razvozka_return
        razvozka.return_from = True
    else:
        razvozka.return_from = False
    date_until = request.POST['date_until']
    if date_until != '':
        razvozka.date_until = date_until
    elif date == '2100-01-01':
        date_until = date_create + datetime.timedelta(days=7)
        razvozka.date_until = date_until
    razvozka.save()
    if page_num != '':
        page_num = '?page=' + page_num
    return HttpResponseRedirect(reverse('razvozki:index') + page_num)


def main_rzv(request):
    template = loader.get_template('razvozki/main.html')
    return HttpResponse(template.render({}, request))


def customers(request):
    navi = 'customer'
    cust = Customer.objects.order_by('name')

    paginator = Paginator(cust, 30)  # Show 30.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_name = list(page_obj.object_list)[0].name + ' - ' + list(page_obj.object_list)[-1].name

    customer_range = []
    for i in range(page_obj.paginator.num_pages):
        page_obj2 = paginator.get_page(i + 1)
        customer_range.append([i + 1, list(page_obj2.object_list)[0].name + ' - ' + list(page_obj2.object_list)[-1].name])

    context = {'navi': navi, 'page_obj': page_obj, 'active2': 'active', 'page_name': page_name,
               'customer_range': customer_range}
    return render(request, 'razvozki/customers.html', context)


@transaction.atomic()
def cst_double_search(request):
    """
    looking for doubles
    :param request:
    :return: change color to danger
    """
    order = request.POST['order_doub']
    cust = Customer_clr.objects.all()
    for cst1 in cust:
        cst1.clr = ''
        if find_dubl_cst(cst1, cust)[0]:
            cst1.clr = 'text-danger'
        Customer_clr.objects.filter(id=cst1.id).update(clr=cst1.clr)
    context = {'order': order}
    return HttpResponseRedirect(reverse('razvozki:customers'), context)


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
    """
    :param cst1: first customer to compare
    :param cst2: second customer to compare
    :return:
    """
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
    """
    looking doubles in db
    :param cst1: element if have double
    :param cust: db in which searching element
    :return: True if cst1 in cust db
    """
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


def updaterecord_cst(request):
    page_num = request.POST['page_number_upd']
#    order = request.POST['order_up']
    name = request.POST['customer']
    address = request.POST['address']
    contact = request.POST['contact']
    mappoint = request.POST['mappoint']
    try:
        cst_id = request.POST['cst_id']
        customer = Customer.objects.get(id=cst_id)
        customer.name = name
        customer.address = address
        customer.contact = contact
        customer.mappoint = mappoint
    except:
        customer = Customer(name=name, address=address, contact=contact, mappoint=mappoint)
    customer.save()
    out = 'razvozki:customers'
    if page_num != '':
        page_num = '?page=' + page_num
    return HttpResponseRedirect(reverse(out) + page_num)


def print_rzv(request, date_r):
    """
    :param date_r: date for print report
    :return:
    """
    razvozka = Razvozka.objects.filter(Q(date=date_r) & Q(date_id__lt=20)).order_by('date_id')
    date_r = datetime.datetime.strptime(date_r, '%Y-%m-%d').strftime('%d.%m.%Y')
    context = {'date_r': date_r, 'razv': razvozka}
    return render(request, 'razvozki/print.html', context)


def double(request, order):
    """
    looking for double customers and show them (color=danger)
    :param request:
    :param order: order of db
    :return:
    """
    navi = 'double'
    cust = []
    for cst in Customer_clr.objects.filter(clr='text-danger').order_by(order, 'id'):
        cust.append(cst)
    context = {'navi': navi, 'cust': cust, 'order': order, 'active3': 'active'}
    return render(request, 'razvozki/double.html', context)


def unite_cst(request):
    """
    unite two customers checked
    :param request: receive what was checked
    :return:
    """
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
               'customer_count': customer_count, 'razv_count': razv_count, 'active4': 'active'}
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
                        to_do_deliver = row[4][slice((deliver_pos + deliver_len), take_pos)]
                        to_do_take = row[4][slice((take_pos + take_len), to_do_len)]
                    elif take_pos < deliver_pos and take_pos != -1:
                        to_do_take = row[4][slice((take_pos + take_len), deliver_pos)]
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
    razv_imp = Razvozka.objects.order_by('-date', '-date_id')
    cust_clr = Customer_clr.objects.order_by('name')
    for rzv in razv_imp:
        new_customer = Customer_clr(name=rzv.customer_name, address=rzv.address,
                                    contact=rzv.contact, clr='text-dark')
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
    razv = Razvozka.objects.order_by('-date', 'date_id')
    for rzv in razv:
        rzv_name = trim_rzv(rzv)[0]
        rzv_address = trim_rzv(rzv)[1]
        rzv_contact = trim_rzv(rzv)[2]
        rzv_to_do_take = trim_rzv(rzv)[3]
        rzv_to_do_deliver = trim_rzv(rzv)[4]
        Razvozka_import.objects.filter(id=rzv.id).update(customer_name=rzv_name, address=rzv_address,
                                                         contact=rzv_contact, to_do_take=rzv_to_do_take,
                                                         to_do_deliver=rzv_to_do_deliver)
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

def updrzv_txt(request):
    f = open('razvozki/static/razvozki/upd_rzv.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")

def cust_xml(request):
    """
    :return: Customer db in xml format
    """
    cust = Customer.objects.all().order_by('name')
    data = '<?xml version="1.0" encoding="UTF-8"?><CUSTOMERS>'
    for cst in cust:
        data = data + ('<Customer><cst_id>' + str(cst.id) + '</cst_id>' +
        '<name>' + cst.name + '</name>' + '<address>' + cst.address + ' ' + '</address>' +
        '<contact>' + cst.contact + ' ' + '</contact></Customer>')
    data = data + '</CUSTOMERS>'

#    pprint.pprint(data)
    return HttpResponse(data,  content_type="text/xml")


def search_(request, navi):
    srch = request.POST['search_']

    if navi == 'razvozka':
        rzv = list(Razvozka.objects.filter(Q(customer_name__icontains=srch) | Q(address__icontains=srch) |
                                           Q(date__icontains=srch)).order_by('-date'))
        razv = {}
        for r in rzv:
            if r.date not in razv:
                razv[r.date] = []
            razv[r.date].append(r)

        context = {'navi': navi, 'f_rzv': razv, 'srch': srch , 'look_up': True, 'active1': 'active'}
        return render(request, 'razvozki/index.html', context)

    if navi == 'customer':
        razv = list(Customer.objects.filter(Q(name__icontains=srch) | Q(address__icontains=srch)).order_by('name'))
        context = {'navi': navi, 'page_obj': razv, 'srch': srch, 'look_up': True, 'active2': 'active'}
        return render(request, 'razvozki/customers.html', context)

@csrf_exempt
def fulfilled_chg(request, id):
    razv = Razvozka.objects.get(id=id)
    razv.fulfilled = not razv.fulfilled
    razv.save()
    return HttpResponse()


@csrf_exempt
def return_all(request, id):
    razv = Razvozka.objects.get(id=id)
    razv.return_all = not razv.return_all
    razv.save()
    return HttpResponse()


@csrf_exempt
def deliver_to(request, id):
    razv = Razvozka.objects.get(id=id)
    if razv.deliver_to and not razv.return_all:
        razv.deliver_to = False
        razv.save()
    elif not razv.deliver_to:
        razv.deliver_to = True
        razv.save()
        date = '2100-01-01'
        date_create = razv.date
        date_until = date_create + datetime.timedelta(days=8)
        customer = razv.customer
        customer_name = razv.customer_name
        map_point = razv.map_point
        address = razv.address
        contact = razv.contact
        return_from = True
        return_goods = razv
        to_do_take = 'Поменять это поле!!!'
        new_razv = Razvozka(fulfilled=False, date=date, date_create=date_create, date_until=date_until, customer=customer,
                            customer_name=customer_name, address=address, contact=contact, map_point=map_point,
                            return_from=return_from, return_goods=return_goods, to_do_take=to_do_take)
        new_razv.save()
    return HttpResponse()


def rzv_return_xml(request, id):
    """
    :return: razvozki, not returned db in xml format filter by customer
    """
    cust = Customer.objects.get(id=id)
    razv = Razvozka.objects.all().filter(Q(deliver_to=True) & Q(return_all=False) & Q(customer=cust))
    data = '<?xml version="1.0" encoding="UTF-8"?><RAZVOZKI>'
    for rzv in razv:
        data = data + ('<Razvozka><id>' + str(rzv.id) + '</id>' +
                       '<date>' + str(rzv.date) + '</date>' + '<date_id>' + str(rzv.date_id) + '</date_id>' +
        '<customer_name>' + rzv.customer_name + '</customer_name>' + '<address>' + rzv.address + ' ' +
                       '</address><contact>' + rzv.contact + ' ' + '</contact>' + '<to_do_deliver>' +
                       rzv.to_do_deliver + '</to_do_deliver></Razvozka>')
    data = data + '</RAZVOZKI>'

#    pprint.pprint(data)
    return HttpResponse(data,  content_type="text/xml")
