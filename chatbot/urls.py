from django.urls import path, include
from chatbot.views import ChatbotGenerateResponse

urlpatterns = [
  path("generate/", ChatbotGenerateResponse.as_view(), name="chatbot-response")
]
