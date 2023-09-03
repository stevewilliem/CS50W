from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class comment(models.Model):
    comments = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.comments}"

class auction(models.Model):
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    active_status = models.BooleanField()

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    bid_value =  models.DecimalField(decimal_places=2, max_digits=10)
    # image = models.URLField(blank=True)
    image = models.ImageField(null=True, blank=True, help_text="upload image", upload_to='uploads/')
    category = models.CharField(max_length=40)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.id}: item: {self.title} category: {self.category} listing open: {self.active_status} user: {self.creator_id}"
    
class bid(models.Model):
    highest_bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    highest_bid = models.ForeignKey(auction, on_delete=models.CASCADE, related_name="bid_price")

    def __str__(self):
        return f"{self.id}: bidder: {self.highest_bidder} ({self.price})"
