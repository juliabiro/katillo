# Generated by Django 2.2.11 on 2020-03-30 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0019_auto_20200330_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hatas',
            name='celcsoport',
            field=models.CharField(choices=[('1-3', '1-3'), ('3-6', '3-6'), ('6-12', '6-12'), ('felnőtt', 'felnőtt'), ('várandós', 'várandós')], default='4', max_length=20, verbose_name='Célcsoport'),
        ),
        migrations.AlterField(
            model_name='olaj',
            name='fajsuj',
            field=models.FloatField(blank=True, null=True, verbose_name='Fajsúly'),
        ),
        migrations.AlterField(
            model_name='olaj',
            name='jegy',
            field=models.CharField(blank=True, choices=[('FEJJEGY', 'FEJJEGY'), ('SZÍVJEGY', 'SZIVJEGY'), ('Alapillat', 'Alapillat')], max_length=10),
        ),
    ]
