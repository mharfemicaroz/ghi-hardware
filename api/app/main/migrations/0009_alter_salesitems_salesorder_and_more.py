# Generated by Django 4.1.7 on 2023-10-02 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_peoplecustomer_salestransaction_salesorder_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesitems',
            name='salesOrder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.salesorder'),
        ),
        migrations.AlterField(
            model_name='salestransaction',
            name='salesOrder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.salesorder'),
        ),
    ]
