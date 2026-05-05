from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'


class About(models.Model): 
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'


class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'
class MpesaTransaction(models.Model):
    """
    Stores all M-Pesa STK Push transactions for tracking and reconciliation.
    """

    class Status(models.TextChoices):
        PENDING   = 'PENDING',   'Pending'
        SUCCESS   = 'SUCCESS',   'Success'
        FAILED    = 'FAILED',    'Failed'
        CANCELLED = 'CANCELLED', 'Cancelled'

    # --- Request Info ---
    phone_number       = models.CharField(max_length=15)
    amount             = models.DecimalField(max_digits=10, decimal_places=2)
    account_reference  = models.CharField(max_length=100)
    description        = models.CharField(max_length=150)

    # --- Daraja Response Fields ---
    merchant_request_id  = models.CharField(max_length=100, blank=True, null=True)
    checkout_request_id  = models.CharField(max_length=100, blank=True, null=True, db_index=True)

    # --- Callback / Confirmation Fields ---
    mpesa_receipt_number = models.CharField(max_length=50, blank=True, null=True)
    transaction_date     = models.CharField(max_length=30, blank=True, null=True)
    result_code          = models.IntegerField(blank=True, null=True)
    result_desc          = models.TextField(blank=True, null=True)

    # --- Status ---
    status     = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'M-Pesa Transaction'
        verbose_name_plural = 'M-Pesa Transactions'

    def __str__(self):
        return f"{self.phone_number} | KES {self.amount} | {self.status}"
