# Generated by Django 3.2.18 on 2023-03-15 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_alter_employee_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='egn',
            field=models.CharField(default='', max_length=10, unique=False),
            preserve_default=False,
        ),
    ]
