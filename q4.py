Password = "python123"
User_input= input("Enter passowrd: ")
while Password != User_input:
    print("Wrong password, please try again!")
    User_input= input("Enter passowrd: ")
print("Password accepted!")