#Application Instructions

Welcome to the suite of user utilities. These were created to function simply with three main goals:
1) Create Users
2) List Users
3) Remove Users

Each application can be run from a Command Line/Terminal. Please open your Command Line/Terminal to begin. If you need
assistance with locating your Command Line/Terminal applciation, please reach out to your supervisor or the application
developer. 

If this is the first time that the applications have been run on this server by you, the permissions will need to be 
modified. In order to modify the permissions please open your Command Line/Terminal. The applications that you will
be modifiying should be in the working directory prior to beginning. To modify the applications please enter the 
following command for each application(without quotation) then press enter:
"sudo chmod u+x AddUser.py"
"sudo chmod u+x RemUser.py"
"sudo chmod u+x ListUser.py"


#AddUser.py
To run the application, type in the command below(without quotation) then press enter:
"sudo ./AddUser.py"
You may be prompted for your password, this is necessary to proceed with a user creation. 
Three steps within the application will allow you to create the user:
  - Follow the onscreen instructions, type the username, the press enter/return.
  - Follow the onscreen instructions, type in the Public SSH key then press enter/return.
  - Follow the onscreen instructions, type in the UID/Comment for the user then press enter.
The user has now been created using the information you had provided. If something was entered incorrectly, please inform
your supervisor or systems administrator.

#RemUser.py
To run the application, type in the command below(without quotation) then press enter:
"sudo ./RemUser.py"
You may be prompted for your password, this is necessary to proceed with a user removal. 
One step within the application will allow you to remove a user:
  - Follow the onscreen instructions, type the username, the press enter/return.
The user has now been removed using the information you had provided. If something was entered incorrectly, please inform
your supervisor or systems administrator.

#ListUser.py
To run the application, type in the command below(without quotation) then press enter:
"sudo ./ListUser.py"
You may be prompted for your password, this is necessary to proceed with a listing the users. 
There are no additional steps requried for listing users, however an example with delimiters is provided below:
Username:UID/Comment
The users have now been listed.
