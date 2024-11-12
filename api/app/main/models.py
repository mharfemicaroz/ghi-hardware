from django.db import models


class ProductCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    code = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    author = models.CharField(max_length=64, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class ProductSubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    code = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    author = models.CharField(max_length=64, null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class ProductBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    author = models.CharField(max_length=64, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class PeopleSupplier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    code = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    author = models.CharField(max_length=64, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class PeopleCustomer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    code = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    email = models.CharField(max_length=64, null=True, blank=True)
    phone = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    author = models.CharField(max_length=64, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class ProductVoucher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    mode = models.CharField(max_length=64)
    discountPercentage = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    specialPrice = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    startDate = models.DateTimeField(blank=True, null=True)
    expirationDate = models.DateTimeField(blank=True, null=True)
    author = models.CharField(max_length=64, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class ProductItem(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(
        ProductSubCategory, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(
        ProductBrand, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=64, unique=True)
    unit = models.CharField(max_length=64)
    sku = models.CharField(max_length=128, unique=True)
    minqty = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=256, null=True, blank=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=64)
    author = models.CharField(max_length=64, null=True, blank=True)
    expirationDate = models.DateTimeField(null=True, blank=True)
    manufacturingDate = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    isRecentPurchased = models.BooleanField(default=False)


class ProductVoucherItem(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    voucher = models.ForeignKey(ProductVoucher, on_delete=models.CASCADE)
    author = models.CharField(max_length=64, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class PurchaseOrder(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    purchaseDate = models.DateTimeField(blank=True, null=True)
    refno = models.CharField(max_length=64, unique=True)
    supplier = models.ForeignKey(
        PeopleSupplier, on_delete=models.CASCADE, null=True, blank=True)
    progressStatus = models.CharField(max_length=64)
    paidStatus = models.CharField(max_length=64)
    description = models.CharField(max_length=256, null=True, blank=True)
    author = models.CharField(max_length=64, null=True, blank=True)
    discountPercent = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    taxPercent = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    shippingCost = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    lastCost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    totalPaid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    lastBalance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)


class SalesOrder(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    salesDate = models.DateTimeField(blank=True, null=True)
    refno = models.CharField(max_length=64, unique=True)
    customer = models.ForeignKey(
        PeopleCustomer, on_delete=models.CASCADE, null=True, blank=True)
    progressStatus = models.CharField(max_length=64)
    paidStatus = models.CharField(max_length=64)
    description = models.CharField(max_length=256, null=True, blank=True)
    author = models.CharField(max_length=64, null=True, blank=True)
    discountPercent = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    taxPercent = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    shippingCost = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    lastCost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    totalPaid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    lastBalance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)


class PurchaseItems(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    purchaseOrder = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sellingPrice = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discountPercent = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    taxPercent = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    totalCost = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class SalesItems(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    salesOrder = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    qty = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discountPercent = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    taxPercent = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    totalCost = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class PurchaseTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    purchaseOrder = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amountPaid = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=64)
    refno = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)


class SalesTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    salesOrder = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    amountPaid = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=64)
    refno = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=256, null=True, blank=True)
