#!/usr/bin/python3
import sys, os

## Ask for input
user = input("What is the username to add? ")
password = input("What is password for new user? ")

## Create function to add user
def createuser(user):
    print("Creating user: "+ user + " : " + password)
    os.system("useradd -m -p " +password+ " "+ user)

## Run Function
createuser(user)

