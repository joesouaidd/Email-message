"""
Created on Sun Sep 25 17:02:51 2022

@author: souaid
"""


def in_between(now, start, end):
    if start <= end:
        return start <= now < end
    else: # over midnight e.g., 23:30-04:15
        return start <= now or now < end


from datetime import datetime, time


status = ("night" if in_between(datetime.now().time(), time(23), time(5)) else "day")
print(status)


if status == "night":
    


    import smtplib
     
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
     
    # start TLS for security
    s.starttls()
     
    # Authentication
    s.login("email@gmail.com", "pass")
     
    # message to be sent
    message = "hello night"
     
    # sending the mail
    s.sendmail("sender@gmail.com", "recp@gmail.com", message)
     
    # terminating the session
    s.quit()