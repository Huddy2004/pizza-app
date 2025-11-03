from django.urls import path
from firstdjango import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    
    # Orders
    path("order/", views.order, name="order"),
    path("basket/", views.basket, name="basket"),
    
    # Checkout
    path("checkout/", views.checkout, name="checkout"),
    path("checkout/success/", views.checkout_success, name="checkout_success"),

    # Previous Orders
    path("previous-orders/", views.previous_orders, name="previous_orders"),

    # basket actions
    path("add-to-basket/", views.add_to_basket, name="add_to_basket"),
    path("remove-from-basket/<int:item_index>/", views.remove_from_basket, name="remove_from_basket"),
    path("clear-basket/", views.clear_basket, name="clear_basket")
]
