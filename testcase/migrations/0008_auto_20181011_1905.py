# Generated by Django 2.0.5 on 2018-10-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('testcase', '0007_auto_20180930_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suitcasemapping',
            name='desc',
        ),
        migrations.AddField(
            model_name='testsuite',
            name='last_edit_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='testsuite',
            name='last_editer',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='testsuite',
            name='last_run_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='testsuite',
            name='run_count',
            field=models.IntegerField(default=0),
        ),
    ]
