#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path
import sys

def name_given_by_the_user():
	insert_name = raw_input("Insert the name of file: ")
	return insert_name

def create(file_name):  #This creates a file
	file_name = open(file_name+".txt", "w")
	file_name.close()

def verificate_file(insert_name):
	return os.path.isfile(insert_name)
def file_exists():
	name = name_given_by_the_user()
	exists = verificate_file(name)
	if exists == True:
		print "the file exists"
		menu()
	else:
		print "the file don't exists"
		create(name)

def menu():
	print ""
	print "Welcome to files creator"
	print ""
	file_exists()
menu()

