# Generated by Django 4.1.5 on 2023-02-11 03:43

from django.db import migrations, models
import django.db.models.deletion
import time


class Migration(migrations.Migration):

    dependencies = [
        ('mapalitics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wsid', models.CharField(db_index=True, max_length=64, unique=True)),
                ('display_name', models.CharField(db_index=True, max_length=128)),
                ('created_ts', models.IntegerField(default=time.time, verbose_name='created timestamp')),
            ],
        ),
        migrations.AddField(
            model_name='mapaliticstoken',
            name='created_ts',
            field=models.IntegerField(default=time.time, verbose_name='created timestamp'),
        ),
        migrations.CreateModel(
            name='TrackEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(db_index=True, max_length=64)),
                ('created_ts', models.IntegerField(default=time.time, verbose_name='created timestamp')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mapalitics.user')),
            ],
        ),
        migrations.AddField(
            model_name='mapaliticstoken',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='mapalitics.user'),
        ),
    ]
