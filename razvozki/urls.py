from django.urls import path, include

from . import views

app_name = 'razvozki'

urlpatterns = [
    path('', views.index, name='index'),
    path('addrecord_razv/', views.addrecord_razv, name='addrecord_razv'),
    path('delete_rzv/<int:id>', views.delete_rzv, name='delete_rzv'),
    path('updaterecord_rzv/<int:id>', views.updaterecord_rzv, name='updaterecord_rzv'),
    path('main', views.main_rzv, name='main_rzv'),
    path('newdate_rzv', views.newdate_rzv, name='newdate_rzv'),
    path('customers', views.customers, name='customers'),
    path('customers_clr', views.customers_clr, name='customers_clr'),
    path('addrecord_cst/', views.addrecord_cst, name='addrecord_cst'),
    path('delete_cst/<int:id>', views.delete_cst, name='delete_cst'),
    path('updaterecord_cst/<from_where>', views.updaterecord_cst, name='updaterecord_cst'),
    path('print_rzv/<str:date_r>', views.print_rzv, name='print_rzv'),
    path('double/', views.double, name='double'),
    path('double/unite_cst/', views.unite_cst, name='unite_cst'),
    path('admin', views.admin, name='admin'),
    path('import_csv', views.import_csv, name='import_csv'),
    path('import_cst', views.import_cst, name='import_cst'),
    path('delete_all_cst', views.delete_all_cst, name='delete_all_cst'),

]


