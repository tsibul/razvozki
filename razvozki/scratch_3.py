from django.apps import AppConfig
from django.db import models


class RazvozkiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'razvozki'

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from models import Razvozka
from django.template import loader
from django.shortcuts import render

DJANGO_SETTINGS_MODULE=razv.settings


tmp_razvozka = Razvozka.objects.order_by('-date', 'date_id')
tmp_context = {}
for tmp in tmp_razvozka:
    tmp_context.append = {
        'date': tmp.date,
        'razv': tmp,
        'to_do': 'Сдать: ' + tmp.to_do_deliver + ', Забрать: ' + tmp.to_do_take
    }

print()
