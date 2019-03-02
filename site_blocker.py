import time
from datetime import datetime as dt

#This program will run in the background and during a certain time frame block certain, specified sites.

hosts_temp='hosts'
#Using the r allows us to escape escape characters
hosts_path=r'C:\Windows\System32\drivers\etc\hosts'
redirect = '127.0.0.1'
sites_that_kill_my_time = ['www.facebook.com', 'facebook.com', 'www.gmail.com', 'gmail.com']
#These 4 elements need their own respective lines on the host file and redirect IP
print(dt.now())

while True:
    #We are stating that if the time is between 9am and 5 pm on today
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("These are my Working Hours: ")
# now we can load, read and write to the hosts file, using the r+ allows reading and writing to the file
        with open(hosts_path, 'r+') as file:
            content = file.read() # This will load the entire file
            for site in sites_that_kill_my_time:
                if site in content:
                    pass
                else:
                    file.write(redirect + ' ' + site + '\n')
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
#The readlines() method will place the cursor at the end of the file.
# To bring the cursor back to the begining we use the seek() function and specify its placement.
            file.seek(0)
            for line in content:
# If item not there, append a new file host via writing a new file
                if not any(site in line for site in sites_that_kill_my_time):
                    file.write(line)
# truncate method will delete all things under the specified section
            file.truncate()
        print("Time to play!!!")
    time.sleep(600)
