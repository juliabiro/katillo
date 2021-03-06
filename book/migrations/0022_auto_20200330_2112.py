# Generated by Django 2.2.11 on 2020-03-30 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0021_auto_20200330_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forgalmazas',
            name='mertekegyseg',
            field=models.CharField(choices=[('ml', 'ml'), ('g', 'g'), ('csepp', 'csepp')], default='1', max_length=40, verbose_name='Mértékegység'),
        ),
        migrations.AlterField(
            model_name='forgalmazas',
            name='tipus',
            field=models.CharField(choices=[('Növényi Olaj', 'Növényi Olaj'), ('Hidralátum', 'Hidralátum'), ('Kometikai alapanyag', 'Kometikai alapanyag'), ('', '')], default='1', max_length=40, verbose_name='Típus'),
        ),
    ]
