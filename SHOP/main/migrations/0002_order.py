# Generated by Django 4.0.4 on 2023-05-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название товара')),
                ('surname', models.CharField(max_length=200, verbose_name='Название товара')),
                ('email', models.CharField(max_length=200, verbose_name='Название товара')),
                ('phone', models.CharField(max_length=200, verbose_name='Название товара')),
                ('basket', models.TextField(verbose_name='Название товара')),
            ],
        ),
    ]
