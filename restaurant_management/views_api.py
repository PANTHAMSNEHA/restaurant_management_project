from rest_framework.views import APIView
from rest_framework.response  import Response

class MenuAPIView(APIView):
    def get(self,request):
        menu = [
            {"name":"Butter chicken","description":"Creamy tomato-based chicken curry","price":250},
            {"name":"Paneer Tikka","description":"Grilled cottage cheese with spices","price":200},
            {"name":"Masala Dosa","description":"Crispy rice crepe with spiced potato filling","price":150},
        ]
        return Response(menu)