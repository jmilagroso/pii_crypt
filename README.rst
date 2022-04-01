pii\_crypt - PII Crypt
===========================================================

.. image:: https://badge.fury.io/py/pii-crypt.svg
    :target: https://badge.fury.io/py/pii-crypt

.. image:: https://travis-ci.com/jmilagroso/pii_crypt.svg?branch=master
    :target: https://travis-ci.com/jmilagroso/pii_crypt
 
.. image:: https://img.shields.io/lgtm/grade/python/g/jmilagroso/pii_crypt.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/jmilagroso/pii_crypt/context:python

.. image:: https://img.shields.io/lgtm/alerts/g/jmilagroso/pii_crypt.svg?logo=lgtm&logoWidth=18
    :target: https://lgtm.com/projects/g/jmilagroso/pii_crypt/alerts/

.. image:: https://codecov.io/gh/jmilagroso/pii_crypt/branch/master/graph/badge.svg?token=W657M2RVO7
    :target: https://codecov.io/gh/jmilagroso/pii_crypt

.. image:: https://www.codefactor.io/repository/github/jmilagroso/pii_crypt/badge
    :target: https://www.codefactor.io/repository/github/jmilagroso/pii_crypt
    :alt: CodeFactor

.. image:: https://pepy.tech/badge/pii-crypt
   :target: https://pepy.tech/project/pii-crypt

.. image:: https://img.shields.io/badge/python-3.6-blue.svg
    :target: https://www.python.org/downloads/release/python-360/

.. image:: https://img.shields.io/badge/python-3.7-blue.svg
    :target: https://www.python.org/downloads/release/python-370/

|
| Secures Personally Identifiable Information using AES (128/256 bit) key encryption.


Overview
--------

The ``pii_crypt`` was written to help secure sensitive information.


Installation
------------

To download ``pii_crypt``, either fork this github repo
or simply use Pypi via pip.

.. code:: sh

    $ pip install pii-crypt


Usage
-----

.. code:: sh

    from pii_crypt import PIICrypt

    secret_128bit_key = '1234567812345678'

    pc = PIICrypt(secret_128bit_key)

    # Encrypt/Decrypt
    encrypted = pc.encrypt('John Doe')

    print(encrypted)   # VQd0JvSY8PTsszHEURT8xw==

    decrypted = pc.decrypt(encrypted)

    print(decrypted)   # John Doe


Unit Tests
----------

.. code:: sh

     ✘ jay@ThinkPad  ~/pii_crypt   master ±  coverage run --source=. -m unittest
    ....
    ----------------------------------------------------------------------
    Ran 4 tests in 0.002s

    OK


Code Coverage
-------------

.. code:: sh

     ✘ jay@ThinkPad  ~/pii_crypt   master ±  coverage report --omit=setup.py
    Name                     Stmts   Miss  Cover
    --------------------------------------------
    pii_crypt/__init__.py        1      0   100%
    pii_crypt/pii_crypt.py      19      0   100%
    --------------------------------------------
    TOTAL                       20      0   100%


License
-------

MIT License

Copyright (c) 2021

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
