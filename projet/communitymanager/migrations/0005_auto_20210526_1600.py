# Generated by Django 3.2.3 on 2021-05-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communitymanager', '0004_auto_20210525_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communaute',
            name='nom',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='titre',
            field=models.CharField(max_length=150),
        ),
    ]
