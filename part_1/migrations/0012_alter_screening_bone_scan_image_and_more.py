# Generated by Django 4.2.3 on 2023-08-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part_1', '0011_alter_screening_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screening',
            name='bone_scan_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='fdgpetct_img',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='gapsma_img',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='renal_scintigraphy',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='screening',
            name='salivary_gland_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
