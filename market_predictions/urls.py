from django.urls import path, include
from market_predictions.views import MarketPredictionsGenerateDaily, MarketPredictionsGenerateTwoWeeks

urlpatterns = [
  path("generate_daily/", MarketPredictionsGenerateDaily.as_view(), name="market-predictions-daily"),
  path("generate_two_weeks/", MarketPredictionsGenerateTwoWeeks.as_view(), name="market-predictions-two-weeks")
]
