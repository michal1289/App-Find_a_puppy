# Generated by Django 2.1.5 on 2019-01-23 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy', '0003_auto_20190122_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racelist',
            name='activity',
            field=models.CharField(choices=[(1, 'Wymaga małej aktywności'), (2, 'Wymaga przeciętnej aktywności'), (3, 'Wymaga dużej aktywności')], max_length=128),
        ),
        migrations.AlterField(
            model_name='racelist',
            name='care',
            field=models.CharField(choices=[(1, 'Łatwa'), (2, 'Średnia'), (3, 'Trudna')], max_length=128),
        ),
        migrations.AlterField(
            model_name='racelist',
            name='character',
            field=models.CharField(choices=[(1, 'Uległy'), (2, 'Pośredni'), (3, 'Lubi dominować')], max_length=128),
        ),
        migrations.AlterField(
            model_name='racelist',
            name='children',
            field=models.CharField(choices=[(1, 'Może wychowywać się z dzieckiem'), (2, 'Nie polecany dla rodziny z dziećmi')], max_length=128),
        ),
        migrations.AlterField(
            model_name='racelist',
            name='live_in_city',
            field=models.CharField(choices=[(1, 'Nadaje się do mieszkania w bloku'), (2, 'Może mieszkać w bloku z warunkiem możliwości wybiegu'), (3, 'Tylko dom z ogrodem')], max_length=128),
        ),
        migrations.AlterField(
            model_name='racelist',
            name='salary',
            field=models.CharField(choices=[(1, 'Stosunkowo małe'), (2, 'Przeciętne'), (3, 'Duże')], max_length=128),
        ),
        migrations.AlterField(
            model_name='racelist',
            name='save',
            field=models.CharField(choices=[(1, 'Nie nadaje się'), (2, 'Nadaje się warunkowo'), (3, 'Bardzo nadaje się do roli stróża')], max_length=128),
        ),
        migrations.AlterField(
            model_name='racelist',
            name='size',
            field=models.CharField(choices=[(1, 'Mały'), (2, 'Średni'), (3, 'Duży'), (4, 'Bardzo duży')], max_length=128),
        ),
        migrations.AlterField(
            model_name='racelist',
            name='training',
            field=models.CharField(choices=[(1, 'Szybko i chętnie się uczy'), (2, 'Przeciętne zdolności do uczenia')], max_length=128),
        ),
    ]
