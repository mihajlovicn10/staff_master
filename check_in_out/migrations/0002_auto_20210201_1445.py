# Generated by Django 3.1.5 on 2021-02-01 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_remove_users_position'),
        ('check_in_out', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkinout',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.users'),
        ),
        migrations.AlterField(
            model_name='checkinout',
            name='check_out',
            field=models.DateTimeField(null=True),
        ),
    ]
