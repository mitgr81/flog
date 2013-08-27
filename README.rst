flog
====

Fast access to some simple python logging tricks

|BuildImage|_

.. image:: https://pypip.in/v/flog/badge.png
    :target: https://crate.io/packages/flog/
    :alt: Latest PyPI version

.. image:: https://pypip.in/d/flog/badge.png
    :target: https://crate.io/packages/flog/
    :alt: Number of PyPI downloads


Installation
============

Either find flog on PyPI_ or install it with pip or easy_install
::

  pip install flog
  #or
  easy_install flog

Basic Usage
===========

Getting a logger: ``import flog``, get a logger with ``flog.get_logger(__name__)``

Logging calls: in and out  Get a logger, decorate functions with ``flog.log_call(<your logger>)``

Logging calls with sensitive args (such as passwords): Get a logger, decorate functions with ``flog.log_sensitive_call(<your logger>)``


License
=======
This software is hereby released under the MIT License, as seen in the LICENSE file

.. |BuildImage| image:: https://secure.travis-ci.org/mitgr81/flog.png
.. _BuildImage: https://travis-ci.org/mitgr81/flog
.. _PyPI: http://pypi.python.org/pypi/flog
