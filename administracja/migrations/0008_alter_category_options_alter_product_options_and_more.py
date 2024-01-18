# Generated by Django 5.0 on 2024-01-17 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracja', '0007_category_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='specjalizacja',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='specjalizacja',
            new_name='name',
        ),
    ]
