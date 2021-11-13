#Write a program that prompts the user to input a password and checks if the password
# is valid. If the password is valid, print a confirmation statement. If it is not, print a
# statement that the password is not valid.


from re import*

print("your welocme to code password ")

Password= input("Input your password :  ")
x = True
while x:  
    
    if (len(Password)<6 or len(Password)>20):   #للتاكد من العدد
        break
    elif not search("[a-z]",Password):# للتاكد انه يوجد حرف صغير
        break
    elif not search("[0-9]",Password): # للتاكد انه يوجد رقم
        break
    elif not search("[A-Z]",Password): #للتاكد انه يوجد حرف كبير
        break
    elif search("\s",Password):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")