# Generated by Django 3.2.18 on 2023-03-29 14:37

from django.db import migrations, models
import expenses_tracker.main.custom_validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profiles/', validators=[expenses_tracker.main.custom_validators.MaxFileSizeInMbValidator(5)]),
        ),
    ]
