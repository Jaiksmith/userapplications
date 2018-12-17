The v0.2 applications currently perform the following actions:

AddUser.py: A python application that when provided with username/password will create a user then
generate a private/public ssh keys on a host. Assume that the user running the program has the rights to
manage users on that host.

RemUser.py: A python application that will remove a user, revoke private/public ssh keys and relocate
the user directory to a backup folder when specified with the username.

LisUser.py: A python application that can list users on a host, reporting their username.
