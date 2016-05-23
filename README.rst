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

(`new in version 0.1.0`) In production environments, you may wish to run with the environment variable ``FLOG_NOWRAP`` set truthy.  This will make ``flog.log_call`` and ``flog.log_sensitive_call`` exit as quickly as possible and not attempt to emit DEBUG-level statements.  This can also be accomplished by running the interpreter in "optimized" mode (``python -O <your entry>`` or by setting the ``PYTHONOPTIMIZE`` environment variable)

(`new in version 0.2.0`) ``flog.log_call`` and ``flog.log_sensitive_call`` both now optionally take a callable that will be called with logger-compatible arguments.  Suggested uses would be to log at a higher-than-debug level, or piping into another stream handler.


License
=======
This software is hereby released under the MIT License, as seen in the LICENSE file

.. |BuildImage| image:: https://secure.travis-ci.org/mitgr81/flog.png
.. _BuildImage: https://travis-ci.org/mitgr81/flog
.. _PyPI: http://pypi.python.org/pypi/flog
