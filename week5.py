

 #Create a simple password checker.
#. The password should be at least 8 characters long and if it isn’t
#then tell the user what they must do to create a password

name="patrick"
user="patrick2026"
loginpasswor="Pat123@$"
if len(loginpasswor) >= 8:
    print("2you have access")
else:
    print("password too short")


#. Create an age classifier. Categorize them as child, teenager,

age=int(input("what is your age?"))
if age>=25 and age<=40:
    print("3you are in the prime working years")
if age<10:
    print("you are a child")
if age >70:
    print("you are a senior")


# Create a discount calculator.

total=float(input("Enter your total order"))
if total<50:
    print("discount is 5% ")
elif total<50:
    print("discount is 1.1%")
elif total<50:
    print("discount is 5%")
