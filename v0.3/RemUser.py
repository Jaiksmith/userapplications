#!/usr/bin/python3
import sys, os

## Ask for input
user = input("What is the username to remove? ")
directory = "/home/backup"

## Create function to remove user/revoke ssh
def delUser(user):
    print ("Deleting user: " + user)
    os.system("userdel " + user)
    print ("Revoke ssh key for: " + user)
    os.system("rm -r /home/" + user + "/.ssh/")

## Execute remove/revoke function
delUser(user)


## Check to see if backup directory exists/create backup directory
if not os.path.exists(directory):
    os.makedirs(directory)

## Move user directory/files to backup directory
def usercopy(user):
    print ("Relocating " + user + " directory")
    os.system("mv /home/" + user + "/ /home/backup/" + user)

## Execute relocation function
usercopy(user)
