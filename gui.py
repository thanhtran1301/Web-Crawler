from tkinter import *
from urllib import parse
import crawler

"""Validate the ur given by the user"""
def url_validator(x):
  
    try:
        result = parse.urlparse(x)
        for i in range(2):
        	if result[i] == '':
        		return False;
        return True
    except:
        return False
"""Split the string into a list of words"""
def searchString(string):
  
	return string.split()

"""Validate the number for the max depth of searching"""
def validate_max_depth(num):
	if (num.isdigit() and int(num) > 0):
		return int(num)
	else:
		return False 

"""Collect all user data and begin searching"""
def get_user_data():
   feed_url = e1.get()
   search_string = e2.get()
   max_depth = e3.get()
   if(not url_validator(feed_url) or not validate_max_depth(max_depth)):
   		print("Please validate either feed url or max depth value")
   else:
   		print("Searching begins")
   		crawler.web_crawler(feed_url,searchString(search_string),validate_max_depth(max_depth))

"""Create a GUI with the entry boxes for the url, search string and max depth in searching loop"""

master = Tk()
master.wm_title("Hello, world")
Label(master, text="Feed Url").grid(row=0)
Label(master, text="Search String").grid(row=1)
Label(master, text="Max depth").grid(row=2)

e1 = Entry(master,width = 50)
e2 = Entry(master,width = 50)
e3 = Entry(master,width = 50)

e1.grid(row=0, column=1,pady = 10)
e2.grid(row=1, column=1,pady = 10)
e3.grid(row=2, column=1,pady = 10)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=10)
Button(master, text='Search', command=get_user_data).grid(row=3, column=1, sticky=W, pady=10)

mainloop()