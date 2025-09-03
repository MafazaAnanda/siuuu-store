import uuid
from django.db import models

# Create your models here.
class Item(models.Model):
    CATEGORY_CHOICES = [
    ('jersey', 'Jersey'),
    ('shoes', 'Shoes'),
    ('ball', 'Ball'),
    ('accessory', 'Accessory'),
    ('equipment', 'Equipment'),
    ]
    
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=25, blank=True)

def __str__(self):
        return self.name