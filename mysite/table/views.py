from .models import Currency, Coins
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.contrib import auth


@login_required(login_url="/login/")
def table(request):
    select = Coins.objects.all()
    if request.method == "POST":
        coin = request.POST['sel']
        if coin != 'All':
            table = Currency.objects.filter(coinName__name_of_currency__exact=coin)
        else:
            table = Currency.objects.all()[:830]
    else:
        table = Currency.objects.all()[:830]
    print(auth.get_user(request))
    dic = {'table': table, 'select': select, 'username': auth.get_user(request)}
    return render(request, 'table.html', dic)