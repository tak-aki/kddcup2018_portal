# Generated by Django 2.0.4 on 2018-04-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit', '0004_submitmodel_for_score_simulation'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoremodel',
            name='bj_o3_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scoremodel',
            name='bj_pm10_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scoremodel',
            name='bj_pm25_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scoremodel',
            name='ld_pm10_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scoremodel',
            name='ld_pm25_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
