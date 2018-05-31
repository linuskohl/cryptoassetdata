================
cryptoassetdata
================


|release| |pypi| |license|

Python module to fetch historic crypto asset market data from `CoinMarketCap <https://coinmarketcap.com/>`_.
To reduce traffic extracted data is cached. Furthermore loading the required pages is threaded for performance improvement. Returns Pandas DataFrames with dates as index. As symbols are *not* unique, the *website slug* is used.

Documentation
=============

See `requirements.txt <https://github.com/linuskohl/cryptoassetdata/blob/master/requirements.txt>`_
file for additional dependencies:

* Python_ 3.x
* dateparser_
* Pandas_
* requests_
* lxml_

Installation
------------------

Pip Installation:
::

    $ pip install cryptoassetdata

To install from source:
::

    $ git clone https://github.com/linuskohl/cryptoassetdata
    $ pip install -r requirements.txt
    $ python setup.py install

Usage
-----

Sample code to plot Ethereums Open data

.. code-block:: python

    import cryptoassetdata
    import matplotlib.pyplot as plt

    def available_assets():
        # As Symbols are not unique, the website slugs are used.
        # Get a list of available crypt assets
        print(cryptoassetdata.get_slugs())

    def plot_ethereum_price():
        # get_historic_data takes an array containing asset slugs, start and end date of the data.
        # fill_na specifies if the DataFrame contains only dates the assets were traded, or every date
        # in the specified date range. A dictionary containing a DataFrame for every is returned.
        data = cryptoassetdata.get_historic_data(["ethereum"], "01/01/2017", "12/31/2017", fill_na=True)
        ethereum = data['ethereum'].Open # Get open data from Ethereum
        ethereum.plot()
        plt.show() # Display plot



Contribute
----------
- Source Code: https://github.com/linuskohl/cryptoassetdata
- Issue Tracker: https://github.com/linuskohl/cryptoassetdata/issues

Changelog
------------------

Please see the `CHANGES.txt
<https://github.com/linuskohl/cryptoassetdata/blob/master/CHANGES.txt>`__ for a list
of all changes.


License
-------

The project is licensed under the GPLv3 License. See `LICENSE.txt <https://github.com/linuskohl/cryptoassetdata/blob/master/LICENSE.txt>`_ for more details.

Package Author
--------------
* Linus Kohl <linus@munichresearch.com>

.. |release| image:: https://img.shields.io/github/release/linuskohl/cryptoassetdata.svg?style=flat-square
.. |license| image:: https://img.shields.io/github/license/linuskohl/cryptoassetdata.svg?style=flat-square
.. |pypi| image:: https://img.shields.io/pypi/v/cryptoassetdata.svg?style=flat-square

.. _Python: http://www.python.org
.. _Pandas: https://pandas.pydata.org
.. _Dateparser: https://github.com/scrapinghub/dateparser
.. _Requests: http://docs.python-requests.org/en/master/
.. _lxml: http://lxml.de/