from pytrends.request import TrendReq
import pandas as pd

def get_keyword_trend(keyword):
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload([keyword], cat=0, timeframe='today 3-m', geo='', gprop='')
        data = pytrends.interest_over_time()
        if data.empty:
            return None
        return data[[keyword]]
    except Exception as e:
        return None
