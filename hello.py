from Tkinter import *
import urllib2
import json
#from PIL import ImageTk, Image
import Pillow

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.xkcdbutton = Button(frame, text="Hello", command=self.xkcd)
        self.xkcdbutton.pack(side=LEFT)

    def xkcd(self):
        #print "hi there, everyone!"
        reqxkcd = urllib2.urlopen('http://xkcd.com/info.0.json')
        json = json.load(reqxkcd)
        image_url = json['img']
        image_object_request = urllib2.Request(image_url)
        image_object_response = urllib2.urlopen(image_object_request)
        panel = Label(root, image = image_object_response)
        panel.pack(side = "bottom", fill = "both", expand = "yes")


root = Tk()

app = App(root)

root.mainloop()
root.destroy()