# Generated by Django 2.1.5 on 2019-01-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy', '0005_auto_20190123_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='activity',
            field=models.IntegerField(choices=[(1, ''), (2, 'Wymaga małej aktywności'), (3, 'Wymaga przeciętnej aktywności'), (4, 'Wymaga dużej aktywności')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='care',
            field=models.IntegerField(choices=[(1, ''), (2, 'Łatwa'), (3, 'Średnia'), (4, 'Trudna')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='character',
            field=models.IntegerField(choices=[(1, ''), (2, 'Uległy'), (3, 'Pośredni'), (4, 'Lubi dominować')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='children',
            field=models.IntegerField(choices=[(1, ''), (2, 'Może wychowywać się z dzieckiem'), (3, 'Nie polecany dla rodziny z dziećmi')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='live_in_city',
            field=models.IntegerField(choices=[(1, ''), (2, 'Nadaje się do mieszkania w bloku'), (3, 'Może mieszkać w bloku z warunkiem możliwości wybiegu'), (4, 'Tylko dom z ogrodem')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='salary',
            field=models.IntegerField(choices=[(1, ''), (2, 'Stosunkowo małe'), (3, 'Przeciętne'), (4, 'Duże')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='save',
            field=models.IntegerField(choices=[(1, ''), (2, 'Nie nadaje się'), (3, 'Nadaje się warunkowo'), (4, 'Bardzo nadaje się do roli stróża')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='size',
            field=models.IntegerField(choices=[(1, ''), (2, 'Mały'), (3, 'Średni'), (4, 'Duży'), (5, 'Bardzo duży')]),
        ),
        migrations.AlterField(
            model_name='race',
            name='training',
            field=models.IntegerField(choices=[(1, ''), (2, 'Szybko i chętnie się uczy'), (3, 'Przeciętne zdolności do uczenia')]),
        ),
    ]
