#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import random
import unittest
import uuid
from unittest.mock import patch

from flog import flog  # SUT


@patch("flog.flog.logging")
class TestGetLogger(unittest.TestCase):
    def test_get_logger_gets_logger(self, logging):
        """flog.flog.get_logger: Gets a logger from the standard library"""
        name = random.choice(["bunny", "ninja", "soup.pants.mcgillicutty"])

        actual = flog.get_logger(name)

        logging.getLogger.assert_called_once_with(name)
        self.assertEqual(logging.getLogger.return_value, actual)

    def test_get_logger_adds_null_handler(self, logging):
        """flog.flog.get_logger: Adds a null logger to the logger in question,
        avoiding "Unconfigured logger" exceptions"""
        flog.get_logger("_")
        logging.getLogger.return_value.addHandler.assert_called_once_with(logging.NullHandler())

    def test_get_logger_with_correlation_gets_adapter(self, logging):
        """flog.flog.get_logger: Can optionally wrap the logger with an adapter
        that adds an id to each log record"""
        actual = flog.get_logger("_", add_correlation_id=True)
        self.assertIsInstance(actual, flog.CorrelationLoggerAdapter)


@patch("flog.flog.get_logger")
class TestCorrelationLoggerAdapter(unittest.TestCase):
    def test_adapter_adds_correlation_id(self, get_logger):
        """flog.flog.CorrelationLoggerAdapter.process: Appends provided correlation id to log record"""
        cid = str(uuid.uuid4())
        msg = random.choice(["bunny", "ninja", "soup.pants.mcgillicutty"])
        logger = get_logger("_")

        # SUT
        logger_adapter = flog.CorrelationLoggerAdapter(logger, {"correlation_id": cid})
        logger_adapter.debug(msg)

        logger.log.assert_called_once_with(logging.DEBUG, "[{}] {}".format(cid, msg))
