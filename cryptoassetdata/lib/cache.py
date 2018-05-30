import os
from os.path import dirname, abspath, join
import logging
import pickle

logger = logging.getLogger('cryptoassetdata')

_base_dir = dirname(dirname(abspath(__file__)))  # Parent directory
_cache_name = 'cache'
_cache_path = join(_base_dir, _cache_name)


def assure_path_exists(path):
    """Check if cache directory exists, else create it."""
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except:
            logger.error("Could not create directory {}".format(dir))
            return False
    return True


def _generate_cache_filename(slug, start_date, end_date):
    """Generate filename"""
    return "{}-{}-{}".format(slug, start_date.strftime("%Y_%m_%d"), end_date.strftime("%Y_%m_%d"))


def load_from_cache(slug, start_date, end_date):
    """Try to load DataFrame from cache, depending on slug,start_date,end_date"""
    cache_name = _generate_cache_filename(slug, start_date, end_date)
    cache_file_name = join(_cache_path, cache_name)
    if cache_name and os.path.exists(cache_file_name):
        with open(cache_file_name, 'rb') as file:
            try:
                data = pickle.load(file)
                logger.info("{} [{}->{}] loaded from cache".format(slug, start_date.date(), end_date.date()))
                return data
            except:
                logger.info("Cache missed for {}".format(slug))
    return None


def store_to_cache(slug, start_date, end_date, data):
    """Store DataFrame for slug, dependent on slug,start_date,end_date in cache."""
    cache_name = _generate_cache_filename(slug, start_date, end_date)
    cache_file_name = join(_cache_path, cache_name)
    if assure_path_exists(_cache_path):
        with open(cache_file_name, 'wb') as file:
            logger.info("{} [{}->{}] stored to cache".format(slug, start_date.date(), end_date.date()))
            pickle.dump(data, file)
            return True
    return False


def clear_cache():
    """Clear cached DataFrames"""
    logger.info("Cleaning cache")
    for file in os.listdir(_cache_path):
        logger.debug("Removing cache {}".format(file))
        file_path = os.path.join(_cache_path, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            logger.error(e)
