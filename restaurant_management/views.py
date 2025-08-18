def home(request):
    try:
        query = request.GET.get('q','')
        content = {
            "restaurant_name":"Flavours of India",
            "search_query": query
        }
        return render(request, 'home.html', content)
    except Exception as e:
        return HttpResponseServerErrir(f"An error occurred: {e}")