# Generated by Django 3.1.3 on 2020-11-23 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionapp', '0008_auto_20201123_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_end',
            field=models.DateTimeField(),
        ),
    ]
