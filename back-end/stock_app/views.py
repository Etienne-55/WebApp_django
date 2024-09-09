from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, world!-test1"}, status=status.HTTP_200_OK)
    
class Get_name(APIView):
    def get(self, request):
        return Response({"message": "Enter your name: "}, status=status.HTTP_200_OK)
    
class Get_password(APIView):
    def get(self, request):
        return Response({"message": "Enter your password: "}, status=status.HTTP_200_OK)

