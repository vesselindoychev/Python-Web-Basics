# Generated by Django 3.2.18 on 2023-03-23 15:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0015_auto_20230315_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='employee',
            name='egn',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='EGN'),
        ),
    ]
