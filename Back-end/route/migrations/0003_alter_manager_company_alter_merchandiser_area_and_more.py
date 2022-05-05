# Generated by Django 4.0.3 on 2022-05-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0002_rename_manager_manager_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='merchandiser',
            name='area',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='merchandiser',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
