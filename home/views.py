from django.shortcuts import render

# Create your views here.
def home_view(request):
    """
    Renders the main homepage template.

    """
    return render(request,'home.html')