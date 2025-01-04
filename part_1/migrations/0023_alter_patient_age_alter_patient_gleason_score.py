# Generated by Django 4.2.5 on 2025-01-04 12:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0022_alter_screening_fdgpetct_bone_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, message='Value cannot be negative.')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gleason_score',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(6, message='Value should be 6-10.'), django.core.validators.MaxValueValidator(10, message='Value should be 6-10.')]),
        ),
    ]
