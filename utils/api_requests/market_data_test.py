from polygon import RESTClient
import os
from dotenv import load_dotenv

load_dotenv()

client = RESTClient(api_key=os.getenv("POLYGON_API_KEY"))

ticker = "X:BTCUSD"

aggs = []
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="day", from_="2023-01-01", to="2023-06-13", limit=50000):
  aggs.append(a)

print(aggs)