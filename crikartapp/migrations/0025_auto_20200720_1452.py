# Generated by Django 3.0.3 on 2020-07-20 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crikartapp', '0024_auto_20200720_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_register',
            name='team_logo',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
