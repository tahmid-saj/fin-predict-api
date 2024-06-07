from utils.helpers.shared_helpers import convert_unix_msec_to_datetime

def process_market_data_response(market_data_response):
  res_closing_price_dates, res_closing_prices = [], []
  for record in market_data_response:
    res_closing_price_dates.append(str(convert_unix_msec_to_datetime(record.timestamp)))
    res_closing_prices.append(float(record.close))
  
  return res_closing_price_dates, res_closing_prices