from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [

path('',views.index,name='index'),
path('index/',views.index,name='index'),
path('contact/',views.con,name='contact'),
path('about/',views.about,name='about'),
path('jewellery',views.jewellery,name='jewellery'),
path('contact_form',views.contact_form,name='contact_form'),
path('login',views.login,name='login'),
path('signup',views.signup,name='signup'),
path('logout',views.logout,name='logout'),
path('login',views.info,name='info'),
path('product',views.product,name='product'),
path('necklace',views.necklace,name='necklace'),
path('earrings',views.earrings,name='earrings'),
path('rings',views.rings,name='rings'),
path('hair',views.hair,name='hair'),
path('productview/<int:pk>',views.productview,name='productview'),
path('add_to_cart/',views.add_to_cart,name='add_to_cart'),
path('cart/',views.showcart,name='cart'),
path('pluscart/',views.plus_cart,name='pluscart'),
path('minuscart/',views.minus_cart,name='minuscart'),
path('removecart/',views.remove_cart,name='removecart'),
path('checkout/',views.checkout,name='checkout'),
]