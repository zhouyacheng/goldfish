# Generated by Django 4.0.3 on 2023-01-09 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('delete_time', models.DateTimeField(default=None, null=True, verbose_name='删除时间')),
                ('host', models.CharField(max_length=128)),
                ('ip', models.CharField(max_length=128)),
                ('ok', models.IntegerField(default=0)),
                ('dark', models.IntegerField(default=0)),
                ('failures', models.IntegerField(default=0)),
                ('changed', models.IntegerField(default=0)),
                ('ignored', models.IntegerField(default=0)),
                ('processed', models.IntegerField(default=0)),
                ('rescued', models.IntegerField(default=0)),
                ('skipped', models.IntegerField(default=0)),
                ('artifact_data', models.CharField(blank=True, max_length=1024, null=True)),
                ('task', models.ForeignKey(db_column='task_id', on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='iac.task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
