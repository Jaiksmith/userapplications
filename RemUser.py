#!/usr/bin/python3
import sys, os

## Ask for input
user = input("What is the username to remove? ")

## Create function to remove user/revoke ssh
def delUser(user):
    os.system("userdel " + user)

## Execute remove/revoke function
delUser(user)
