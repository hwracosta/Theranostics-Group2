# Generated by Django 4.2.3 on 2023-08-25 03:26

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0007_remove_physicalexam_slug_alter_physicalexam_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='physicalexam',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from='id', unique=True),
        ),
    ]
