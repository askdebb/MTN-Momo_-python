from functions_for_main.functions import mtn_MOMO_Registered_user
from functions_for_main.functions import mtn_MOMO_Registered_user_pin
from functions_for_main.functions import no_int_begins 

print("\n")
print("A test of MTN GH MOMO Services..... \n")

regUser = input("Enter your name to register: ")
reguser = no_int_begins(regUser)

if regUser == '':
    print("Did you entered spacebar or didnt, Man you are sick, start the process again")
    exit()
else:
    new_applicant = mtn_MOMO_Registered_user(reguser)

regUserPin = input("Enter your preferred 4 - digit pin: ")
if regUserPin == ' ':
    print("The field is empty, retart the process again")
else:    
    new_applicant_pin = mtn_MOMO_Registered_user_pin(regUserPin)

re_regUserPin = input("Enter your pin_number again:  ")

if re_regUserPin == regUserPin:
    print("Y'ello {}!, you have been registered successfully!".format(regUser))
    
    
else:
    print("Sorry you entered a wrong password for your pin registration, try again")