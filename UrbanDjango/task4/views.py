from django.shortcuts import render


def index(request):
    return render(request, 'fourth_task/index.html')


def shop(request):
    items = {'items': ['Игровая приставка', 'Cyberpunk 2077', 'Контроллер']}
    return render(request, 'fourth_task/shop.html', context=items)


def cart(request):
    return render(request, 'fourth_task/cart.html')
