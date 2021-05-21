from django.db import models
from .utils import product_link
# Create your models here.

class Address(models.Model):
    name = models.CharField(max_length=220, blank=True)
    url = models.URLField()
    currentprice = models.FloatField(blank=True)
    oldprice = models.FloatField(default=0)
    pricedifference = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ('pricedifference', '-created')

    def save(self, *args, **kwargs):
        name, price = product_link(self.url)
        oldprice = self.currentprice
        if self.currentprice:
            if price != oldprice:
                amountdifference = price - oldprice
                self.pricedifference = round(amountdifference, 2)
                self.oldprice = oldprice
                self.currentprice = price

        else:
            self.oldprice = 0
            self.pricedifference = 0

        self.name = name
        self.currentprice = price
        
        super().save(*args, **kwargs)