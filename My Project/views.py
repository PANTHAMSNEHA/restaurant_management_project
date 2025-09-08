from django.shortcuts import render

def plce_order_view(request):
    return render(request, 'orders/place_order.html')




def menu_view(request):
    bredcrumbs = [
        {'name':'Home', 'url':'/'},
        {'name':'Menu','url':'/menu'},
    ]
    return render(request,'menu.html',{'breadcrumbs':breadcrumbs})