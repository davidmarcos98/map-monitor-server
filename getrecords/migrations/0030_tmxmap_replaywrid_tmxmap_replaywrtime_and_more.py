# Generated by Django 4.2.2 on 2023-07-13 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getrecords', '0029_alter_tmxmapat_authortimebeaten_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tmxmap',
            name='ReplayWRID',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tmxmap',
            name='ReplayWRTime',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tmxmap',
            name='ReplayWRUserID',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tmxmap',
            name='ReplayWRUsername',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
