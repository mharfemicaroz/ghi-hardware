# Generated by Django 4.1.7 on 2023-09-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_productitem_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='name',
            field=models.CharField(default='', max_length=256, unique=True),
            preserve_default=False,
        ),
    ]
