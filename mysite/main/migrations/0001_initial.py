# Generated by Django 4.1.2 on 2022-10-07 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='firm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inn', models.CharField(max_length=20, verbose_name='ИНН')),
                ('ogrn', models.CharField(max_length=20, verbose_name='ОГРН')),
                ('adres', models.CharField(max_length=100, verbose_name='Адрес')),
                ('Name', models.CharField(max_length=100, verbose_name='Наименование')),
            ],
        ),
    ]
