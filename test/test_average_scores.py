"""
Program: test_average_scores.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose:
"""

import unittest
import unittest.mock as mock
from format_output import average_scores as avg


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert avg.average() == 90


if __name__ == '__main__':
    unittest.main()
