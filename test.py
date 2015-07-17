import application
import mock
import unittest

class Test_application(unittest.TestCase):

	@mock.patch('application.os.path')
	@mock.patch('__builtin__.open')

	def test_exists_file(self, mock_open, mock_path):
		mock_path.isfile.return_value == True
		application.create("File exists")
		mock_open.assert_called_with("File exists.txt", "w")


