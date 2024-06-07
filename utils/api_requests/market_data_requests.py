from polygon import RESTClient
import os
from dotenv import load_dotenv

from utils.constants.market_data_constants import MARKET_DATA_SEARCH_QUERY_MULTIPLIER
from utils.helpers.market_data_helpers import process_market_data_response

load_dotenv()

polygon_client = RESTClient(api_key=os.getenv("POLYGON_API_KEY"))

def request_market_data(request):
  
  response_aggregates = []
  for aggregate in polygon_client.list_aggs(
    ticker=request["ticker"],
    multiplier=MARKET_DATA_SEARCH_QUERY_MULTIPLIER,
    timespan=request["interval"],
    from_=request["start_date"],
    to=request["end_date"]
  ):
    response_aggregates.append(aggregate)
    
  closing_price_dates, closing_prices = process_market_data_response(response_aggregates)
  
  return closing_price_dates, closing_prices