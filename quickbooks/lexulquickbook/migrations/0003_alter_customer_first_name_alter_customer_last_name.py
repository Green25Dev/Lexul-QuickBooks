# Generated by Django 4.1 on 2022-08-20 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lexulquickbook', '0002_alter_customer_options_customer_qbd_object_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]