import unittest
from datetime import datetime, date, time


class PythonDates(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dt = datetime(2011, 10, 29, 20, 30, 21)

    def test_type(self):
        self.assertEqual(29, self.dt.day)
        self.assertEqual(30, self.dt.minute)
        self.assertEqual(date(2011, 10, 29), self.dt.date())
        self.assertEqual(time(20, 30, 21), self.dt.time())

    def test_format(self):
        self.assertEqual('10/29/2011 20:30', self.dt.strftime('%m/%d/%Y %H:%M'))
        self.assertEqual(datetime(2009, 10, 31, 0, 0), datetime.strptime('20091031', '%Y%m%d'))


if __name__ == '__main__':
    unittest.main()
