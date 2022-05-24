from django import forms
from .models import Order
from .bulma_mixin import BulmaMixin

#dobavit v pizza
class OrderForm(BulmaMixin, forms.Form):
    name = forms.CharField(label='Write your name')
    phone = forms.CharField(label='Write your phone')
    address = forms.CharField(label='Write your address')
    time_delivery = forms.CharField(label='Faster')
    class Meta:
        model = Order
        fields = ['name','phone', 'address','time_delivery']


# class RateForm(forms.ModelForm):
#     text = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), label='Leave your review here')
#     rate = forms.ChoiceField(choices=RATE_CHOICES, required=True, label='Rate product from 1 to 5')
#
#     class Meta:
#         model = Review
#         fields = ('text', 'rate')
