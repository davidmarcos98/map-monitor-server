# Generated by Django 4.1.5 on 2023-06-02 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getrecords', '0011_challenge_cotdqualitimes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='uid',
            field=models.CharField(db_index=True, max_length=64, unique=True),
        ),
    ]
