# Generated by Django 4.1.7 on 2023-09-27 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleSupplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('code', models.CharField(max_length=64, unique=True)),
                ('desc', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(blank=True, max_length=64, null=True)),
                ('phone', models.CharField(blank=True, max_length=64, null=True)),
                ('address', models.CharField(blank=True, max_length=256, null=True)),
                ('author', models.CharField(blank=True, max_length=64, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
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
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('code', models.CharField(max_length=64, unique=True)),
                ('desc', models.CharField(blank=True, max_length=256, null=True)),
                ('author', models.CharField(blank=True, max_length=64, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, unique=True)),
                ('unit', models.CharField(max_length=64)),
                ('sku', models.CharField(max_length=256, unique=True)),
                ('minqty', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qty', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desc', models.CharField(blank=True, max_length=256, null=True)),
                ('tax', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(max_length=64)),
                ('author', models.CharField(blank=True, max_length=64, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.productbrand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('refno', models.CharField(max_length=256, unique=True)),
                ('progressStatus', models.CharField(max_length=64)),
                ('paidStatus', models.CharField(max_length=64)),
                ('desc', models.CharField(blank=True, max_length=256, null=True)),
                ('author', models.CharField(blank=True, max_length=64, null=True)),
                ('discountPercent', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('taxPercent', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('tax', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('totalCost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('totalBalance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('totalPaid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.peoplesupplier')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseTransaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('amountPaid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(max_length=64)),
                ('purchaseOrder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.purchaseorder')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseItems',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('purchasePrice', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('qty', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('discountPercent', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('taxPercent', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('tax', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('totalCost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productitem')),
                ('purchaseOrder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.purchaseorder')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSubCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('code', models.CharField(max_length=64, unique=True)),
                ('desc', models.CharField(blank=True, max_length=256, null=True)),
                ('author', models.CharField(blank=True, max_length=64, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productcategory')),
            ],
        ),
        migrations.AddField(
            model_name='productitem',
            name='subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.productsubcategory'),
        ),
    ]
