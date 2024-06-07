from utils.api_requests.chatbot_requests import request_chatbot

def get_chatbot_response(request):
  print(request.data)
  request = request.data
  
  response = request_chatbot(str(request["userMessage"]))
  
  return response