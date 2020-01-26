from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


from rest_framework import status
from . import serializers
from . import models
from . import permissions

# Create your views here.
class HelloApiView(APIView):
    """test api view"""
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """return a list of apiview features"""
        
        an_apiview=[
            'Uses HTTP method as function',
            'It is similar to a traditional django',
            'gives you most control over your logic',
            'It mapped manually to Urls'

        ]
        
        return Response({'message':'Hello','an_apiview':an_apiview})
    
    def post(self,request):
        """Create a hello messaage with our name"""

        serializer =serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None):
        """Handles update"""

        return Response({'method':'put'})
    
    def patch(self,request,pk=None):
        """Patch request , only update fields provided"""

        return Response({'method':'patch'})
    
    def delete(self,request,pk=None):
        """delete a object"""

        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """test api viewset"""

    serializer_class=serializers.HelloSerializer

    def list(self,request):
        """return a hello message"""

        a_viewset=[
            'User actio(list,create,retrieve,update,partial_update)',
            'automatically maps to Ursl using Routers'
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})
    
    def create(self,request):
        """create a new hello message"""

        serializer =serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk=None):
        """handles getting a n object by its ID"""

        return Response({'http_method':'GET'})
        
    def update(self,request,pk=None):
        """handles update an object"""

        return Response({'http_method':'PUT'})
        
    def partial_update(self,request,pk=None):
        """handles updating part of object"""

        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """handles removing an object"""
        
        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating updating profiles"""

    serializer_class=serializers.UserProfileSerializer
    queryset = models.UserProfile.object.all()

    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)

    
        

    
            




