# Generated by Django 4.1.7 on 2023-09-01 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_productcategory_subcategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('desc', models.CharField(blank=True, max_length=256, null=True)),
                ('author', models.CharField(blank=True, max_length=64, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='image_filename',
        ),
    ]