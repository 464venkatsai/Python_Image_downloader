# Importing the modules
import requests
import multiprocessing
from tkinter import *

# Declaring Global Variables
global e1
global e2

# Size of GUI 
top = Tk()
top.geometry('510x350')
top.maxsize(510,350)

# Making a function to download
def Download_Image(url,name='image'):
    response  = requests.get(url)
    # Creating the file with the user defined name
    open(f'{name}.jpg','wb').write(response.content)
    
# Clearing all widgets
def clear_window():
    for widget in top.winfo_children():
        widget.destroy()
    
# Creating a interface to User
def Image_downloader():
    # Getting Entered values from user
    def get_values():
        url = e1.get()
        name = e2.get()
        Download_Image(url,name)
        clear_window()
        Image_downloader()
    # Widgets in GUI
    heading = Label(text=' ',font='bold 15')
    l1 = Label(text='URL of image : ',font='bold 13')
    e1 = Entry(font='bold 13')
    l2 = Label(text='Name of image : ',font='bold 13')
    e2 = Entry(font='bold 13')
    b1 = Button(text='Download Image',width=18,height=2,font='bold 10',command=get_values)
    heading1 = Label(text=' IMAGE DOWNLOADER ',font='bold 15')

    # Arranging the widgets in GUI
    heading1.grid(row=0,column=0,padx=30,pady=20,sticky='w')
    heading.grid(row=0,column=1,padx=(0,50),pady=20)
    l1.grid(row=1,column=0,padx=30,pady=20)
    e1.grid(row=1,column=1,padx=0,pady=0,sticky='w')
    l2.grid(row=3,column=0,padx=30,pady=50)
    e2.grid(row=3,column=1,padx=0,pady=20,sticky='w')
    b1.grid(row = 4,column=0)
    

# Initializing Image Downloader
Image_downloader()
 
# Closing GUI 
top.mainloop()



