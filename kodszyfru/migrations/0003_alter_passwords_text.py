# Generated by Django 3.2.8 on 2021-10-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kodszyfru', '0002_passwords_cipher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwords',
            name='text',
            field=models.TextField(max_length=2000),
        ),
    ]