# Generated by Django 4.1.5 on 2023-02-25 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hududlar', '0008_videocategory_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocategory',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
