# Generated by Django 4.1.5 on 2023-02-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hududlar', '0004_alter_vaqt_ochish_alter_vaqt_yopish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaqt',
            name='sana',
            field=models.DateField(unique=True),
        ),
    ]
