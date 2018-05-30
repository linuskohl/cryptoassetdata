import os
import sys
import csv
import json
import requests
import urllib.robotparser
from urllib.parse import urlencode
from lxml import etree
from lxml.etree import tostring
from lxml.html import parse
from lxml.cssselect import CSSSelector
import logging

class downloader:
    _user_agent = 'Chrome'
    # Base URL
    _base_url = 'https://coinmarketcap.com/'
    # API URL
    _api_url = 'https://api.coinmarketcap.com/'

    def __init__(self):
        self.logger = logging.getLogger('cryptoassetdata')
        self.request_headers = {
            'User-Agent': self._user_agent,
        }

        self.robots = urllib.robotparser.RobotFileParser()
        self.robots.set_url(self._base_url + 'robots.txt')
        self.robots.read()

    def get_historic_data(self, slug, start_date, end_date):
        self.logger.info("Fetching {} from CoinMarketCap".format(slug))
        params = {}
        params['end'] = end_date.strftime("%Y%m%d")
        params['start'] = start_date.strftime("%Y%m%d")
        qstr = urlencode(params)
        url = self._base_url + "currencies/" + slug + "/historical-data/" + '?' + qstr

        if self.robots.can_fetch("*", url):
            response = requests.get(url, headers=self.request_headers)
            if response.status_code == 200:
                return response.content
        else:
            self.logger.critical("Blocked by robots.txt")
        return None

    def get_listings(self):
        url = self._api_url + "v2/listings/"
        response = requests.get(url, headers=self.request_headers)
        if response.status_code == 200:
            return response.content
        return None
