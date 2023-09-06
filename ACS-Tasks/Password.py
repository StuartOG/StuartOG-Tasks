#program to ask for a password
password = input("What is your password?: ")
if len(password) >= 6:
    print("Valid password")
else:
    print("Invalid password")
#end if