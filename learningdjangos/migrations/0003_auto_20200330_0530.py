# Generated by Django 3.0.4 on 2020-03-30 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learningdjangos', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='data_add',
            new_name='date_add',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='data_add',
            new_name='date_add',
        ),
    ]
