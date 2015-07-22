"""Creator and Remover the files"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
import sys

def reset():
    """This clean the screen"""
    os.system("reset")

def name_given_by_the_user():
    """This saves the name of the file that the user gives"""
    insert_name = raw_input("Enter the name of file: ")
    return insert_name

def verificate_file(insert_name):
    """This verificates if is file"""
    return os.path.isfile(insert_name+".txt")

def create(insert_name):
    """This creates a file"""
    if os.path.isfile(insert_name+".txt") == False:
        open((insert_name+".txt"), "w").close()

def remove(insert_name):
    """This removes the file"""
    if os.path.isfile(insert_name+".txt") == True:
        os.remove(insert_name+".txt")

def file_exists_create():
    """This verificates if the file don't exist to create it"""
    name = name_given_by_the_user() #This saves the function of the name given by the user
    exists = verificate_file(name)  #This saves the function that saves if is file

    if exists == False: #If the name given by the user is file
        reset()
        print "\n\n--It has created the file\n\n"
        create(name)
        raw_input("Press enter to return the menu")
        reset()
        menu()
    else:
        reset()
        print "\n\n--The file exists"
        print "--Can't create it\n\n"
        raw_input("Press Enter to return the menu")
        reset()
        menu()
def file_exists_remove():
    """This verificates if the file exists to remove it"""
    name = name_given_by_the_user()
    exists = verificate_file(name)

    if exists == True:
        reset()
        print "\n\n--It has removed the file"
        remove(name)
        raw_input("\n\nPress enter tu return the menu")
        reset()
        menu()
    else:
        reset()
        print "\n\n--The file don't exist"
        print "--Can't remove it\n\n"
        raw_input("Press Enter to return the menu")
        reset()
        menu()

def menu():
    """This saves the menu"""
    print ""
    print "Welcome to Creator and Remover of files\n"
    print "Insert -1- to create file\n"
    print "Insert -2- to remove file\n"
    print "Insert -3- to quit\n"
    answer_menu = True
    while answer_menu == True:
        choose_user = raw_input(" - ") #This saves the election of the user
        if choose_user == "1":
            reset()
            file_exists_create()
        elif choose_user == "2":
            reset()
            file_exists_remove()
        elif choose_user == "3":
            reset()
            print """\n\n
 ******   **    ** ********
/*////** //**  ** /**///// 
/*   /**  //****  /**      
/******    //**   /******* 
/*//// **   /**   /**////  
/*    /**   /**   /**      
/*******    /**   /********
///////     //    //////// 
\n\n"""
            sys.exit()
        else:
            reset()
            print "*Election invalid, insert one option valid"
menu()

if __name__ == "__main__":
    menu()
