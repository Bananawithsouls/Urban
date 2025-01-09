from django.urls import path
from .views import home, shop, cart, menu

urlpatterns = [
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('menu/', menu, name='menu'),
]
