# Generated by Django 4.0.3 on 2023-01-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('k8s', '0006_projectresource_envs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectresource',
            name='envs',
        ),
        migrations.AddField(
            model_name='projectenv',
            name='envs',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projectenv',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='projectenv',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
    ]
