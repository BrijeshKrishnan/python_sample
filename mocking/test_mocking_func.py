import os
import sys
from unittest import TestCase
sys.path.append(os.path.join((os.path.dirname(__file__))))
from mocking_func import MockSample
from unittest.mock import patch
class TestMocking(TestCase):
    def setUp(self):
        self.object = MockSample()
    def test_sum(self):
        answer = self.object.sum(2, 4)
        self.assertEqual(answer, 6)

    @patch('mocking_func.MockSample.sum_mock', return_value=9)
    def test_sum_mock(self, sum_mock):
        self.assertEqual(sum_mock(2,3), 9)