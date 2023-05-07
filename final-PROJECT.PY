#GUI
from tkinter import *
from email.message import EmailMessage
import ssl
import smtplib
import random
import math
from PIL import Image,ImageTk 
import tkinter as tk

ea=''
root=Tk()
root.minsize(358,353)
root.maxsize(358,353)

root.config(bg="green")

#image 
image=Image.open('logo.png')
photo = ImageTk.PhotoImage(image)
image_label=Label(image=photo)
image_label.grid(row=0,column=0,sticky=NW)





l1=Label(text="AUTHORISE USER",bg='black',fg='red',relief=SUNKEN,font="Arial 12 bold")
l1.grid(row=0,column=5,sticky=N)

l2=Label(text="SUZUKI",bg='blue',fg='red',borderwidth=3,relief=SUNKEN,font="Arial 9 bold").grid(row=1,column=0,sticky=W,)
         

digits='0123456789'
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP"
print(OTP)

    

#functoion of sending email when button is clicked
def login():
    ea =emailid.get()
        
    


    email_sender='minorproject004@gmail.com'
    email_password='acfvxsqrlxlcyyui'
    email_receiver=ea
    subject="otp"
    body=otp


    em= EmailMessage()
    em['From']= email_sender
    em['To']=email_receiver
    em['Subject']=subject
    em.set_content(body)

    context=ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context)as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_receiver,em.as_string())

    result=Label(text="otp send successfully",fg='black',borderwidth=3,relief=SUNKEN)
    result.grid(row=7,column=5)

    #otp receving

    otp_label=Label(root,text="otp")
    otp_label.grid(row=8,column=4)
    otp_entery=Entry(root,show="*")
    otp_entery.grid(row=8,column=5)
    
    #fucnction for ootp checking
    def checkotp():
        otps=otp_entery.get()
        print(otps)
        if(otps==OTP):
            return_label=Label(root,text="access granted",bg="black",fg="red",borderwidth=5,relief=SUNKEN)
            return_label.grid(row=10,column=5)
        else:
            return_label=Label(root,text="access denied",bg="black",fg="red",borderwidth=5,relief=SUNKEN)
            return_label.grid(row=10,column=5)

            

#otp button
    b2=Button(fg='red',text="verfiy otp", command=checkotp)
    b2.grid(row=9,column=5)



## credentials entery from the user
emailid_label=Label(root,text="email id")
emailid_label.grid(row=2,column=4,)
emailid=Entry(root)
emailid.grid(row=2,column=5)
b1=Button(fg='red',text="sent OTP", command=login)
b1.grid(row=6,column=5)







root.mainloop()









