# Generated by Django 5.0 on 2023-12-30 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracja', '0002_delete_lekarze'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lekarze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numer_lek', models.IntegerField(blank=True, null=True)),
                ('imie', models.TextField(blank=True, null=True)),
                ('nazwisko', models.TextField(blank=True, null=True)),
                ('specjalizacja', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lekarze',
                'managed': False,
            },
        ),
    ]