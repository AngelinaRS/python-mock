# -*- coding: utf-8 -*-
import os
import os.path
import sys

def name_given_by_the_user(): #This saves the name of the file that the user gives
	insert_name = raw_input("Insert the name of file: ")
	return insert_name

def create(insert_name):  #This creates a file
	if os.path.isfile(insert_name+".txt") == False:
		open((insert_name+".txt"), "w").close()
def remove(insert_name): #This removes the file
	if os.path.isfile(insert_name+".txt") == True:
		os.remove(insert_name+".txt")

def verificate_file(insert_name):#This verificates if is file
	return os.path.isfile(insert_name+".txt")

def file_exists_create():
	name = name_given_by_the_user() #This saves the function of the name given by the user
	exists = verificate_file(name)  #This saves the function that saves if is file

	if exists == False: #If the name given by the user is file
		print "The file don't exists"
		print "Can create it"
		create(name)
	else:
		print "The file exists"
		print "Can't create it"
		menu()
def file_exists_remove():
	name = name_given_by_the_user()
	exists = verificate_file(name)

	if exists == True:
		print "The file exists"
		print "Can remove it"
		remove(name)
	else:
		print "The file don't exist"
		print "Can't remove it"
		menu()


def menu(): #This saves the menu
	print ""
	print "Welcome to Creator and Remover of files"
	print ""
	print "Insert 1 to create file"
	print ""
	print "Insert 2 to remove file"
	answer_menu = True
	while answer_menu == True:
		choose_user = raw_input(" - ") #This saves the election of the user
		if choose_user == "1":
			file_exists_create()
		elif choose_user == "2":
			file_exists_remove()
		else:
			print "Election invalid"

menu()
