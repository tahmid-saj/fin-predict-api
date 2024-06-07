from utils.api_requests.chatbot_requests import request_chatbot

def get_chatbot_response(request):
  request = request.data
  
  chatbot_response = request_chatbot(str(request["userMessage"]))
  response = {
    "message": chatbot_response
  }
  
  return response