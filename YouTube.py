from Tkinter import *
import main
url="A"
d=main.download()
gui=Tk()
gui.title("YouTube Download")
frame1= Frame(gui)
frame1.pack()
frame2=Frame(gui)
frame2.pack(side=BOTTOM)
text1= Text(frame1,height=2,width=50)
text1.pack(side=LEFT)
text1.insert(END,"Enter URL..!")
variable = StringVar(frame1)
variable.set("Select Format")
dropdown1=OptionMenu(frame1,variable,"Audio","Video")
dropdown1.pack(side=LEFT)
def start():
	url=text1.get("1.0","end-1c")
	videotype = variable.get()
	vtype=str(videotype)
	d.start_download(url,vtype)
	
button1= Button(frame2,text="DOWNLOAD!",command=start)
button1.pack()
gui.mainloop()