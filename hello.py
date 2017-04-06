from Tkinter import *
import urllib2
import json
from PIL import ImageTk, Image
import tempfile
import wget

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.xkcdbutton = Button(frame, text="XKCD", command=self.xkcd)
        self.xkcdbutton.pack(side=LEFT)

    def xkcd(self):
        reqxkcd = urllib2.urlopen('http://xkcd.com/info.0.json')
        content = json.load(reqxkcd)
        image_url = content['img']
        tempfilename = tempfile.gettempdir() + "\comic.png"
        imagefile = wget.download(image_url, out = tempfilename)        
        appimage = ImageTk.PhotoImage(Image.open(tempfilename))
        panel = Label(root, image = appimage)
        panel.image = appimage
        panel.pack(side = "bottom", fill = "both", expand = "yes")

root = Tk()

app = App(root)

root.mainloop()
root.destroy()
