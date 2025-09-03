
def menu_view(request):
    bredcrumbs = [
        {'name':'Home', 'url':'/'},
        {'name':'Menu','url':'/menu'},
    ]
    return render(request,'menu.html',{'breadcrumbs':breadcrumbs})