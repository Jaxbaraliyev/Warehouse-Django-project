# Generated by Django 4.1.2 on 2023-02-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statsapp', '0002_alter_stats_sana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stats',
            name='sana',
            field=models.DateField(),
        ),
    ]
