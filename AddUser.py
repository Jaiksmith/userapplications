#!/usr/bin/python3
import sys, os

## Ask for input
user = input("What is the username to add? ")
password = input("What is password for new user? ")
email = input("What is the email address of the user? ")
directory = "/home/"+ user + "/.ssh/"

## Check to see if ssh directory exists/create ssh directory
if not os.path.exists(directory):
    os.makedirs(directory)
    
## Create function to add user
def createuser(user):
    print("Creating user: "+ user + " : " + password)
    os.system("useradd -m -p " +password+ " "+ user)
    os.system("ssh-keygen -t rsa -b 4096 -C " + email + " -f /home/" + user + "/.ssh/id_rsa")

## Execute Add User Function
createuser(user)

