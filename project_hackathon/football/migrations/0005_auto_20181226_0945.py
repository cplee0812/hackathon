# Generated by Django 2.1.1 on 2018-12-26 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0004_auto_20181223_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='duration1',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='match',
            name='duration2',
            field=models.IntegerField(default=50),
        ),
        migrations.AlterField(
            model_name='match',
            name='starttime1',
            field=models.TimeField(help_text="Format:'HH:MM'"),
        ),
        migrations.AlterField(
            model_name='match',
            name='starttime2',
            field=models.TimeField(help_text="Format:'HH:MM'"),
        ),
        migrations.AlterField(
            model_name='matchstat',
            name='away_score',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='matchstat',
            name='host_score',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]