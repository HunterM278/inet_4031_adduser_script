# inet_4031_adduser_script
Repository for code and files for INET4031 Lab 8 part 2
## Program Description
This program has a python script that automatically adds multiple users, their informations, and sorts them into groups to in the Ubuntu system. The information comes from a input file that holds the users data and is read by the script and automatically filled in, without having to be entered manually by a user.

### Program User Operation
Script contained in this repository automates the creation of new user accounts from a input file that is either provided or created by the user, and runs the commands adduser, passwd, and usermod.

#### Input File Format
There are five fields in the file that are separated by colons ':' that are tied to username, password, lastname, firstname, and groups that they belong to.

Any line in the input file that begins with a '#' symbol is skipped

If a user is found with the '-' symbol they will not be assigned to a group

##### Command Execution
Make the file executable with the command:

```
chmod +x create-users.py
```

Run the file with the command:

```
./create-users.py < create-users.input
```
###### Dry Run
Dry run allows the user to test what a script would do without actually executing it. This allows the user to see how it looks and verify that the script is doing what it is supposed to do without the script making any changes.
