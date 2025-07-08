from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import datetime

current_year = datetime.datetime.now().year

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
            MaxValueValidator(current_year)
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
    
    def __str__(self):
        return self.title

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist_items")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchlisted_by")

    class Meta:
        unique_together = ("user", "listing")  # prevents duplicates

    def __str__(self):
        return f"{self.user.username} → {self.listing.title}"