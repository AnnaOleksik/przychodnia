from django.contrib import admin
from .models import Lekarze
from .models import Pacjenci
from .models import Wizyta
from .models import Zalecenia
from .models import Cennik,Category,Product

admin.site.register(Lekarze)
admin.site.register(Pacjenci)
admin.site.register(Wizyta)
admin.site.register(Zalecenia)
admin.site.register(Cennik)
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','image','imie','nazwisko','cena']
    list_filter=['nazwisko','name','cena']
    list_editable=['cena']
    prepopulated_fields={'slug':('name',)}

@admin.register
class CennikAdmin(admin.ModelAdmin):
    list_display=['imie','nazwisko','name','obrazek','koszt']
    list_filter=['imie','nazwisko','name','koszt']
    list_editable=['koszt']
