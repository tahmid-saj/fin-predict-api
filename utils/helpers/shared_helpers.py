from datetime import datetime

def convert_unix_msec_to_datetime(unix_msec_ts):
  res_datetime = datetime.fromtimestamp(unix_msec_ts / 1000.0)
  return res_datetime