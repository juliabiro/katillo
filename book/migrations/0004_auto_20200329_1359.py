# Generated by Django 2.2.11 on 2020-03-29 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20200328_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forgalmazas',
            options={'verbose_name': 'Termék', 'verbose_name_plural': 'Termékek'},
        ),
        migrations.AlterModelOptions(
            name='forgalmazo',
            options={'verbose_name': 'Cég', 'verbose_name_plural': 'Cégek'},
        ),
        migrations.AlterModelOptions(
            name='olaj',
            options={'verbose_name': 'Összetevő', 'verbose_name_plural': 'Összetevők'},
        ),
        migrations.RenameField(
            model_name='olaj',
            old_name='name',
            new_name='magyar_nev',
        ),
        migrations.AddField(
            model_name='olaj',
            name='cave',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='olaj',
            name='fajsuj',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='olaj',
            name='jegy',
            field=models.CharField(blank=True, choices=[('1', 'FEJJEGY'), ('2', 'SZIVJEGY')], max_length=2),
        ),
        migrations.AddField(
            model_name='olaj',
            name='latin_nev',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='olaj',
            name='tipus',
            field=models.CharField(choices=[('1', 'Növényi Olaj'), ('2', 'Hidralátum'), ('3', 'Kometikai alapanyag'), ('4', '')], default='1', max_length=2),
        ),
        migrations.AddField(
            model_name='recept',
            name='tipus',
            field=models.CharField(choices=[('1', 'Kozmetikum'), ('2', 'Aromaterápia')], default='2', max_length=2),
        ),
        migrations.AlterField(
            model_name='hatas',
            name='korosztaly',
            field=models.CharField(choices=[('1', '1-3'), ('2', '3-6'), ('3', '6-12'), ('4', 'felnőtt'), ('5', 'váarndós')], default='4', max_length=2),
        ),
    ]
