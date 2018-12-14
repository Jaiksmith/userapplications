#!/usr/bin/python3
import sys, os

## Ask for input
user = input("What is the username to remove? ")

## Create function to remove user
def delUser(user):
    print ("Deleting user: " + user)
    os.system("userdel " + user)

delUser(user)
