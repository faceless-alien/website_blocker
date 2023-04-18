from tkinter import *

site_entry=Entry()

directory = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

blocked_sites=['facebook.com','www.facebook.com']
hosts=open(directory,"r+") 

def block():
    global blocked_sites
    blocked_sites.append(site_entry.get())
    site_entry.delete(0,END)
    content=hosts.read()
    for site in blocked_sites:
        if site not in content:
            hosts.write(redirect +" " + site + '\n')
            
def unblock():
    global blocked_sites
    blocked_sites.remove(site_entry.get())
    site_entry.delete(0,END)
    content=hosts.read()
    hosts.seek(0)
    for line in content:
        if not any(site in line for site in blocked_sites):
            hosts.write(line)
    hosts.truncate() 


root=Tk()
root.geometry("400x600")

block_button=Button(text="Add site to the blacklist",command=block)
unblock_button=Button(text="Remove site from the blacklist",command=unblock)

list_of_blocked_sites=Text()


