# Generated by Django 3.2.6 on 2021-08-21 09:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddOn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('price', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('Time_to_60', models.CharField(max_length=10, null=True)),
                ('base_price', models.IntegerField(default=0, null=True)),
                ('start_range', models.CharField(max_length=20, null=True)),
                ('peak_power', models.CharField(max_length=20, null=True)),
                ('top_speed', models.CharField(max_length=20, null=True)),
                ('weight', models.CharField(max_length=20, null=True)),
                ('cargo_capacity', models.CharField(max_length=20, null=True)),
                ('power_train', models.CharField(max_length=20, null=True)),
                ('acceleration', models.CharField(max_length=20, null=True)),
                ('drag_coefficient', models.CharField(max_length=20, null=True)),
                ('wheels', models.CharField(max_length=20, null=True)),
                ('charging', models.CharField(max_length=20, null=True)),
                ('img_url', models.CharField(max_length=200, null=True)),
                ('add_on', models.ManyToManyField(to='website.AddOn')),
            ],
        ),
        migrations.CreateModel(
            name='CarVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('add_on_price', models.IntegerField(default=0, null=True)),
                ('range', models.CharField(max_length=20, null=True)),
                ('peak_power', models.CharField(max_length=20, null=True)),
                ('top_speed', models.CharField(max_length=20, null=True)),
                ('weight', models.CharField(max_length=20, null=True)),
                ('cargo_capacity', models.CharField(max_length=20, null=True)),
                ('power_train', models.CharField(max_length=20, null=True)),
                ('acceleration', models.CharField(max_length=20, null=True)),
                ('drag_coefficient', models.CharField(max_length=20, null=True)),
                ('wheels', models.CharField(max_length=20, null=True)),
                ('charging', models.CharField(max_length=20, null=True)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.car')),
            ],
        ),
        migrations.CreateModel(
            name='Interior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interior', models.CharField(max_length=20, null=True)),
                ('price', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Paint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(max_length=20, null=True)),
                ('price', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wheel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wheel', models.CharField(max_length=20, null=True)),
                ('price', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('car_variation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.carvariation')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='interior',
            field=models.ManyToManyField(to='website.Interior'),
        ),
        migrations.AddField(
            model_name='car',
            name='paint',
            field=models.ManyToManyField(to='website.Paint'),
        ),
        migrations.AddField(
            model_name='car',
            name='wheel',
            field=models.ManyToManyField(to='website.Wheel'),
        ),
    ]
