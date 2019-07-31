import os
import sys
import unittest
from unittest import TestCase
from unittest.mock import patch
sys.path.append(os.path.join((os.path.dirname(__file__))))
from mocking_example_rem import FileRemove
class FileRemoveTestCase(unittest.TestCase):
    @patch('mocking_example_rem.os.path')
    @patch('mocking_example_rem.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = FileRemove()
        # set up the mock
        mock_path.isfile.return_value = False
        reference.rm("any path")
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        # make the file 'exist'
        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")
      