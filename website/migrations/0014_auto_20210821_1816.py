# Generated by Django 3.2.6 on 2021-08-21 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_delete_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='placeorder',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='placeorder',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
