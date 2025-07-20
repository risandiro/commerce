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
    path("auction_close/<int:listing_id>", views.auction_close, name="auction_close"),
    path("listing/<int:listing_id>/bid_order", views.bid_order, name="bid_order"),
    path("user/<str:username>", views.user_profile, name="user_profile"),
    path("listing/<int:listing_id>/add_comment", views.add_comment, name="add_comment"),
    path("listing/<int:listing_id>/all_comments", views.all_comments, name="all_comments"),
    path("categories", views.categories, name="categories"),
    path("categories/<int:category_id>", views.category_list, name="category_list")
]
