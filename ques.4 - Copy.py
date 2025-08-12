correct_password ="python123"
password =""
while password != correct_password:
    password = input("enter the password: ")
    if password !=correct_password:
        print ("incorrect password. try again!")
print("password correct . access granted!")
