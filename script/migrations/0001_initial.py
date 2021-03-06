# Generated by Django 2.1.1 on 2018-09-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=255, null=True)),
                ('path', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('create_user', models.IntegerField()),
                ('run_count', models.IntegerField()),
                ('last_run_time', models.DateTimeField()),
                ('related_case', models.IntegerField(null=True)),
                ('last_edit_time', models.DateTimeField(auto_now=True)),
                ('last_edit_user', models.IntegerField()),
                ('script_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ScriptType',
            fields=[
                ('desc', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=20)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
