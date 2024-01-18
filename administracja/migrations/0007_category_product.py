# Generated by Django 5.0 on 2024-01-16 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracja', '0006_cennik'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specjalizacja', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('specjalizacja',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField(blank=True, null=True)),
                ('specjalizacja', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products')),
                ('imie', models.TextField(blank=True, null=True)),
                ('nazwisko', models.TextField(blank=True, null=True)),
                ('cena', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ('specjalizacja',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]