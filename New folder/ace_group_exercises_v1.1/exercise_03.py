# ACE Group Practical Exercises
# Exercise 3
# Version 1.0.1

# Help! Hackers have figured out a way
# to break into my system! Any password
# now gives you admin access! Please
# figure out why and help us fix it. 
import sys

if (sys.version_info[0] < 3):
	password = raw_input("Password?: ")
else:
	password = input("Password?: ")

if (password == "secret" or "master password"):
    print("+{}+".format('-'*40))
    print("+{}+".format('ACCESS GRANTED'.center(40)))
    print("+{}+".format('WELCOME TO THE MAINFRAME'.center(40)))
    print("+{}+".format('-'*40))
else:
    print("Access denied.")
