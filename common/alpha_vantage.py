"""
https://www.alphavantage.co/documentation/
"""

import json
import pandas
import requests


class AlphaVantage(object):
    def __init__(self, api_key, data_format='dict', remove_metadata=True):
        """
        Initialize object to return data of format:
            - Python dictionary
            - JSON
            - Pandas dataframe

        :param api_key: API key (string)
        :param data_format: choices - 'dict', 'json', 'dataframe' (string)
        :param remove_metadata: True to remove metadata from reponse (bool)
        """
        self.api_key = api_key
        self.data_format = data_format
        self.remove_metadata = remove_metadata

    def _remove_metadata(self, data):
        """
        Remove 'Meta Data' key and values from reponse.
        """
        # remove Meta Data key/value pair
        data.pop('Meta Data', None)

        # move data up one level
        data = data[next(iter(data))]

        return data

    def _format_data(self, data):
        """
        Return formatted data based on self.data_format

        :param data: data in Python dictionary format
        :return: data in desired format (dict, JSON, Pandas dataframe)
        """
        if self.remove_metadata:
            data = self._remove_metadata(data)

        if self.data_format == 'dict':
            return data

        if self.data_format == 'json':
            return json.dumps(data)

        if self.data_format == 'dataframe':
            return pandas.read_json(json.dumps(data))

    def get_intraday_stock_quotes(self, symbol, interval_size):
        """
        Return stock interval data.

        Returned data includes:
            - open
            - high
            - low
            - close
            - volume

        :param symbol: stock ticker symbol (string)
        :param interval_size: choices - '1min', '5min', '15min', '30min',
            '60min' (string)
        :param api_key: API key (string)
        :return: historical stock data (dict)
        """
        r = requests.get('https://www.alphavantage.co/query'
                         '?function=TIME_SERIES_INTRADAY&symbol={}&interval={}'
                         '&apikey={}'.format(
                            symbol, interval_size, self.api_key))

        return self._format_data(r.json())

    def get_daily_stock_quotes(self, symbol):
        """
        Return stock interval data.

        Returned data includes:
            - open
            - high
            - low
            - close
            - volume

        :param symbol: stock ticker symbol (string)
        :param api_key: API key (string)
        :return: historical stock data (JSON)
        """
        r = requests.get('https://www.alphavantage.co/query'
                         '?function=TIME_SERIES_DAILY&symbol={}'
                         '&apikey={}'.format(symbol, self.api_key))

        return self._format_data(r.json())
