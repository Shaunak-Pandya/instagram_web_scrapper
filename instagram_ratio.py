#Authored by Shaunak N. Pandya

from tkinter import *
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageTk
def toScrape(event):
    r = Tk()   
    r.configure(background='white')
    string = e1.get()
    r.title("Instagram User - "+string)
    url = "https://www.instagram.com/{}/".format(string)
    x = requests.get(url)
    soup = BeautifulSoup(x.content, "html.parser")  
    Label(r,text="INSTAGRAM TOOL BY WEBSYCODE",height=1,width=40,bg="white").grid(row=0,padx=10,pady=10)
    Label(r,text="Username:",height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=1,padx=10,pady=10)
    Label(r,text=e1.get(),height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=1,column=1,padx=20,pady=10)
    lis=''.join(map(str,soup)) #Converted to String
    followc = lis[lis.find('edge_follow')-1:lis.find('edge_follow')+100]  #To find a particular substring from string
    postc=lis[lis.find('edge_owner_to_timeline_media')+39:lis.find('edge_owner_to_timeline_media')+47]
    
    ### Followers 
    Label(r,text="Followers:  (n)",height=1,width=40,bg="white",borderwidth=2,relief="solid").grid(row=2,padx=10,pady=10)
    Label(r,text=followc[followc.find("{")+9:followc.find("}")],height=1,width=40,bg="white",borderwidth=2,relief="solid").grid(row=2,column=1,padx=20,pady=10)
    
    ### Following 
    follows = followc[followc.find("}")+52:followc.find(",\"follows")]
    Label(r,text="Following:  (m)",height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=3,padx=10,pady=10)
    if (follows.find("}")>1):
        
        Label(r,text=follows[:follows.find("}")],height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=3,column=1,padx=20,pady=10)
    
    else:
        Label(r,text=follows,height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=3,column=1,padx=20,pady=10)
        
    #Total Posts
    Label(r,text="Total Posts:",height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=4,padx=10,pady=10)
    Label(r,text=postc[:postc.find(",")],height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=4,column=1,padx=20,pady=10)
    n=int(followc[followc.find("{")+9:followc.find("}")]) #conversion to int
    m=int(follows[:follows.find("}")]) #conversion to int
    ratio=n/m
    #TODO - To add clauses of ratios

    Label(r,text="Ratio (n/m):",height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=5,padx=10,pady=10)
    Label(r,text=ratio,height=1,width=40,bg="white",borderwidth=2, relief="solid").grid(row=5,column=1,padx=20,pady=10)
        
    Button(r, text='Exit', width=20, command=r.destroy,bg="red",borderwidth=2,relief="solid").grid(row=6, column=1,pady=5)
    mainloop()
##########################################    

master = Tk()
master.title("Instagram Scrapping Tool")
master.configure(background='white')
Label(master, text='Enter Username ->',height=1,width=30,bg="white",borderwidth=2, relief="solid").grid(row=0) 
e1 = Entry(master) #Input Widget
e1.configure(background='white',width=30,borderwidth=2, relief="solid")
e1.grid(row=0, column=2,padx=30,pady=20)
e1.bind('<Return>',toScrape) #Binding Function to key press
Label(master, text='</> by Shaunak Pandya',height=1,width=30,bg="white").grid(row=4,padx=10,pady=10)
Label(master, text='www.websycode.in',height=1,width=30,bg="white").grid(row=4,column=2)
button = Button(master, text='Exit', width=20, command=master.destroy,bg="red",borderwidth=2,relief="solid").grid(row=2,pady=20,padx=50) #to destroy screen
mainloop()
