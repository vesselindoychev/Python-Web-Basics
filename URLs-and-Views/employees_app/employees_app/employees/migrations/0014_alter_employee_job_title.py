# Generated by Django 3.2.18 on 2023-03-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0013_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.CharField(choices=[('Software Developer', 'Software Developer'), ('QA Engineer', 'QA Engineer'), ('Marketing Specialist', 'Marketing Specialist')], max_length=20),
        ),
    ]
