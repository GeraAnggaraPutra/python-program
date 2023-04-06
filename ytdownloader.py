from pytube import YouTube
from tkinter import *

root = Tk()
root.geometry('400x200')
root.title("Python pytube")

text = StringVar()
text.set("paste link here...")

def download(link):
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').desc().first().download()
    e.delete(0, END)
    e.insert(0, "Successfully Download Video!")

label1 = Label(root, text="Python YouTube Video Downloader").pack()

e = Entry(root, width=50,bd=4,textvariable=text)
e.pack(side=TOP,pady=40)

btn1 = Button(root, text="Download Video", command=lambda: download(e.get()), bd=5, bg='red', fg='white',activeforeground='white',activebackground='black').pack()

root.mainloop()


