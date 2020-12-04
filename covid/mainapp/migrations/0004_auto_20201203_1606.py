# Generated by Django 3.0.1 on 2020-12-03 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20201203_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='approvedAgainstDiseases',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='diseaseMeshId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='mechanismOfAction',
            field=models.CharField(blank=True, max_length=3000, null=True),
        ),
    ]
