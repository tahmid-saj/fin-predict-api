from django.urls import path, include
from market_data.views import MarketDataGenerate

urlpatterns = [
  path("generate/", MarketDataGenerate.as_view(), name="market-data"),
]