from django.urls import path, include

from . import views

app_name = 'razvozki'

urlpatterns = [
    path('', views.index, name='index'),
    path('addrecord_razv/', views.addrecord_razv, name='addrecord_razv'),
    path('delete_rzv/<int:id>', views.delete_rzv, name='delete_rzv'),
    path('upd_rzv_txt', views.updrzv_txt),
    path('updaterecord_rzv/<int:id>', views.updaterecord_rzv, name='updaterecord_rzv'),
    path('main', views.main_rzv, name='main_rzv'),
    path('newdate_rzv', views.newdate_rzv, name='newdate_rzv'),
    path('customers/<order>', views.customers, name='customers'),
    path('customers_clr', views.customers_clr, name='customers_clr'),
    path('customers/addrecord_cst/', views.addrecord_cst, name='addrecord_cst'),
    path('customers/delete_cst/<int:id>', views.delete_cst, name='delete_cst'),
    path('updaterecord_cst/<from_where>', views.updaterecord_cst, name='updaterecord_cst'),
    path('print_rzv/<str:date_r>', views.print_rzv, name='print_rzv'),
    path('double/<order>', views.double, name='double'),
    path('double/unite_cst/', views.unite_cst, name='unite_cst'),
    path('admin', views.admin, name='admin'),
    path('import_csv', views.import_csv, name='import_csv'),
    path('import_cst', views.import_cst, name='import_cst'),
    path('delete_all_cst', views.delete_all_cst, name='delete_all_cst'),
    path('cst_double_search', views.cst_double_search, name='cst_double_search'),
    path('clean_rzv', views.clean_rzv, name='clean_rzv'),
    path('clean_cst', views.clean_cst, name='clean_cst'),
    path('export_rzv', views.export_rzv, name='export_rzv'),
    path('customers.xml', views.cust_xml, name='customers.xml'),

]


