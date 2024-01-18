from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your models here.
class Lekarze(models.Model):
    numer_lek = models.IntegerField(primary_key=True)
    imie = models.TextField(blank=True, null=True)
    nazwisko = models.TextField(blank=True, null=True)
    specjalizacja = models.TextField(blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'lekarze'

class Pacjenci(models.Model):
    numer_pac = models.IntegerField(primary_key=True)
    imie = models.TextField(blank=True, null=True)
    nazwisko = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pacjenci'


class Wizyta(models.Model):
    numer_pacjenta = models.IntegerField(blank=True, null=True)
    numer_lekarza = models.IntegerField(blank=True, null=True)
    data_wizyty = models.TextField(primary_key=True)
    koszt = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wizyta'

class Zalecenia(models.Model):
    numer_pacjenta = models.IntegerField(blank=True, null=True)
    numer_lekarza = models.IntegerField(blank=True, null=True)
    data_wizyty = models.TextField(primary_key=True)
    koszt = models.IntegerField(blank=True, null=True)
    recepta = models.IntegerField(blank=True, null=True)
    szczegol = models.TextField(blank=True, null=True)
    badania = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zalecenia'


class Cennik(models.Model):
    imie = models.TextField(blank=True, null=True)
    nazwisko = models.TextField(blank=True, null=True)
    specjalizacja = models.TextField(blank=True, null=True)
    obrazek = models.ImageField(upload_to='administracja/pic/',blank=True)
    koszt = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cennik'
class Category(models.Model):
    name = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=200,db_index=True,unique=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('administracja:product_list_by_category',
                       args=[self.slug])
        
class Product(models.Model):
    category = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=200,db_index=True)
    image = models.ImageField(upload_to="products",blank=True)
    imie = models.TextField(blank=True, null=True)
    nazwisko = models.TextField(blank=True, null=True)
    cena = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)
    def __str__(self):
        return self.name
		
    def get_absolute_url(self):
        return reverse('administracja:product_detail',
                       args=[self.id, self.slug])


