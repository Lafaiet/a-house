# Generated by Django 3.1.3 on 2020-11-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionapp', '0004_auto_20201121_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='auction_end',
            field=models.DateTimeField(),
        ),
    ]
