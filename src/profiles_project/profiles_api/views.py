from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self, request,format=None):
        """Return a list of  APIView features."""

        an_apiview=[
        'Uses HTTP method as functions (get,post,put,delete)',
        'It is similiar to a traditional Django view',
        'Gives you most control of you logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})
        
