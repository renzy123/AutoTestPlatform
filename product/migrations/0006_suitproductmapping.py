# Generated by Django 2.0.5 on 2018-10-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('product', '0005_auto_20180914_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuitProductMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.IntegerField()),
                ('suit', models.IntegerField()),
            ],
        ),
    ]