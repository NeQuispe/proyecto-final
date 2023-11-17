from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products', null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    total = models.FloatField()
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return super().__str__()


    def save(self, *args, **kwargs):
        """Guarda la instancia y calcula el precio total de la orden.
        Modifica la cantidad de stock disponible."""
        
        self.total = self.product.price * self.quantity
        super().save(*args, **kwargs)
        self.product.stock -= self.quantity
        self.product.save()
        
    def delete(self, *args, **kwargs):
        """Elimina la instancia y modifica la cantidad de stock disponible."""
        
        self.product.stock += self.quantity
        self.product.save()
        super().delete(*args, **kwargs)
