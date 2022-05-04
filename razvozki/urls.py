from django.urls import path

from . import views

app_name = 'razvozki'
urlpatterns = [
    path('', views.index, name='index'),
#    path('specifics/<int:razvozki_id>/', views.detail, name='detail'),
    path('add_razv/<int:id>/', views.add_razv, name='add_razv'),
    path('addrecord_razv/', views.addrecord_razv, name='addrecord_razv'),
    path('delete_rzv/<int:id>', views.delete_rzv, name='delete_rzv'),
    path('update_rzv/<int:id>', views.update_rzv, name='update_rzv'),
    path('updaterecord_rzv/<int:id>', views.updaterecord_rzv, name='updaterecord_rzv'),
#    path('<str:razvozka_date>/', views.date_detail, name='date_detail'),
#    path('<int:razvozki>/results/', views.results, name='results'),
    path('main', views.main_rzv, name='main_rzv'),
    path('newdate_rzv', views.newdate_rzv, name='newdate_rzv'),
    path('customers', views.customers, name='customers'),
    path('add_cst', views.add_cst, name='add_cst'),
    path('addrecord_cst/', views.addrecord_cst, name='addrecord_cst'),
    path('delete_cst/<int:id>', views.delete_cst, name='delete_cst'),
    path('updaterecord_cst/<int:id>', views.updaterecord_cst, name='updaterecord_cst'),

]