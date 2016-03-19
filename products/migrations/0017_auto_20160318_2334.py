# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import products.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0016_auto_20160224_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(null=True, blank=True)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='media',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/Users/NESCODE/project/githubsunil/djangodm/static_cdn/protected'), null=True, upload_to=products.models.download_media_location, blank=True),
        ),
        migrations.AddField(
            model_name='productrating',
            name='product',
            field=models.ForeignKey(to='products.Product'),
        ),
        migrations.AddField(
            model_name='productrating',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
