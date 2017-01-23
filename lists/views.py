from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        print('@@@@@@@@@@@@@@')
        return redirect('/lists/the-only-list-in-the-world')

    print('+++++')
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    print('##########')
    return render(request, 'list.html', {'items': items})
