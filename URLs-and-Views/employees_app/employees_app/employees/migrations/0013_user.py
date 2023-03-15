# Generated by Django 3.2.18 on 2023-03-15 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0012_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='employees.employee')),
            ],
        ),
    ]
