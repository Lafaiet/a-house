# Generated by Django 3.1.3 on 2020-11-23 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionapp', '0007_auto_20201122_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_end',
            field=models.DateTimeField(choices=[(datetime.datetime(2020, 11, 24, 12, 15, 58, 810535), '1 day'), (datetime.datetime(2020, 11, 26, 12, 15, 58, 810535), '3 days'), (datetime.datetime(2020, 11, 30, 12, 15, 58, 810535), '7 days')]),
        ),
    ]
