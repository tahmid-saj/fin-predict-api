from utils.api_requests.market_predictions_requests import request_market_predictions_daily, request_market_predictions_two_weeks

def get_market_predictions_daily(request):
  
  closing_price = request_market_predictions_daily()
  
  return closing_price

def get_market_predictions_two_weeks(request):
  
  closing_price_dates, closing_prices = request_market_predictions_two_weeks()
  
  response = {
    "closingPriceDates": closing_price_dates,
    "closingPrices": closing_prices
  }
  
  return response