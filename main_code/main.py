from functions_for_main.functions import mtn_MOMO_Registered_user
from functions_for_main.functions import mtn_MOMO_Registered_user_pin 

print("\n")
print("A test of MTN GH MOMO Services..... \n")

regUser = input("Enter your name to register: ")
new_applicant = mtn_MOMO_Registered_user(regUser)

regUserPin = input("Enter your preferred 4 - digit pin: ")
new_applicant_pin = mtn_MOMO_Registered_user_pin(regUserPin)

re_regUserPin = input("Enter your pin_number again:  ")

if re_regUserPin == regUserPin:
    print("Y'ello {}!, you have been registered successfully!".format(regUser))
    
else:
    print("Sorry you entered a wrong password for your pin registration, try again")