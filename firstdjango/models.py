from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, default="No Name")  # Ensure default value
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(default="Unknown Address")  # Ensure default value
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.full_name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=20, blank=True)
    base = models.CharField(max_length=20, blank=True)
    toppings = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} for Order {self.order.id}"
