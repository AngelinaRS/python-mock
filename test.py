#!/usr/bin/env python
# -*- coding: utf-8 -*-

import application
import mock
import unittest

class Test_application(unittest.TestCase):

	@mock.patch('application.os.path')
	@mock.patch('__builtin__.open')

	def test_exists_file_create(self, mock_open, mock_path):
		mock_path.isfile.return_value == True
		self.assertFalse(mock_open.called, "File exists, can't create it")

	@mock.patch('application.os.path')
	@mock.patch('__builtin__.open')

	def test_not_exist_file_create(self, mock_open, mock_path):
		mock_path.isfile.return_value == False
		application.create("file_name")
		mock_open.assert_called_with("file_name", "w")

	@mock.patch('application.os.path')
	@mock.patch('application.os')

	def test_exists_file_remove(self, mock_os, mock_path):
		mock_path.isfile.return_value = True
		application.remove("file_name")
		mock_os.remove.assert_called_with("file_name")

	@mock.patch('application.os.path')
	@mock.patch('application.os')

	def test_not_exist_file_remove(self, mock_os, mock_path):
		mock_path.isfile.return_value = False
		self.assertFalse(mock_os.remove.called, "Can't create the file")

if __name__ =="__main":
	unittest.main()