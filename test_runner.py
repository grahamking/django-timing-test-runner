
import time
import operator

from django.utils.unittest import TestSuite
from django_jenkins.runner import CITestSuiteRunner

TIMINGS = {}


def time_it(func):

    def _inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        TIMINGS[unicode(func)] = end - start

    return _inner


class TimingSuite(TestSuite):
    """TestSuite wrapper that times each test.
    """

    def addTest(self, test):                            # pylint: disable=C0103
        test = time_it(test)
        super(TimingSuite, self).addTest(test)


class TimeRunner(CITestSuiteRunner):
    """Extend django_jenkins's test runner to time the tests.
    """

    def build_suite(self, test_labels, extra_tests=None, **kwargs):
        suite = super(TimeRunner, self).build_suite(
                test_labels, extra_tests=extra_tests, **kwargs)
        return TimingSuite(suite)

    def teardown_test_environment(self, **kwargs):
        super(TimeRunner, self).teardown_test_environment(**kwargs)
        by_time = sorted(
                TIMINGS.iteritems(),
                key=operator.itemgetter(1),
                reverse=True)[:10]
        print("Ten slowest tests:")
        for func_name, timing in by_time:
            print("{t:.2f}s {f}".format(f=func_name, t=timing))
