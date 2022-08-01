from functions_for_main.functions import mtn_MOMO_Registered_user

print("\n")
print("A test of MTN GH MOMO Services..... \n")

reg = input("Enter your name to register: ")
new_applicant = mtn_MOMO_Registered_user(reg)
print(new_applicant)