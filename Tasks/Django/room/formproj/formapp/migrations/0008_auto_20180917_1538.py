# Generated by Django 2.1.1 on 2018-09-17 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formapp', '0007_auto_20180917_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company_form',
            old_name='adddress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='company_form',
            old_name='citsy',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='company_form',
            old_name='discrsiption',
            new_name='discription',
        ),
        migrations.RenameField(
            model_name='company_form',
            old_name='emaisl',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='company_form',
            old_name='passsword',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='company_form',
            old_name='pname',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='company_form',
            old_name='pincsode',
            new_name='pincode',
        ),
        migrations.RenameField(
            model_name='company_form',
            old_name='tditle',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='company_form',
            old_name='ursl',
            new_name='url',
        ),
    ]
