# Generated by Django 4.1.5 on 2023-02-20 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hududlar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaqt',
            name='hudud',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hududlar.hududlar'),
        ),
    ]
