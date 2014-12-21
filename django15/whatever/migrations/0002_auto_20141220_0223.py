# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whatever', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whatever',
            name='body',
        ),
        migrations.RemoveField(
            model_name='whatever',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='whatever',
            name='title',
        ),
        migrations.AddField(
            model_name='whatever',
            name='BloqCanalJSuper',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='BloqCanalJumbo',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='BloqCanalSisa',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='FechBloqCanalJSuper',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='FechBloqCanalJumbo',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='FechBloqCanalSisa',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='articulo',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='cmed08_gr',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='cmed09_me',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='cmed10_pe',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='cmed22_mini',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='cpal11_me',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='cpal12_pe',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='cpal23_mini',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='cpba13_me',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='cpba14_pe',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='cpba24_mini',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='descripcion',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='ean',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='emer18_gr',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='emer19_me',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='emer20_pe',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='emer26_mini',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='fechBloqBasico',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='ful01a',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='ful02b',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='marca',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='meg03a',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='meg04b',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='mixt15_gr',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='mixt16_me',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='mixt17_pe',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='mixt25_mini',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='pref05_gr',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='pref06_me',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='pref07_pe',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='pref21_mini',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='whatever',
            name='vigencia',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
    ]
