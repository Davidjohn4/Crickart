# Generated by Django 3.0.3 on 2020-08-20 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crikartapp', '0026_auto_20200720_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_register',
            name='team_logo',
            field=models.ImageField(default='', upload_to='upload/'),
        ),
    ]
