import json
import lxml
from datetime import datetime
import pandas as pd
import numpy as np
from lxml import etree
from lxml.etree import tostring
from lxml.html import parse
from .downloader import downloader
import logging


class extractor:
    # XPath to select table body
    _selector_data_xpath = '//*[@id = "historical-data"]//table/tbody'
    # Names of columns in table
    _column_names = ['Open', 'High', 'Low', 'Close', 'Volume', 'Marketcap']

    def __init__(self):
        self.logger = logging.getLogger('cryptoassetdata')
        self.downloader = downloader()

    def get_listings(self):
        """Returns parsed JSON data from API"""
        api_response = self.downloader.get_listings()
        if api_response:
            json_data = json.loads(api_response.decode('utf-8'))
            if 'data' in json_data:
                return json_data['data']

    def get_slugs(self):
        """Returns a list of available slugs"""
        listings = self.get_listings()
        if listings:
            return [d['website_slug'] for d in listings if 'website_slug' in d]
        self.logger.error("Failed to get listings")
        return None

    def _clean_to_float(self, value):
        """Try to load float from string or return NaN"""
        try:
            value = value.replace(',', '')  # Remove commata
            return float(value)
        except:
            # For example "-" values
            return np.NaN

    def get_historic_data(self, slug, start_date, end_date):
        # Fetch the content of the page
        page_content = self.downloader.get_historic_data(slug, start_date, end_date)
        if page_content:

            # Initialize DataFrame
            df = pd.DataFrame(columns=self._column_names)

            # Decode page content and parse DOM
            page_content = page_content.decode('utf-8')
            page_root_node = lxml.html.fromstring(page_content)

            # Get table using xpath selector
            table_elements = page_root_node.xpath(self._selector_data_xpath)
            if len(table_elements) > 0:
                table_data = table_elements[0]
                # Iterate over table rows
                for row in table_data:
                    df_row_data = {}
                    tdata = row.getchildren()
                    # Parse date
                    date = tdata[0].text_content()
                    date_parsed = datetime.strptime(date, '%b %d, %Y')

                    # Aggregate data
                    df_row_data['Open'] = self._clean_to_float(tdata[1].text_content())
                    df_row_data['High'] = self._clean_to_float(tdata[2].text_content())
                    df_row_data['Low'] = self._clean_to_float(tdata[3].text_content())
                    df_row_data['Close'] = self._clean_to_float(tdata[4].text_content())
                    df_row_data['Volume'] = self._clean_to_float(tdata[5].text_content())
                    df_row_data['Marketcap'] = self._clean_to_float(tdata[6].text_content())

                    # Append new row to DataFrame
                    df = df.append(pd.DataFrame(df_row_data, index=[date_parsed]), sort=True)

                # Reorder date
                df = df.iloc[::-1]

                # Reorder columns and return
                return df[self._column_names]
