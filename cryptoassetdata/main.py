import dateparser
from datetime import datetime, timedelta
import pandas as pd
from threading import Thread
from cryptoassetdata.lib.extractor import extractor
from cryptoassetdata.lib.logging import init_logger
from cryptoassetdata.lib.cache import store_to_cache, load_from_cache, clear_cache, assure_path_exists


_min_start_date = datetime.strptime('04/28/2013', '%m/%d/%Y')
_max_end_date = datetime.today() - timedelta(days=1)
logger = init_logger('cryptoassetdata')


def _fix_dates(start_date, end_date):
    """Set start and end dates to valid range"""
    if not start_date or dateparser.parse(start_date) < _min_start_date:
        start_date = _min_start_date
    else:
        start_date = dateparser.parse(start_date)
    if not end_date or dateparser.parse(end_date) > _max_end_date:
        end_date = _max_end_date
    else:
        end_date = dateparser.parse(end_date)
    return start_date, end_date


def _get_historic_data(result, slug, start_date=None, end_date=None, extr=None):
    """Get historic data for slug and stores the DataFrame in results.
       If the asset is not already cached, load it from CoinMarketCap and add it to cache."""
    if not slug:
        logger.error("No slug specified")
        return None

    if not extr:
        extr = extractor()

    # Try to load data from cache
    data = load_from_cache(slug, start_date, end_date)
    if isinstance(data, pd.DataFrame):
        # Data loaded from cache
        result[slug] = data
        return
    else:
        # Data not found in cache
        data = extr.get_historic_data(slug, start_date, end_date)
        if isinstance(data, pd.DataFrame):
            store_to_cache(slug, start_date, end_date, data)
            result[slug] = data
        return

def get_historic_data(slugs, start_date=None, end_date=None, fill_na=False):
    """Gets historic data for asset/s in slugs."""

    if not isinstance(slugs, list):
        slugs = [slugs]

    extr = extractor()  # share extractor
    results = {}  # store results in dict
    threads = []

    # Fix dates
    start_date, end_date = _fix_dates(start_date, end_date)

    for slug in slugs:
        t = Thread(target=_get_historic_data, args=(results, slug, start_date, end_date, extr))
        t.start()
        threads.append(t)

    # Wait till every thread finished execution
    for t in threads:
        t.join()

    # Add dates and fill with NaN values if the asset has not been traded
    # from start_date on - or until end_date
    if fill_na:
        dates = pd.date_range(start_date, end_date)
        for slug_name, dataframe in results.items():
            df_tmp = pd.DataFrame(index=dates)
            results[slug_name] = df_tmp.join(dataframe)

    return results

def get_metainfo(slugs):
    # TODO
    pass


def get_slugs():
    return extractor().get_slugs()

