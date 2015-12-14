# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Full_salary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datemonth', models.CharField(max_length=7)),
                ('tsavings', models.FloatField()),
                ('zsavings', models.FloatField()),
                ('base', models.FloatField()),
                ('all_salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('nation', models.CharField(max_length=7)),
                ('sex', models.BooleanField(default=True)),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_name', models.CharField(max_length=10)),
                ('base', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Yewu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('client', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('zhishou', models.BooleanField(default=True)),
                ('money', models.FloatField()),
                ('person', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('checkinDate', models.DateField()),
                ('beizhu', models.CharField(max_length=100)),
                ('username1', models.ForeignKey(to='webapp.Users')),
            ],
        ),
        migrations.AddField(
            model_name='people',
            name='postkey',
            field=models.ForeignKey(to='webapp.Salary'),
        ),
        migrations.AddField(
            model_name='people',
            name='username1',
            field=models.ForeignKey(to='webapp.Users'),
        ),
        migrations.AddField(
            model_name='full_salary',
            name='peopleid',
            field=models.ForeignKey(to='webapp.People'),
        ),
    ]
