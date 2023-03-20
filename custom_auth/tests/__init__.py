import unittest


def suite():
    return unittest.TestLoader().discover("custom_auth.tests", pattern="*.py")