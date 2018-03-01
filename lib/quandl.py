"""
https://www.quandl.com/docs-and-help
"""
import pandas
from simple_terminal import Terminal


class Quandl(object):
    def __init__(self, source_csv):
        # set destination of WIKI-datasets-codes.csv
        self.source_csv = source_csv
        # if file does not exist, download it
        with Terminal() as t:
            if not t.command('ls {}'.format(source_csv)):
                self._download_wiki_csv(self.source_csv)

        # create ticker dataframe
        self.ticker_dataframe = self._create_dataframe()

    def _download_wiki_csv(self, destination=None):
        """
        Gets a CSV with columns - ticker, description
        """
        with Terminal() as t:
            # temp filename

            # download zipped tickers
            t.command(
                'wget https://www.quandl.com/api/v3/databases/WIKI/codes'
            )
            # unzip file
            t.command(
                'unzip codes'
            )
            # move to data directory
            if destination:
                t.command(
                    'mv WIKI-datasets-codes.csv {}'.format(destination)
                )
            # clean up files
            t.command('rm codes')

    def _create_dataframe(self):
        """
        Retrieves tickers and descriptions from WIKI-datasets-codes.csv
        """
        return pandas.read_csv(
            self.source_csv,
            names=['ticker', 'description']  # set header names
        )

    @property
    def tickers(self):
        """
        Return a list of tickers.
        """
        # remove string 'WIKI/' from list of tickers
        return [
            x.replace('WIKI/', '')
            for x in self.ticker_dataframe['ticker'].tolist()
        ]
