================
cryptoassetdata
================


|release| |pypi| |license|

Python module to fetch historic crypto asset market data from `CoinMarketCap <https://coinmarketcap.com/>`_.
To reduce traffic extracted data is cached. Furthermore loading the required pages is threaded for performance improvement. Returns Pandas DataFrames with dates as index. 

Documentation
=============

See `requirements.txt <https://github.com/linuskohl/cryptoassetdata/blob/master/requirements.txt>`_
file for additional dependencies:

* Python 3.3 or higher
* dateparser
* Pandas
* requests
* lxml

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


.. |release| image:: https://img.shields.io/github/release/linuskohl/cryptoassetdata.svg?style=flat-square 
.. |license| image:: https://img.shields.io/github/license/linuskohl/cryptoassetdata.svg?style=flat-square 
.. |pypi| image:: https://img.shields.io/pypi/v/cryptoassetdata.svg?style=flat-square::
