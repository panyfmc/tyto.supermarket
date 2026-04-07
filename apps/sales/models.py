from django.db import models
from apps.products.models import Product
from apps.clients.models import Client

#vender um item a um cliente cadastrado
class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        if self.item.stock < self.quantity:
            raise ValueError("Estoque insuficiente")
        self.item.stock -= self.quantity
        self.item.save()

        self.total = self.item.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.item.name} - {self.quantity} unidades"
        
