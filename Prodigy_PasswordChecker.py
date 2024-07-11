import os

def PasswordChecker(password):

    
    os.system('cls')

    count = 0

    Contains_Upper = False
    Contains_Lower = False
    Contains_Digit = False
    Contains_Special = False

    len_pass = len(password)

    if len_pass == 0:
        while not len_pass > 0:
            password = input("Enter a longer password :\n")
            len_pass = len(password)

    for i in range(len_pass):
        if password[i].isupper():
            Contains_Upper = True
        if password[i].islower():
            Contains_Lower = True
        if password[i].isdigit():
            Contains_Digit = True
        if not password[i].isdigit() and not password[i].isalpha():
            Contains_Special = True

    if Contains_Upper == True:
        count+=1
    else:
        print("Include an Uppercase Letter to make your password stronger.")
    if Contains_Lower == True:
        count+=1
    else:
        print("Include n Lowercase Letter to make your password stronger.")
    if Contains_Digit == True:
        count+=1
    else:
        print("Include a Digit to make your password stronger.")
    if Contains_Special == True:
        count+=1
    else:
        print("Include a Special Character to make your password stronger.")
    if len_pass > 7:
        count+=1
    else:
        print("Lenghten your password to make your password stronger.")

    print()

    if count == 5:
        print("Your Password is Very Strong")
    if count == 4:
        print("Your Password is Strong")
    if count == 3:
        print("Your Password is Moderate")
    if count == 2:
        print("Your Password is Weak")
    if count == 1:
        print("Your Password is Very Weak")

    print()
    retry = input("If You Would Like To Check another Password, Type YES \n")

    retry = retry.upper()

    if retry == "YES":

        os.system('cls')

        password = input("Enter your Password Here :\n")
        PasswordChecker(password)
    
    else:
        print("Thank You For Using This Program")


        


print("Welcome To Password Strenght Checker.\nThis Program will determine the strenght of your password on the follwing conditions :")
print("1. If the password contains an uppercase letter")
print("2. If the password contains a lowercase letter")
print("3. If the password contains a digit")
print("4. If the password contains a special character")
print("5. If the password is longer then 8 characters.")

password = input("Enter your Password Here :\n")

PasswordChecker(password)