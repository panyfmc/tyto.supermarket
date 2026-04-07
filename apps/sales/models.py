from django.db import models
from apps.products.models import Product
from apps.clients.models import Client

class SaleItem(models.Model):
    sale = models.ForeignKey('Sale', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.product.stock < self.quantity:
            raise ValueError("Estoque insuficiente")

        self.product.stock -= self.quantity
        self.product.save()

        super().save(*args, **kwargs)

class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Venda {self.id}"

    def calculate_total(self):
        total = sum(item.price * item.quantity for item in self.items.all())
        self.total = total
        self.save()
        
