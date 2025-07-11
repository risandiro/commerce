from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Listing, Watchlist
from .forms import NewListingForm, NewBidForm


def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def create_listing(request):
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.creator = request.user
            listing.save()
            return redirect('index')

    else:
        form = NewListingForm()  

    return render(request, "auctions/create_listing.html", {
                "form": form
            })

def show_listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)

    is_in_watchlist = False
    if request.user.is_authenticated:
        is_in_watchlist = Watchlist.objects.filter(user=request.user, listing=listing).exists()

    form = NewBidForm() 

    return render(request, "auctions/show_listing.html", {
        "listing": listing,
        "is_in_watchlist": is_in_watchlist,
        "form": form
    })

@login_required
def auction_close(request, listing_id):
    listing = Listing.objects.get(id=listing_id)    # get listing_id of the page
    listing.active = False
    listing.save()
    return redirect("show_listing", listing_id=listing.id)


@login_required
def my_listings(request):
    queryset = Listing.objects.filter(creator=request.user)
    return render(request, "auctions/my_listings.html", {
                "listings": queryset
            })

@login_required
def watchlist(request):
    queryset = Listing.objects.filter(watchlisted_by__user=request.user)
    return render(request, "auctions/watchlist.html", {
                "listings": queryset
            })

@login_required
def toggle_watchlist(request, listing_id):
    listing = Listing.objects.get(id=listing_id)    # get listing_id of the page
    watchlist_item = Watchlist.objects.filter(user=request.user, listing=listing)   # create temporary watchlist object

    if watchlist_item.exists():    # check if the same object exists already
        watchlist_item.delete()    # if so, delete it
    else:
        Watchlist.objects.create(user=request.user, listing=listing)    # if not, create one
    
    return redirect('show_listing', listing_id=listing.id)