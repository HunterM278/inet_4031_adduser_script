# inet_4031_adduser_script
Repository for code and files for INET4031 Lab 8 part 2
## Program Description
This program has a python script that automatically adds multiple users, their informations, and sorts them into groups to in the Ubuntu system. The information comes from a input file that holds the users data and is read by the script and automatically filled in, without having to be entered manually by a user.

### Program User Operation
Script contained in this repository automates the creation of new user accounts from a input file that is either provided or created by the user, and runs the commands adduser, passwd, and usermod.

#### Input File Format
There are five fields in the file that are separated by colons ':' that are tied to username, password, lastname, firstname, and groups that they belong to.

Any line in the input file that begins with a '#' symbol is skipped
