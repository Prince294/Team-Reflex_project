# Generated by Django 3.1.3 on 2020-11-07 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0004_auto_20201107_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='Email',
            field=models.CharField(max_length=100),
        ),
    ]
