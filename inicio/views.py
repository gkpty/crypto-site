from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
import requests
import json

from .models import Post
from .models import Register
from .models import Contact_Us

from .forms import RegisterForm
from .forms import Contact_UsForm


def index(request):
	#Anuncios
    latest_post_list = Post.objects.order_by('-post_date')[:5]
    #BTC
    dbtc = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin')
    rbtc = dbtc.json()
    lbtc = rbtc[0].get("price_usd")
    #ETH
    deth = requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum')
    reth = deth.json()
    leth = reth[0].get("price_usd")
    #XLM
    dxlm = requests.get('https://api.coinmarketcap.com/v1/ticker/stellar')
    rxlm = dxlm.json()
    lxlm = rxlm[0].get("price_usd")
    #form Registro

    if request.method == "POST":
    	if 'contacta' in request.POST:
    		contactform = Contact_UsForm(request.POST, prefix='contact')
    		if contactform.is_valid():
    			contacto = contactform.save(commit=False)
    			contacto.contact_date = timezone.now()
    			contacto.save()
    		registerform = RegisterForm(prefix='register')
    		return HttpResponse("Gracias por contactarnos, le responderemos pornto.")
    	if 'registra' in request.POST:
        	registerform = RegisterForm(request.POST, prefix='register')
        	if registerform.is_valid():
        		register = registerform.save(commit=False)
        		register.reg_date = timezone.now()
        		register.save()
        	contactform = Contact_UsForm(prefix='contact')
        	return HttpResponse("Gracias por Registrarse!")

        	#contactform = Contact_UsForm(request.POST, prefix='contact')
        	#if contactform.is_valid():
        		#contact = contactform.save(commit=False)
        		#contact.contact_date = timezone.now()
        		#contact.save()
        	#registerform = RegisterForm(prefix='register')
        	#return HttpResponse("Gracias por contactarnos! le responderemos pronto.")
    else:
    	registerform = RegisterForm(prefix='register')
    	contactform = Contact_UsForm(prefix='contact')
    #context
    context = {'latest_post_list': latest_post_list, 'lbtc':lbtc, 'leth':leth, 'lxlm':lxlm, 'contactform':contactform, 'registerform':registerform}
    return render(request, 'inicio/index.html', context)

def registro(request):
	return HttpResponse("gracias por registrarse")

def contactus(request):
	return HttpResponse("gracias por contactarnos")
