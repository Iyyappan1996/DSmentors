import re
def email(email_flag):
 email=input("Enter your email : ")
 if re.match("[a-zA-Z][a-zA-Z 0-9]*@gmail.com",email):
     email_flag=1
 else:
    print("Not a valid")
 return email_flag,email
def password(password_flag):
    password=input("Enter the password: ")
    if not re.search("[a-z]",password):
        password_flag=0
    elif not re.search("[A-Z]",password):
        password_flag=0
    elif not re.search("[0-9]",password):
        password_flag=0
    elif not re.search("[@#$%&]",password):
        password_flag=0
    elif len(password)<=5 or len(password)>=15:
        password_flag=0
    if password_flag==1:
          pass
    elif password_flag==0:
          print("Password should contains below things \n1. One alphabet\n2. One small letter\n3. one numeric character\n4. One special character\n5. It should be greater than the 5 and less than 15 character") 
    return (password_flag,password)
inp=int(input("Enter your option: \n 1. To login \n 2. Forgot Password\n "))
if inp==1:
    email_flag,email=email(0)
    if email_flag==1:
      password_flag,password=password(1)
if email_flag==1 and password_flag==1:
    print("matched")
    file=open("Database","a")
    file.write(email)
    file.write(password)
    file.close()
    
    
    
       
    
    