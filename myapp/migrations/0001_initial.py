# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-03-05 03:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_plate', models.CharField(max_length=8)),
                ('seats', models.IntegerField()),
                ('model', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='BusCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('image', models.CharField(max_length=400)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=400)),
                ('longitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=400)),
                ('longitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('longitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('valid', models.BooleanField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('price', models.IntegerField()),
                ('arrival', models.TimeField()),
                ('departure', models.TimeField()),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Bus')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='myapp.Location')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='myapp.Location')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Route'),
        ),
        migrations.AddField(
            model_name='bus',
            name='bus_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.BusCompany'),
        ),
    ]
