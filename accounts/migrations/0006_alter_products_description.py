# Generated by Django 3.2.5 on 2021-12-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20211207_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
