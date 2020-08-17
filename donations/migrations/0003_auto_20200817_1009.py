# Generated by Django 3.0.8 on 2020-08-17 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_auto_20200817_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='organization',
            field=models.CharField(blank=True, choices=[('COVID-19', 'COVID-19'), ('MAKEDONIA', 'MAKEDONIA'), ('SELE ENAT CHARITABLE', 'SELE ENAT CHARITABLE'), ('ETHIOPIAN CENTER FOR DISABILITY AND DEVLOPMENT', 'ETHIOPIAN CENTER FOR DISABILITY AND DEVLOPMENT')], max_length=300, null=True, verbose_name='organization'),
        ),
    ]
