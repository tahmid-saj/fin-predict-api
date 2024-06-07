from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, status, mixins, viewsets

from django.shortcuts import render, get_object_or_404

from chatbot.permissions import AdminOrReadOnly, AdminOnly
from chatbot.controllers import get_chatbot_response

# Create your views here.

class ChatbotGenerateResponse(APIView):
  permission_classes = [AdminOrReadOnly]
  
  def post(self, request):
    print("getting")
    response = get_chatbot_response(request=request)
    
    print(response)
    
    return Response(data=response)