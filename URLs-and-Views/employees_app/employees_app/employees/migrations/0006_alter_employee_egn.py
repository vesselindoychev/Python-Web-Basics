# Generated by Django 3.2.18 on 2023-03-15 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_employee_egn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='egn',
            field=models.CharField(max_length=10),
        ),
    ]
