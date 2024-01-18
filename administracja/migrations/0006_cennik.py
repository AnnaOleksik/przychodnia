# Generated by Django 5.0 on 2024-01-08 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracja', '0005_wizyta_zalecenia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cennik',
            fields=[
                ('imie', models.TextField(blank=True, null=True)),
                ('nazwisko', models.TextField(blank=True, null=True)),
                ('specjalizacja', models.TextField(blank=True, null=True)),
                ('koszt', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'cennik',
                'managed': False,
            },
        ),
    ]