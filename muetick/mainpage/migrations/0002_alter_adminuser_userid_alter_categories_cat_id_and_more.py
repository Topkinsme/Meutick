# Generated by Django 5.1.1 on 2024-09-08 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='userid',
            field=models.CharField(default='00000', max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categories',
            name='cat_id',
            field=models.CharField(default='00000', max_length=5, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='cus_id',
            field=models.CharField(default='00000', max_length=5, primary_key=True, serialize=False),
        ),
    ]
