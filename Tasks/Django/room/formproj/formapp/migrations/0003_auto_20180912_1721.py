# Generated by Django 2.1.1 on 2018-09-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0002_company_form_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_form',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]
