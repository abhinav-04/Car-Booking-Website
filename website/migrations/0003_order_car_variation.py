# Generated by Django 3.2.6 on 2021-08-21 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_remove_order_car_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='car_variation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.carvariation'),
        ),
    ]
