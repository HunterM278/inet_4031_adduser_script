#!/usr/bin/python3

# INET4031
# Hunter Mocling
# Data Created: October 27, 2025
# Date Last Modified: October 28,2025

# The import os gives the program access to commands for os, regular expressions matching for import re, and import sys allows for the program to access system functions
import os
import re
import sys


def main():
    for line in sys.stdin:

        #Checks for any lines that begin with the # symbol, noting that it should be skipped
        match = re.match("^#",line)

        #Splits line with ':' after removing any whitespaces
        fields = line.strip().split(':')

        #Skips comment lines or if it does not have 5 fields
        if match or len(fields) != 5:
            continue

        #Gives variables for user info from the inpuit file, gecos field is being created with combination of other data fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #Splitting the last field with commas for user groups
        groups = fields[4].split(',')

        #Shows that a new user is being made
        print("==> Creating account for %s..." % (username))
        #Creates user without password, and cmd is being stored executes the creation of user
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #print cmdd helps with coding and fixing bugs like (dry runs), os.system(cmd) executes the creation of user stored in the cmd as shown above
        #print cmd
        os.system(cmd)

        #Shows password being made for the created user
        print("==> Setting the password for %s..." % (username))
        #cmd in this case is being store with the action of getting password from input file
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #Executes cmd to set password to user
        #print cmd
        os.system(cmd)

        for group in groups:
            #Checks for '-' if tied to user and does not assign them a group, and if it is not found on a user they are placed into their specified groups
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()

