from services.mongodb.mongodb import create_mongodb_connection, close_mongodb_connection
from utils.constants.market_predictions_constants \
  import BTC_FORECAST_DB_NAME, BTC_FORECAST_DAILY_PREDICTION_COLLECTION, BTC_FORECAST_2_WEEK_PREDICTION_COLLECTION
from datetime import datetime, timedelta

def request_market_predictions_daily():
  # create connection
  mongodb_client_connection = create_mongodb_connection()
  btc_forecast_db = mongodb_client_connection[BTC_FORECAST_DB_NAME]
  collection = btc_forecast_db[BTC_FORECAST_DAILY_PREDICTION_COLLECTION]
  
  closing_price = []
  for prediction in collection.find({
    "current_date": str(datetime.today().strftime("%Y-%m-%d"))
  },{ 
      "_id": 0, 
      "prediction": 1
  }):
    closing_price.append(prediction['prediction']['prediction_price'])
  
  # close connection
  close_mongodb_connection(mongodb_client_connection)
  
  return round(closing_price[0], 2)

def request_market_predictions_two_weeks():
  # create connection
  mongodb_client_connection = create_mongodb_connection()
  btc_forecast_db = mongodb_client_connection[BTC_FORECAST_DB_NAME]
  collection = btc_forecast_db[BTC_FORECAST_2_WEEK_PREDICTION_COLLECTION]
  
  closing_price_dates, closing_prices = [], []
  predictions = []
  
  for prediction in collection.find({
      "current_date": str(datetime.today().strftime("%Y-%m-%d"))
    },{ 
        "_id": 0, 
        "predictions": 1
    }): 
    predictions = prediction["predictions"]

  for prediction in predictions:
    closing_price_dates.append(prediction["prediction_date"])
    closing_prices.append(round(prediction["prediction_price"], 2))

  # close connection
  close_mongodb_connection(mongodb_client_connection)
  
  return closing_price_dates, closing_prices