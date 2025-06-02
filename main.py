from pytrends.request import TrendReq

def get_keyword_trend(keyword):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([keyword], cat=0, timeframe='now 7-d', geo='', gprop='')
    data = pytrends.interest_over_time()
    if data.empty:
        return None
    return data[[keyword]]
