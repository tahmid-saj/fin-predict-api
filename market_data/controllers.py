from utils.constants.market_data_constants import (
  MARKET_DATA_TYPES, MARKET_DATA_CRYPTO_PREFIX, MARKET_DATA_FOREX_PREFIX, MARKET_DATA_INTERVALS)
from utils.api_requests.market_data_requests import request_market_data

def get_market_data(request):
  print(request.data)
  request = request.data
  
  print("21")
  
  request_fields = {
    "category": request["category"],
    "ticker": request["ticker"],
    "interval": MARKET_DATA_INTERVALS[request["interval"]],
    "start_date": request["startDate"],
    "end_date": request["endDate"]
  }
  
  if request_fields["category"] == MARKET_DATA_TYPES["crypto"]:
    request_fields["ticker"] = MARKET_DATA_CRYPTO_PREFIX + request_fields["ticker"]
  elif request_fields["category"] == MARKET_DATA_TYPES["currencies"]:
    request_fields["ticker"] = MARKET_DATA_FOREX_PREFIX + request_fields["ticker"]
  
  closing_price_dates, closing_prices = request_market_data(request=request_fields)
  
  response = {
    "closingPriceDates": closing_price_dates,
    "closingPrices": closing_prices
  }
  
  return response