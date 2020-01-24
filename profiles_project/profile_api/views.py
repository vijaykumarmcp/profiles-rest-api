from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """test api view"""
    def get(self,request,format=None):
        """return a list of apiview features"""
        
        an_apiview=[
            'Uses HTTP method as function',
            'It is similar to a traditional django',
            'gives you most control over your logic',
            'It mapped manually to Urls'

        ]
        
        return Response({'message':'Hello','an_apiview':an_apiview})

