# finance_apis
A few freely-available finance APIs.

1. Install requirements.
```
pip install -r requirements.txt
```

1. Get some stock tickers from Quandl.
```
from common.quandl import Quandl

# there's already a .csv file in the data directory
# otherwise a new .csv will be downloaded from Quandl
q = Quandl('data/WIKI-datasets-codes.csv')
```

2. Query Alpha Vantage for historical prices. Get an API key at https://www.quandl.com/.
```
from common.alpha_vantage import AlphaVantage

# to get Python dictionaries back
av = AlphaVantage('API_KEY', 'dict')

# to get JSON strings back
av = AlphaVantage('API_KEY', 'json')

# to get Pandas dataframe back
av = AlphaVantage('API_KEY', 'dataframe')

# get intraday quotes
av.get_intraday_stock_quotes('AAPL', '1min')

# get daily quotes
av.get_daily_stock_quotes('GOOG')
```
