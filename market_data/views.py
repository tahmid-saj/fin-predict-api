from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, status, mixins, viewsets

from django.shortcuts import render, get_object_or_404

from market_data.permissions import AdminOrReadOnly, AdminOnly
from market_data.controllers import get_market_data

# Create your views here.

class MarketDataGenerate(APIView):
  # permission_classes = [AdminOrReadOnly]
  
  def post(self, request):
    response = get_market_data(request=request)
    
    return Response(data=response)