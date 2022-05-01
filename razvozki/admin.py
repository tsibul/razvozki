from django.contrib import admin


from .models import Customer
from .models import Razvozka

admin.site.register(Customer)
admin.site.register(Razvozka)