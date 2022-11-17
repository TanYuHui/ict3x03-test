from django.db import models


# Database schemas.
# note all id is created as pk

class Roles(models.Model):
    permissions = models.CharField(max_length=20)
    role_desc = models.CharField(max_length=20)


class Users(models.Model):
    role_id = models.ForeignKey(
        "Roles", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=15)
    allergies = models.CharField(max_length=1000)


class Credit_Details(models.Model):
    role_id = models.ForeignKey(
        "Roles", on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        "Users", on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20)
    provider = models.CharField(max_length=50)
    account_no = models.IntegerField(null=True)
    expiry = models.DateField(null=True)


class Product_Category(models.Model):
    category_name = models.CharField(max_length=20)


class Product_Details(models.Model):
    category_id = models.ForeignKey(
        "Product_Category", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    image = models.TextField(null=True)
    ingredients = models.CharField(max_length=1000)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    stock_available = models.IntegerField(null=True)


class Promotion(models.Model):
    product_id = models.ForeignKey(
        "Product_Details", on_delete=models.CASCADE)
    promotion_amount = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)


class Cart(models.Model):
    product_id = models.ForeignKey(
        "Product_Details", on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        "Users", on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    total_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)


class Payment_Details(models.Model):
    total_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    provider = models.CharField(max_length=50)
    card_digits = models.CharField(max_length=4)
    payment_status = models.CharField(max_length=50)


class Orders(models.Model):
    cart_id = models.ForeignKey(
        "Cart", on_delete=models.CASCADE)
    payment_id = models.ForeignKey(
        "Payment_Details", on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    total_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    order_status = models.CharField(max_length=50)
