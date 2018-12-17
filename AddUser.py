#!/usr/bin/python3
import sys, os

## Ask for input
user = input("What is the username to add? ")
key = input("What is Public SSH for new user? ")
comment = input("Type UID/Comment for user: ")

## Create function to add user
def createuser():
    ## Create User Account
    os.system("useradd -m " + user + " -p " + key + " -c " + comment)
    ## Input Public SSH Key
    os.system("mkdir -p /home/" + user + "/.ssh && echo " + key + " >> /home/" + user + "/.ssh/id_rsa.pub")

## Execute Add User Function
createuser()

