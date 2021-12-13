#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import unittest
from unittest.mock import MagicMock, NonCallableMock, patch

from flog import flog  # SUT


def my_fun(*args, **kwargs):
    return sum(args)


@patch("flog.flog.logging")
class TestLogCall(unittest.TestCase):
    def setUp(self):
        self.logger = NonCallableMock()
        # self.logger.debug = MagicMock()

    def instance_method(self, *args, **kwargs):
        return sum(args)

    def test_log_call_logs(self, logging):
        """flog.flog.log_call: Logs a basic call without args or kwargs"""

        flog.log_call(self.logger)(my_fun)()  # SUT

        self.logger.debug.assert_any_call("flog.tests.test_log_call.my_fun: args: (), kwargs: {}")
        self.logger.debug.assert_any_call("flog.tests.test_log_call.my_fun: returns: 0")

    def test_log_call_logs_with_args(self, logging):
        """flog.flog.log_call: Logs a basic call with args"""

        randoa = random.randint(0, 500)
        randob = random.randint(0, 500)
        randoc = random.randint(0, 500)

        flog.log_call(self.logger)(my_fun)(randoa, randob, randoc)  # SUT

        self.logger.debug.assert_any_call(
            "flog.tests.test_log_call.my_fun: args: ({}, {}, {}), kwargs: {}".format(randoa, randob, randoc, "{}")
        )
        self.logger.debug.assert_any_call(
            "flog.tests.test_log_call.my_fun: returns: {}".format(randoa + randob + randoc)
        )

    def test_log_call_logs_with_kwargs(self, logging):
        """flog.flog.log_call: Logs a basic call with args and kwargs"""

        randoa = random.randint(0, 500)
        randob = random.randint(0, 500)
        randoc = random.randint(0, 500)

        flog.log_call(self.logger)(my_fun)(randoa, randob, randoc, random_frippery_scale=32)  # SUT

        self.logger.debug.assert_any_call(
            "flog.tests.test_log_call.my_fun: args: ({}, {}, {}), kwargs: {rfs}".format(
                randoa, randob, randoc, rfs="{'random_frippery_scale': 32}"
            )
        )
        self.logger.debug.assert_any_call(
            "flog.tests.test_log_call.my_fun: returns: {}".format(randoa + randob + randoc)
        )

    def test_log_call_logs_instance_method_with_kwargs(self, logging):
        """flog.flog.log_call: Logs a instance method call with args and kwargs"""

        randoa = random.randint(0, 500)
        randob = random.randint(0, 500)
        randoc = random.randint(0, 500)

        flog.log_call(self.logger)(self.instance_method)(randoa, randob, randoc, random_frippery_scale=32)  # SUT

        self.logger.debug.assert_any_call(
            "flog.tests.test_log_call.TestLogCall.instance_method: args: ({}, {}, {}), kwargs: {rfs}".format(
                randoa, randob, randoc, rfs="{'random_frippery_scale': 32}"
            )
        )
        self.logger.debug.assert_any_call(
            "flog.tests.test_log_call.TestLogCall.instance_method: returns: {}".format(randoa + randob + randoc)
        )

    def test_log_call_accepts_callable(self, logging):
        """flog.flog.log_call: Accepts a callable and calls it as if it were a logger function"""

        my_logger = MagicMock()

        randoa = random.randint(0, 500)
        randob = random.randint(0, 500)
        randoc = random.randint(0, 500)

        flog.log_call(my_logger)(self.instance_method)(randoa, randob, randoc, random_frippery_scale=32)  # SUT

        my_logger.assert_any_call(
            "flog.tests.test_log_call.TestLogCall.instance_method: args: ({}, {}, {}), kwargs: {rfs}".format(
                randoa, randob, randoc, rfs="{'random_frippery_scale': 32}"
            )
        )
        my_logger.assert_any_call(
            "flog.tests.test_log_call.TestLogCall.instance_method: returns: {}".format(randoa + randob + randoc)
        )


@patch("flog.flog.logging")
class TestLogSensitiveCall(unittest.TestCase):
    def setUp(self):
        self.logger = NonCallableMock()

    def test_log_call_logs(self, logging):
        """flog.flog.log_sensitive_call: Discreetly logs a basic call without args or kwargs"""

        flog.log_sensitive_call(self.logger)(my_fun)()  # SUT

        self.logger.debug.assert_any_call("flog.tests.test_log_call.my_fun: args: *XXXXXX, kwargs: **XXXXXXX")
        self.logger.debug.assert_any_call("flog.tests.test_log_call.my_fun: returns: XXXXXXXXXX")

    def test_log_call_logs_with_args(self, logging):
        """flog.flog.log_sensitive_call: Discreetly logs a basic call with args"""

        randoa = random.randint(0, 500)
        randob = random.randint(0, 500)
        randoc = random.randint(0, 500)

        flog.log_sensitive_call(self.logger)(my_fun)(randoa, randob, randoc)  # SUT

        self.logger.debug.assert_any_call("flog.tests.test_log_call.my_fun: args: *XXXXXX, kwargs: **XXXXXXX")
        self.logger.debug.assert_any_call("flog.tests.test_log_call.my_fun: returns: XXXXXXXXXX")

    def test_log_call_logs_with_kwargs(self, logging):
        """flog.flog.log_sensitive_call: Discreetly logs a basic call with args and kwargs"""

        randoa = random.randint(0, 500)
        randob = random.randint(0, 500)
        randoc = random.randint(0, 500)

        flog.log_sensitive_call(self.logger)(my_fun)(randoa, randob, randoc, random_frippery_scale=32)  # SUT

        self.logger.debug.assert_any_call("flog.tests.test_log_call.my_fun: args: *XXXXXX, kwargs: **XXXXXXX")
        self.logger.debug.assert_any_call("flog.tests.test_log_call.my_fun: returns: XXXXXXXXXX")

    def test_log_call_accepts_callable(self, logging):
        """flog.flog.log_sensitive_call: Accepts a callable and calls it as if it were a logger function"""

        my_logger = MagicMock()

        randoa = random.randint(0, 500)
        randob = random.randint(0, 500)
        randoc = random.randint(0, 500)

        # SUT
        flog.log_sensitive_call(my_logger)(my_fun)(randoa, randob, randoc, random_frippery_scale=32)

        my_logger.assert_any_call("flog.tests.test_log_call.my_fun: args: *XXXXXX, kwargs: **XXXXXXX")
        my_logger.assert_any_call("flog.tests.test_log_call.my_fun: returns: XXXXXXXXXX")
