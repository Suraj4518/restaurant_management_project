from rest_framework.views import APIView
from rest_framework.response import response
from .serializers import MenuItemSerializer

class MenuView(APIView)

def get(self, request):
    menu_data = [
        {
            "name" = "Margherita",
            "description"= "Classic pizza with tomato sauce"
            "price"= "545"
        },
        
        {
            "name"= "Pasta"
            "description" = "Pasta with eggs"
            "price" = "145"
        },

        {
            "name" = "Chicken"
            "description" = "Chicken with extra butter"
            "price" = "250"
        },
        
        {
            "name" = "Naan"
            "description" = "Naam with extra butter"
            "price" = "60"
            
        }


    ]

    serializer = MenuItemSerializer(menu_data, many = True)
    return Response(serializer.data)
    