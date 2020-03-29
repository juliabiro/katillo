# Generated by Django 2.2.11 on 2020-03-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20200329_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hatas',
            old_name='korosztaly',
            new_name='celcsoport',
        ),
        migrations.RemoveField(
            model_name='olaj',
            name='cave',
        ),
        migrations.AddField(
            model_name='hozzavalo',
            name='cseppszam',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hozzavalo',
            name='mertekegyseg',
            field=models.CharField(choices=[('1', 'ml'), ('2', 'g')], default='1', max_length=2),
        ),
        migrations.AddField(
            model_name='hozzavalo',
            name='tipus',
            field=models.CharField(choices=[('1', 'Növényi Olaj'), ('2', 'Hidralátum'), ('3', 'Kometikai alapanyag'), ('4', '')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='olaj',
            name='jegy',
            field=models.CharField(blank=True, choices=[('1', 'FEJJEGY'), ('2', 'SZIVJEGY'), ('3', 'Alapillat')], max_length=2),
        ),
        migrations.AlterField(
            model_name='olaj',
            name='kep',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name='Kontraindikacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=200)),
                ('olaj', models.ForeignKey(on_delete=None, to='book.Olaj')),
            ],
            options={
                'verbose_name': 'Kontraindikáció',
                'verbose_name_plural': 'Kontraindikációk',
            },
        ),
    ]