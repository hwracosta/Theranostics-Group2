# Generated by Django 4.2.5 on 2025-01-04 04:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0017_alter_physicalexam_ecog_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalexam',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(1, message='Value cannot be zero or negative.')]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='alkaline_phosphatase',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0, message='Value cannot be negative')]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='bilirubins',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0, message='Value cannot be negative')]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='creatinine',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0, message='Value cannot be negative')]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='hematocrit',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0, message='Value cannot be negative')]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='hemoglobin',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0, message='Value cannot be negative')]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='lactate_hydrogenase',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0, message='Value cannot be negative')]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='platelet',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, message='Value cannot be negative')]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='psa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0, message='Value cannot be negative')]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='rbc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0, message='Value cannot be negative')]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='sgot',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0, message='Value cannot be negative')]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='sgpt',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0, message='Value cannot be negative')]),
        ),
        migrations.AlterField(
            model_name='screening',
            name='wbc',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0, message='Value cannot be negative')]),
        ),
    ]
