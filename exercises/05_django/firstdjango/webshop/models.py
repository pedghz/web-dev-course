from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True, default='')
    description = models.TextField(null= True)
    image_url = models.URLField(blank=True, null= True)
    quantity = models.IntegerField(default=0)

    def sell(self):
        setattr(self, 'quantity', getattr(self, 'quantity') - 1)
        self.save()
