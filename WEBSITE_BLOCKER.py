import time
from datetime import datetime as dt

# for WINDOWS users only
# How to run : written below but read the other comments in the script first

hosts_path=r"C:\Windows\System32\drivers\etc\hosts" # Before running the code, WARNING: Please make a copy of this hosts file and save it in other location

redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com","github.com"] # list of websites you want to block

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16): # setting time limit of blocker 0800 to 1600 hours
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n") # editing the hosts file
    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)  # deleting the websites from hosts file so that you can run blocked websites
            file.truncate()
        print("Fun hours...")
    time.sleep(5) # setting the refresh time

# how to run:

#1. copy this file where all python files (normal .py files which on which you practice) are located.
#2. open command prompt and run it as administrator.
#3. cd directory to the pasted location
#4. write "python WEBSITE_BLOCKER.py" and press enter
#5. and you will  notice facebook stops opening in web browser.