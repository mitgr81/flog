#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import unittest

from mock import patch
from nose.tools import assert_equals

from flog import flog  # SUT

@patch('flog.flog.logging')
class TestGetLogger(unittest.TestCase):

    def test_get_logger_gets_logger(self, logging):
        """flog.flog.get_logger: Gets a logger from the standard library"""
        name = random.choice(['bunny', 'ninja', 'soup.pants.mcgillicutty'])

        actual = flog.get_logger(name)

        logging.getLogger.assert_called_once_with(name)
        self.assertEqual(logging.getLogger.return_value, actual)


    def test_get_logger_adds_null_handler(self, logging):
        """flog.flog.get_logger: Adds a null logger to the logger in question, avoiding "Unconfigured logger" exceptions """
        actual = flog.get_logger('_')
        logging.getLogger.return_value.addHandler.assert_called_once_with(logging.NullHandler())
