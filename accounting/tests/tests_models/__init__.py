import unittest

def suite():
    return unittest.TestLoader().discover("accounting.tests", pattern="*.py")