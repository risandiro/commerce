from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("my_listings", views.my_listings, name="my_listings"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listing/<int:listing_id>", views.show_listing, name="show_listing"),
    path("listing/<int:listing_id>/toggle", views.toggle_watchlist, name="toggle_watchlist"),
    path("auction_close/<int:listing_id>", views.auction_close, name="auction_close")
]
