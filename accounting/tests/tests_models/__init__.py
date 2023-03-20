import unittest

from .test_plan import PlanTestCase


def suite():
    return unittest.TestLoader().discover("accounting.tests", pattern="*.py")