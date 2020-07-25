from django.shortcuts import get_object_or_404
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from paypal.standard.models import ST_PP_COMPLETED
from accounts.models import *
 
@receiver(valid_ipn_received)
def payment_notification(sender, **kwargs):
    ipn_obj = sender
    data=ipn_obj.custom
    data=list(data.split(' '))
    ids=int(data[0])
    email=data[1]
    
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        apk2=get_object_or_404(seller, id=ids)
        apk2.is_sold=True
        apk2.save()    
        print("Payment singnal receive successfully===========================>1")
       