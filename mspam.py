#!/usr/bin/python/
import smtplib, os, sys

def spam():
        msg = input("[+] enter the attack msg ==> ")
        target = input("[+] enter yout target email (gmail) ==> ")
        atack_number = input("[+] enter your attack number ==> ")
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.ehlo()
        s.starttls()
        try:
            s.login("your_gmail@gmail.com","your_password")
            while True:
                x = 1
                s.sendmail(target,target,msg)
                print("[+] send to number => "+x)
                x=x+1
                if x == atack_number:
                    sys.exit("[+] atack complated !")
        except:
            pass

def main():
    os.system("clear")
    print("-"*60)
    print("# devloped by A1peren")
    print("# basic gmail spam bot v0.1")
    print("# welcome to "+sys.argv[0])
    print("-"*60)
    spam()

main()