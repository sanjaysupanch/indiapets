from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import requests
import json


def pet_data(request):
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json",
    }
    API_ENDPOINT = 'http://127.0.0.1:8000/api/seller/'
    r = requests.get(url=API_ENDPOINT, headers=headers)
    pets_data = r.json()
    return render(request, 'vetinary/pets_data.html', {'data':pets_data})

def pet_update(request, **kwargs):
    ids=kwargs['id']
    print(ids, '1111111111111111111111111111')
    if request.method == "POST":
        form = request.POST
        is_verified = form['verify']
        print(is_verified, '1111111111111111111111111111')
        data={"is_verified":is_verified, "doctor_reg_no":str(65401), "doctor_name": "Pia Roy"}    
        data = json.dumps(data)
        headers = {
            "Content-Type": "application/json",
            "accept": "application/json",
        }
        print(data)
        API_ENDPOINT = 'http://127.0.0.1:8000/api/seller/'+str(ids)+'/'
        r = requests.put(url=API_ENDPOINT, data=data, headers=headers)
        pastebin_url = r.content
        print("The pastebin URL is:%s" % pastebin_url)
        return HttpResponse('<h1>hweuwe</h1>')
    
    return render(request, 'vetinary/pets_details.html', {})
