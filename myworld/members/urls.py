from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login, name='login'),
    path('search/', views.search, name='search'),
    path('contactSent/', views.contactSent, name='contactSent'),
    path('checkout/', views.checkout, name='checkout'),
    path('productDetails/', views.productDetails, name='productDetails'),
    
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]