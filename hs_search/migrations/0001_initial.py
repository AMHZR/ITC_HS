# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.IntegerField()),
                ('heading', models.CharField(max_length=1000)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chapter_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=300, verbose_name=b'Chapter Name')),
            ],
        ),
        migrations.CreateModel(
            name='hscode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hs', models.CharField(max_length=20, verbose_name=b'HS-CODE')),
                ('desc', models.TextField(verbose_name=b'HSCODE description')),
                ('wef', models.DateField(auto_now=True, verbose_name=b'W.E.F')),
                ('policy', models.CharField(max_length=30, verbose_name=b'Policy Restriction')),
                ('hs_5', models.CharField(max_length=800, blank=True)),
                ('hs_6', models.CharField(max_length=800, blank=True)),
                ('hs_8', models.CharField(max_length=1000, blank=True)),
                ('condition', models.CharField(max_length=1000, blank=True)),
                ('article', models.ForeignKey(to='hs_search.Article')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note_id', models.CharField(max_length=10)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_id', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=300, verbose_name=b'Section Name')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('desc', models.TextField(max_length=1000)),
                ('cat', models.ForeignKey(to='hs_search.Category')),
            ],
        ),
        migrations.AddField(
            model_name='hscode',
            name='note',
            field=models.ManyToManyField(to='hs_search.Note', blank=True),
        ),
        migrations.AddField(
            model_name='chapter',
            name='notes',
            field=models.ManyToManyField(to='hs_search.Note', blank=True),
        ),
        migrations.AddField(
            model_name='chapter',
            name='section',
            field=models.ForeignKey(to='hs_search.Section'),
        ),
        migrations.AddField(
            model_name='article',
            name='chapter',
            field=models.ForeignKey(to='hs_search.Chapter'),
        ),
    ]
