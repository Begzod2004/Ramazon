# Generated by Django 4.1.5 on 2023-03-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hududlar', '0011_remove_namozvaqti_hudud_namozvaqti_viloyat'),
    ]

    operations = [
        migrations.AddField(
            model_name='hududlar',
            name='hudud_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]