# Generated by Django 4.1.5 on 2023-02-22 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hududlar', '0005_alter_vaqt_sana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaqt',
            name='sana',
            field=models.DateField(),
        ),
    ]
