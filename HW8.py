pincode=(input("please enter valid pin"))
n=1
len=len(pincode)
print(len)
if len==4:
   print("pin validated")
else:
    while n<3:
       print("pin incorrect")
       pincode1 = input("please enter valid pin")
       len = len(pincode1)
       print(len)
       if len == 4:
           print("pin validated")

       n=n+1
       exit()
bal=100
wa=int(input("please enter withdrawl amount"))
try:
    if bal>wa:
       new_bal=bal-wa
       print("new balance="+str(new_bal))
except:
    print("check balance amount")
    exit()
finally:
    print("ATM code was done")






