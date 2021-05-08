from django.db import models
from django.db.models.signals import post_delete, pre_delete
from django.dispatch import receiver
from django.utils import timezone


class SliderImages(models.Model):
    image = models.ImageField(upload_to="images/")

    class Meta:
        verbose_name_plural = "صور الموقع"


class Category(models.Model):
    """
    ex(nagdy)
    """
    name = models.CharField(max_length=128, blank=False)
    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "المنتجات"


class Product(models.Model):
    """
    ex(herfy wasat (12-13)kg - kamel , 1280)
    """
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=128, blank=False)
    price = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "الاحجام"


class Option(models.Model):
    """
    ex(نوع التقطيع , الرأس , مفروم)
    """
    name = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "الخيارات المتاحة"


class Value(models.Model):
    """
    ex(yes)
    """
    value = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name_plural = "القيم المتاحة للخيارات"


class CategoryOptionValue(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    option_name = models.ForeignKey(
        Option, on_delete=models.DO_NOTHING, default=None)
    option_values = models.ManyToManyField(
        Value, default=None)

    def __str__(self):
        return self.category.name

    class Meta:
        verbose_name_plural = "خيارات المنتج"


class ProductVariant(models.Model):
    option_name = models.ForeignKey(
        Option, on_delete=models.DO_NOTHING, default=None)
    option_value = models.ForeignKey(
        Value, on_delete=models.DO_NOTHING, default=None)


class CartItem(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, related_name='category')
    product = models.ForeignKey(
        Product, on_delete=models.DO_NOTHING, related_name='items')
    quantity = models.IntegerField(default=1)
    total_price = models.PositiveIntegerField(default=0)
    notes = models.CharField(max_length=200, blank=True)
    beef_quantity = models.IntegerField(default=0)
    fridge_status = models.CharField(max_length=200, blank=True)
    alive_delivery_form = models.BooleanField(default=True)
    variants = models.ManyToManyField(ProductVariant)

    def __str__(self):
        return (" {}, {}").format(self.product.name, self.quantity)


class Cart(models.Model):
    item = models.ManyToManyField(CartItem)
    total_amount = models.IntegerField()

    # def __str__(self):
    #     return self.id


class Order(models.Model):
    name = models.CharField(max_length=128, verbose_name="customer_name")
    address = models.CharField(max_length=128, verbose_name="customer_address")
    phone = models.IntegerField()
    session_id = models.CharField(max_length=128, null=True)
    payment_method = models.CharField(max_length=128)
    order_confirmation_method = models.CharField(max_length=128)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-date_created',)
        verbose_name_plural = "الطلبات"


@receiver(post_delete, sender=Order)
def delete_order_cart(sender, instance, **kwargs):
    pass
    # cartitems and product variants
    # print("cart : ", instance.cart)
    # print("cart items : ", )
    # instance.cart.delete()
