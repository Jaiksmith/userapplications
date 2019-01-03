Ansible Application Instructions

Welcome to the Ansible suite of user utilities. These were created to function simply with three main goals:

    Create Users
    Remove Users

Each application can be run from a Command Line/Terminal. Please open your Command Line/Terminal to begin. If you need assistance with locating your Command Line/Terminal applciation, please reach out to your supervisor or the application developer.

AddUser.yml: Prior to running you will need to complete three tasks.
 1. Specify a user to create: 
    Open AddUser.yml in nano or an alternative text editor.
    In the seventh line, change the user to the username you would like(i.e. "Grace")
    Save and exit the file.
 2. Specify a user comment:
    Open AddUser.yml in nano or an alternative text editor.
    In the 13th line, change the comment to a user specific comment(i.e. "Grace Dunn")
    Save and exit the file.
 2. Save your SSH Public key:
    Create a folder in your working directory named "keys".
    Add in your SSH public key file with the correct username(i.e. Grace.key.pub)
    The contents should be one line similar to the line below, but edited to match your user information:
      ssh-rsa 123456 Grace@localhost
    "123456" is your SSH Public key and should be changed to the key that was generated. Grace@localhost is the user.
To run the application, type in the command below(without quotation) then press enter: 
    "sudo ansible-playbook AddUser.yml"
    You may be prompted for your password, this is necessary to proceed with a user creation. 
    
RemUser.yml: Prior to running you will need to complete one tasks.
  1. Specify a user to remove:
     Open AddUser.yml in nano or an alternative text editor.
     In the sixth line, change the user to the username you would like(i.e. "Grace")
     Save the file and exit.
To run the application, type in the command below(without quotation) then press enter: 
     "sudo ansible-playbook RemUser.yml"
     You may be prompted for your password, this is necessary to proceed with a user removal.
