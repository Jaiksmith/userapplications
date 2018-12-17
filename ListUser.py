#!/usr/bin/python3
import os

def listUser():
    ## List username:UID/Comment
    os.system("cut -d: -f1,5 /etc/passwd")
    
listUser()
