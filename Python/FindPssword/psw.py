
import random
from time import sleep
import time

chars = "abcdefghijklmnopqrstuvwxyz"
numb = "0123456789"

while 1:  
  email = input("Enter Email Enemy : ")
  wordlist = int(input("Input Code : "))
  print("Email == ",email)
      
  for x in range(wordlist): 
    password = ""
    for x in range(8):
      password_char = random.choice(chars)
      numb_char = random.choice(numb)
      
      password = password + password_char
      numbs =numb_char
      
    time.sleep(1)
    print("Email == ",email)    
    print("Password :: ",password+numbs+numbs)