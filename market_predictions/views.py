from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, status, mixins, viewsets

from django.shortcuts import render, get_object_or_404

from market_predictions.permissions import AdminOrReadOnly, AdminOnly
from market_predictions.controllers import get_market_predictions_daily, get_market_predictions_two_weeks

# Create your views here.

class MarketPredictionsGenerateDaily(APIView):
  # permission_classes = [AdminOrReadOnly]

  def post(self, request):
    response = get_market_predictions_daily(request=request)
    
    return Response(data=response)

class MarketPredictionsGenerateTwoWeeks(APIView):
  # permission_classes = [AdminOrReadOnly]
  
  def post(self, request):
    response = get_market_predictions_two_weeks(request=request)
    
    return Response(data=response)