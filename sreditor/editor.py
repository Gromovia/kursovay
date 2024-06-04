from tkinter import *
from PIL import Image, ImageDraw
from random import randint
from tkinter import colorchooser, messagebox

dsdf
def Black():

        canvas['bg'] = 'black'
        draw_img.rectangle((0, 0, 1920, 1080), width=0, fill='black')
        i=2

def White():
        canvas['bg'] = 'white'
        draw_img.rectangle((0, 0, 1920, 1080), width=0, fill='White')
        i=1




def draw(event):

    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill=color, width=0)
    draw_img.ellipse((x1, y1, x2, y2), fill=color, width=0)


def drawc(event):

    x1, y1 = (event.x - brush_size), (event.y - brush_size)
    x2, y2 = (event.x + brush_size), (event.y + brush_size)
    canvas.create_oval(x1, y1, x2, y2, fill='white', width=0)
    draw_img.ellipse((x1, y1, x2, y2), fill='white', width=0)


def chooseColor():
    global  color
    (rgb,hx)=colorchooser.askcolor()
    color=hx
    color_lab['bg']=hx

def select(value):
    global brush_size
    brush_size = int(value)


def pour():
    canvas.delete('all')
    canvas['bg'] = color
    draw_img.rectangle((0, 0, 1280, 720), width=0, fill=color)
    draw_img.rectangle((0, 0, 1280, 720), width=0, fill=color)

def clear_canvas():
    canvas.delete('all')
    canvas['bg'] = 'white'
    draw_img.rectangle((0,0,1920,1080),width=0,fill='white')

def save_img():
    filename=f'imege_{randint(0,10000)}.png'
    image1.save(filename)
    messagebox.showinfo('Saving','Saved under the name %s'%filename)



def popup(event):
    global x,y
    x=event.x
    y=event.y
    menu.post(event.x_root,event.y_root)

def square():
    canvas.create_rectangle(x,y,x+brush_size,y+brush_size,fill=color,width=0)
    draw_img.polygon((x,y,x+brush_size,y,x+brush_size,y+brush_size,x,y+brush_size),fill=color)

def circle():
    canvas.create_oval(x,y,x+brush_size,y+brush_size,fill=color,width=0)
    draw_img.ellipse((x,y,x+brush_size,y+brush_size),fill=color)

x=0
y=0

root = Tk()
root.title('SR editor')
root.geometry('1920x1080')
root.resizable(None,None)



brush_size = 10
color = 'black'

root.columnconfigure(6,weight = 1)
root.rowconfigure(2,weight = 1)

canvas = Canvas(root,bg='white')
canvas.grid(row=2, column = 0, columnspan = 7, padx=5, pady = 5, sticky = E+W+S+N)


canvas.bind('<B1-Motion>', draw)
canvas.bind("<Button-2>", popup)
canvas.bind('<B3-Motion>', drawc)


menu = Menu(tearoff=0)
menu.add_command(label = 'Square', command=square)
menu.add_command(label = 'Circle', command=circle)
image1 = Image.new('RGB',(1920,1080),'white')
draw_img = ImageDraw.Draw(image1)

Label(root,text='Parameters').grid(row=0, column = 0, padx=6)

Button(root, text='Choose color', width=11,command=chooseColor).grid(row=0, column = 1, padx=6)

color_lab = Label(root, bg=color, width=10)
color_lab.grid(row=0, column=2,padx=6)

v=IntVar(value=10)
Scale(root, variable=v,from_=1, to=100,orient=HORIZONTAL, command=select).grid(row=0, column = 3, padx=6)

Label(root,text='Actions').grid(row=1, column = 0, padx=6)

Button(root,text='Filling',width=10,command=pour).grid(row=1,column=1)

Button(root,text='Black theme',width=10,command=Black).grid(row=1,column=3)
Button(root,text='White theme',width=10,command=White).grid(row=1,column=4)



Button(root,text='Clear', width=10, command=clear_canvas).grid(row=1,column=2)

Button(root, text='Save', width=10, command=save_img).grid(row=1,column=6)

root.mainloop()
