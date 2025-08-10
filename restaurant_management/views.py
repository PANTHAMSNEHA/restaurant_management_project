from django.shortcuts import render

def about_view(request):
    """Render the About Us page with restaurant info and team details."""
    return render(request, 'about.html')