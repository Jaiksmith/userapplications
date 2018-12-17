#!/usr/bin/python3
import os

def lisUser():
    print ("This is a current list of users on this system: ")
    os.system("bash -c \"eval getent passwd {$(awk '/^UID_MIN/ {print $2}' /etc/login.defs)..$(awk '/^UID_MAX/ {print $2}' /etc/login.defs)} | cut -d: -f1\"")
    
lisUser()
