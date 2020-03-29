# Generated by Django 2.2.11 on 2020-03-29 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_auto_20200329_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forgalmazas',
            name='ceg',
            field=models.ForeignKey(on_delete=None, to='book.Forgalmazo', verbose_name='Cég'),
        ),
        migrations.AlterField(
            model_name='forgalmazas',
            name='cseppszam',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cseppszám'),
        ),
        migrations.AlterField(
            model_name='forgalmazas',
            name='kiszereles',
            field=models.CharField(max_length=200, verbose_name='Kiszerelés'),
        ),
        migrations.AlterField(
            model_name='forgalmazas',
            name='olaj',
            field=models.ForeignKey(on_delete=None, to='book.Olaj', verbose_name='Összetevő'),
        ),
        migrations.AlterField(
            model_name='forgalmazas',
            name='termeknev',
            field=models.CharField(blank=True, max_length=200, verbose_name='Terméknév'),
        ),
        migrations.AlterField(
            model_name='forgalmazas',
            name='tipus',
            field=models.CharField(choices=[('1', 'Növényi Olaj'), ('2', 'Hidralátum'), ('3', 'Kometikai alapanyag'), ('4', '')], default='1', max_length=2, verbose_name='Típus'),
        ),
    ]