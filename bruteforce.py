import random
password=str(input("enter password of in numeric "))
guess=""
while guess!=password:
    guess=str(random.randint(0,9999))
    print(">>"+guess)
    if(guess==password):
        print("the password is :"+password)
        break
    
