from django.contrib.auth import get_user_model
from django.db import models

from listings.models import Listing


User = get_user_model()

class Bid(models.Model):
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    listings = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_bids")
    timestamp = models.DateTimeField(auto_now_add=True)
