# Generated by Django 3.0.7 on 2020-06-20 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hopital', '0002_auto_20200620_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
