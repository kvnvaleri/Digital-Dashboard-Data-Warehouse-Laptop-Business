from django.db import models

class DimLaptop(models.Model):
    company = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    typename = models.CharField(max_length=255)
    inches = models.DecimalField(max_digits=4, decimal_places=1)
    screen = models.CharField(max_length=255)
    touchscreen = models.BooleanField()
    ipspanel = models.BooleanField()
    retinadisplay = models.BooleanField()

    def __str__(self):
        return self.product

class FactHarga(models.Model):
    laptopid = models.IntegerField()
    spesifikasiid = models.IntegerField()
    waktuid = models.IntegerField()
    price_euros = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Laptop ID: {self.laptopid}, Harga: {self.price_euros}"