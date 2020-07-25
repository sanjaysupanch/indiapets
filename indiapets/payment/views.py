from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt
from .models import *
from accounts.forms import *



@csrf_exempt
def process_payment(request, **kwargs):
    ids=kwargs['id']
    pet_price=kwargs['pet_price']
    pet_name=kwargs['pet_name']
    
    email=str(request.user)
    
    data=str(ids)+" "+email
    invoice=int(ids)

    invoice="INV-000"+str(invoice+1)
    host = request.get_host()
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': pet_price,
        'item_name': pet_name,
        'invoice': invoice,
        'currency_code': 'INR',
        'custom':data,
        'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,reverse('payment_cancelled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html', {'form':form, 'price':pet_price})

@csrf_exempt
def payment_done(request):
    return render(request, 'payment/payment_done.html')
 
 
@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/payment_cancelled.html')

