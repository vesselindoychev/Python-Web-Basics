# Generated by Django 3.2.18 on 2023-03-29 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.URLField()),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
