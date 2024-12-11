from django.shortcuts import render


def index(request):
    return render(request, 'third_task/index.html')


def shop(request):
    games = {'first': 'Игровая приставка', 'second': 'Cyberpunk 2077', 'third': 'Контроллер'}
    return render(request, 'third_task/shop.html', context=games)


def cart(request):
    return render(request, 'third_task/cart.html')
