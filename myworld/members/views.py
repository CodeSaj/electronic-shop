from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members
from django.contrib.auth import authenticate, login

def index(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
  
def adduser(request):
  x = request.POST['username']
  y = request.POST['pw']
  z = request.POST['email']
  member = Members(username=x, password=y, email=z)
  member.save()
  return HttpResponseRedirect(reverse('login'))
  
def loginU(request):
    user = request.POST['username']
    passw = request.POST['pw']
    name = ""
    mydata = Members.objects.filter(username=user, password=passw).values()
    for x in mydata:
        name = x
        
    if name is not "":
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('login'))
  
def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))
  
def update(request, id):
  mymember = Members.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
 
def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.username = first
  member.password = last
  member.save()
  return HttpResponseRedirect(reverse('index'))
  
def news(request):
  template = loader.get_template('news.html')
  return HttpResponse(template.render({}, request))
  
def contact(request):
  template = loader.get_template('contactUs.html')
  return HttpResponse(template.render({}, request))
  
def about(request):
  template = loader.get_template('AboutUs.html')
  return HttpResponse(template.render({}, request))
  
def cart(request):
  template = loader.get_template('shoppingCart.html')
  return HttpResponse(template.render({}, request))
  
def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render({}, request))
  
def search(request):
  template = loader.get_template('search.html')
  return HttpResponse(template.render({}, request))
  
def contactSent(request):
  template = loader.get_template('ContactUsSent.html')
  return HttpResponse(template.render({}, request))
 
def checkout(request):
  template = loader.get_template('Checkout.html')
  return HttpResponse(template.render({}, request))
  
def productDetails(request):
  template = loader.get_template('productDetails.html')
  return HttpResponse(template.render({}, request))
  
def register(request):
  template = loader.get_template('register.html')
  return HttpResponse(template.render({}, request))