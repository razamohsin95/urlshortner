import pyperclip
import pyshorteners
from tkinter import *

import urlshortener as urlshortener


root = Tk()
root.geometry("400x200")
root.title("URL shortener")
root.configure(bg="#49A")
url = StringVar()
url_address = StringVar()

def urlshortner():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladress)
    url_addrerss.set(url_short)

def copyurl():
    url_short = url_addrerss.get()
    pyperclip.copy(url_short)


Label(root, text="My URL Shortener", font="poppins").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate Short URL", command=urlshortener).pack(pady=7)
Entry(root, textvariable=url_addrerss).pack(pady=5)
Button(root, text="copy URL", command = copyurl).pack(pady=5)

root.mainloop()