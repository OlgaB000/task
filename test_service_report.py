import unittest
from service.calculations import BasicStatistic


class TestReport(unittest.TestCase):
    def test_get_total(self):
        bs = BasicStatistic([1, 2, 3])
        results = bs.get_total()
        self.assertEqual(6, results)

    def test_get_total_if_there_no_numbers(self):
        bs = BasicStatistic([])
        results = bs.get_total()
        self.assertEqual(0, results)

    def test_get_total_if_there_None_value(self):
        bs = BasicStatistic(None)
        results = bs.get_total()
        self.assertEqual(0, results)