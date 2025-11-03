from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomPizzaForm, CheckoutForm
from .models import Order
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def order(request):
    ready_made = [
        {'name': 'Pizza Margherita', 'price': 9.99, 'image': 'firstdjango/images/pizza3.jpg'},
        {'name': 'Pepperoni Pizza', 'price': 11.99, 'image': 'firstdjango/images/pizza2.jpg'},
        {'name': 'Tripolitina', 'price': 12.99, 'image': 'firstdjango/images/pizza1.jpg'},
    ]
    custom_form = CustomPizzaForm()
    return render(request, 'order.html', {'products': ready_made, 'custom_form': custom_form})


def basket(request):
    basket_items = request.session.get('basket_items', [])
    total = sum(float(item.get("price", 9.99)) for item in basket_items)
    return render(request, 'basket.html', {'basket_items': basket_items, 'basket_total': total})

def add_to_basket(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        product_price = request.POST.get("product_price")
        basket_items = request.session.get("basket_items", [])

        try:
            product_price = float(product_price)
        except (TypeError, ValueError):
            product_price = 9.99  # Default price

        new_item = {
            "type": "pre_made",
            "name": product_name,
            "price": product_price,
        }

        basket_items.append(new_item)
        request.session["basket_items"] = basket_items

    return redirect("basket")


def checkout(request):
    basket_items = request.session.get('basket_items', [])
    if not basket_items:
        messages.error(request, 'Your basket is empty.')
        return redirect('basket')

    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            messages.success(request, "Payment successful!")
            request.session["basket_items"] = []
            return redirect("checkout_success")
        else:
            messages.error(request, "Invalid payment details. Please try again.")
    
    else:
        form = CheckoutForm()

    basket_total = sum(float(item.get("price", 9.99)) for item in basket_items)
    return render(request, "checkout.html", {"form": form, "basket_items": basket_items, "basket_total": basket_total})


def checkout_success(request):
    return render(request, 'checkout_success.html')

def remove_from_basket(request, item_index):
    if request.method == "POST":
        basket_items = request.session.get("basket_items", [])

        # Try to remove the item safely
        try:
            basket_items.pop(item_index)
        except IndexError:
            pass

        request.session["basket_items"] = basket_items

    return redirect("basket")

def clear_basket(request):
    if 'basket' in request.session:
        del request.session['basket']  # Clear session-based basket
    return redirect('basket')  # Redirect to updated basket

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("index")  # Redirect to home page
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "registration/login.html")


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login")  # Redirect to login page after logout


def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("register")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
        messages.success(request, "Registration successful!")
        return redirect("index")

    return render(request, "registration/register.html")

@login_required
def previous_orders(request):
    orders = Order.objects.filter(user=request.user).prefetch_related('items')
    return render(request, 'previous_orders.html', {'orders': orders})