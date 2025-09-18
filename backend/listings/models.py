from django.contrib.auth import get_user_model
from django.db import models
from uuid import uuid4


User = get_user_model()


class Listing(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(max_length=1000, blank=True)
    image_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')

    def __str__(self):
        return f"{self.title} created by {self.seller.username} at {self.created_at.strftime('%d-%m-%Y')}"
