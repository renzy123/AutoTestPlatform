# Generated by Django 2.1.2 on 2018-10-06 13:34

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
