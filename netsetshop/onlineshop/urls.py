from django.urls import path 
from . import views

app_name = 'onlineshop'

urlpatterns = [
    path('shop/', views.product_list, name = 'product_list'),
    path('<slug:category_slug>/', views.product_list, name = 'product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name = 'product_detail'),
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
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