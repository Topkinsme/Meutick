# Generated by Django 5.1.1 on 2024-09-08 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_alter_adminuser_userid_alter_categories_cat_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='id',
        ),
        migrations.AddField(
            model_name='ticket',
            name='tic_id',
            field=models.CharField(default='00000', max_length=5, primary_key=True, serialize=False),
        ),
    ]
