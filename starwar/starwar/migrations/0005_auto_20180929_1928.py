# Generated by Django 2.1.1 on 2018-09-29 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('starwar', '0004_userfilm_userplanet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfilm',
            old_name='film_id',
            new_name='film',
        ),
        migrations.RenameField(
            model_name='userfilm',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='userplanet',
            old_name='planet_id',
            new_name='planet',
        ),
        migrations.RenameField(
            model_name='userplanet',
            old_name='user_id',
            new_name='user',
        ),
    ]
