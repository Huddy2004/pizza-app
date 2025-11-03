from django import forms
from django.core.validators import RegexValidator
from django.utils import timezone

class CustomPizzaForm(forms.Form):
    CRUST_CHOICES = [
        ('thin', 'Thin'),
        ('normal', 'Normal'),
        ('cheese_stuffed', 'Cheese Stuffed'),
    ]
    SAUCE_CHOICES = [
        ('tomato', 'Tomato'),
        ('bbq', 'BBQ Base'),
        ('garlic_pesto', 'Garlic Pesto Base'),
    ]
    TOPPING_CHOICES = [
        ('pepperoni', 'Pepperoni'),
        ('mushrooms', 'Mushrooms'),
        ('onions', 'Onions'),
        ('olives', 'Olives'),
        ('extra_cheese', 'Extra Cheese'),
        ('sausage', 'Sausage'),
        ('bacon', 'Bacon'),
        ('peppers', 'Bell Peppers'),
        ('spinach', 'Spinach'),
        ('pineapple', 'Pineapple'),
    ]
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    ]

    crust = forms.ChoiceField(
        choices=CRUST_CHOICES,
        widget=forms.RadioSelect,
        label="Crust Type"
    )
    sauce = forms.ChoiceField(
        choices=SAUCE_CHOICES,
        widget=forms.RadioSelect,
        label="Sauce Base"
    )
    toppings = forms.MultipleChoiceField(
        choices=TOPPING_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Toppings (Select up to 4 free; extra toppings cost €0.50 each)"
    )
    size = forms.ChoiceField(
        choices=SIZE_CHOICES,
        widget=forms.Select,
        label="Pizza Size"
    )

class CheckoutForm(forms.Form):
    full_name = forms.CharField(label="Full Name", max_length=100)
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone Number", max_length=15)
    address = forms.CharField(label="Address", widget=forms.Textarea)

    card_number = forms.CharField(label="Card Number", max_length=16)
    expiry_date = forms.CharField(label="Expiry Date (MM/YY)", max_length=5)
    cvv = forms.CharField(label="CVV", max_length=3, widget=forms.PasswordInput)
