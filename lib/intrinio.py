"""
http://docs.intrinio.com/#introduction
"""

import requests
from requests.auth import HTTPBasicAuth


class Intrinio(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get_company_financials(
        self,
        symbol,
        statement,
        fiscal_year,
        fiscal_period
    ):
        """
        Return company financials.

        :param symbol: stock ticker symbol (string)
        :param statement: choices - 'income_statement', 'balance_sheet',
            'cash_flow_statement', 'calculations' (string)
        :param fiscal_year: YYYY format year (string)
        :param fiscal_period: choices - 'FY', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1TTM',
            'Q2TTM', 'Q3TTM', 'Q2YTD', 'Q3YTD' (string)
        :return: company financials (JSON)
        """
        r = requests.get('https://api.intrinio.com/financials/'
                         'standardized?identifier={symbol}&'
                         'statement={statement}&'
                         'fiscal_year={fiscal_year}&'
                         'fiscal_period={fiscal_period}'.format(
                            symbol=symbol,
                            statement=statement,
                            fiscal_year=fiscal_year,
                            fiscal_period=fiscal_period
                         ), auth=HTTPBasicAuth(self.username, self.password))

        return r.json()
