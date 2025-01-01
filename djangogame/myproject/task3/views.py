from django.shortcuts import render


def home(request):
    return render(request, 'third_task/home.html')


def shop(request):
    items = {
        'item1': 'Atomic Heart',
        'item2': 'Cyberpak 2077',
        'item3': 'Pay Day 2',
    }
    return render(request, 'third_task/shop.html', {'items': items})


def cart(request):
    return render(request, 'third_task/cart.html')
