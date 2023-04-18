import os

directory = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

blocked_sites=['facebook.com','www.facebook.com']
hosts=open(directory,"r+")
content=hosts.read()



for site in blocked_sites:
    if site not in content:
        hosts.write(redirect +" " + site + '\n')