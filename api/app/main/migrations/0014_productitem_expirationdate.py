# Generated by Django 4.1.7 on 2023-10-07 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_salesorder_lastbalance_salesorder_lastcost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='expirationDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
