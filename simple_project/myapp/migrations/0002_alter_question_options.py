# Generated by Django 4.0.1 on 2022-01-20 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('-pub_date',)},
        ),
    ]
