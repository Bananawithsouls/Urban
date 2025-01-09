from django.shortcuts import render


def home(request):
    return render(request, 'fourth_task/home.html')


def shop(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'The Witcher 3']
    return render(request, 'fourth_task/shop.html', {'games': games})


def cart(request):
    return render(request, 'fourth_task/cart.html')


def menu(request):
    return render(request, 'fourth_task/menu.html')

