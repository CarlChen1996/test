import time
import unittest
from unittest import mock
from ttttt import generate_test_plan,time_now


class TestGenerateTestPlan(unittest.TestCase):
    @mock.patch('ttttt.time_now')
    def test_generate_test_plan(self,mock_time):
        # lst = [time.time(), time.time(), 1]
        mock_time.return_value = time.time()
        duration = generate_test_plan(5)
        print(duration)
        self.assertEqual(duration, 0)


if __name__ == '__main__':
    unittest.main()
