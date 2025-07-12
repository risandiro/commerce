from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Listing(models.Model):
    title = models.CharField(max_length=64, verbose_name="Title")
    description = models.TextField(verbose_name="Description")

    year = models.IntegerField (
        verbose_name="Year",
        blank=True,
        null=True,
        validators=[
            MinValueValidator(1837),
            MaxValueValidator(timezone.now().year)
        ])
    
    img_url = models.URLField (
        max_length=500, 
        blank=True, 
        verbose_name="Image URL"
        )

    starting_bid =  models.DecimalField (
        max_digits=10,
        decimal_places=2,
        verbose_name="Starting Bid",
        validators=[
            MinValueValidator(0.01),
            MaxValueValidator(999.99)
        ])
    
    category = models.ForeignKey (
        Category, 
        on_delete=models.CASCADE, 
        related_name="listings",
        verbose_name="Category",
        blank=True,
        null=True
        )
    
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE, 
        related_name="user",
        verbose_name="Creator",
        blank=True,
        null=True
        )
    
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def current_price(self):
        highest_bid = self.bids.order_by("-amount").first()
        return highest_bid.amount if highest_bid else self.starting_bid
    
    def highest_bidder(self):
        highest_bid = self.bids.order_by("-amount").first()
        return highest_bid.bidder if highest_bid else None
    
    def bid_history(self):
        return self.bids.order_by('-timestamp')[:5]

    
    def __str__(self):
        return self.title


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist_items")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchlisted_by")

    class Meta:
        unique_together = ("user", "listing")  # prevents duplicates

    def __str__(self):
        return f"{self.user.username} → {self.listing.title}"
    

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    bidder = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")

    amount = models.DecimalField (
        max_digits=10,
        decimal_places=2,
        verbose_name="Bid",
        validators=[
            MaxValueValidator(999.99)
        ])

    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.amount} by {self.bidder} on {self.listing}"
    

class Comment(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    title = models.CharField(max_length=64, verbose_name="Title", default=None)
    text = models.TextField(verbose_name="Comment")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.author}'s comment on {self.listing} with title: {self.title}"