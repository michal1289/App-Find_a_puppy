# Generated by Django 2.1.5 on 2019-01-22 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddy', '0002_auto_20190122_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='racelist',
            name='activity',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='racelist',
            name='care',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='racelist',
            name='character',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='racelist',
            name='children',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='racelist',
            name='live_in_city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='racelist',
            name='salary',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='racelist',
            name='save',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='racelist',
            name='size',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='racelist',
            name='training',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
