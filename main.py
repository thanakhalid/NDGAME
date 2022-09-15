from tkinter import *
from tkinter.ttk import *
import random
import time


# define the countdown func.
year = random.randint(1932, 2022)
scores = 0
def stopgame():
    my_canvas.itemconfig(image_container, image=bg2)
    my_canvas.itemconfig(timeuplabel,state = 'normal')
    my_canvas.itemconfig(yearlabel, state='hidden')
    my_canvas.itemconfig(qlabel, state='hidden')
    my_canvas.itemconfig(fscorelabel, text=(" نقاطك\n" + str(scores)))
    my_canvas.itemconfig(fscorelabel, state='normal')
    my_canvas.itemconfig(startbtn_window, state='hidden')
    my_canvas.itemconfig(scoreslabel, state='hidden')
    my_canvas.itemconfig(timelabel, state='hidden')
    my_canvas.itemconfig(AbdulAziz_window, state='hidden')
    my_canvas.itemconfig(Saud_window, state='hidden')
    my_canvas.itemconfig(Faisal_window, state='hidden')
    my_canvas.itemconfig(Khalid_window, state='hidden')
    my_canvas.itemconfig(Fahad_window, state='hidden')
    my_canvas.itemconfig(Abdullah_window, state='hidden')
    my_canvas.itemconfig(Salman_window, state='hidden')

def countdowntimer():
    t = 60
    while t > 0:
        my_canvas.itemconfig(timelabel, text=("الوقت المتبقي\n" + str(t)))
        t -= 1
        window.update()
        time.sleep(1)
    stopgame()
def checkanswer1():
    global scores
    if year >= 1932 and year <= 1953:
        scores +=1
    my_canvas.itemconfig(scoreslabel, text=("نقاطك\n"+str(scores)))
    change_year()

def checkanswer2():
    global scores
    if year >= 1953 and year <= 1964:
        scores +=1
    my_canvas.itemconfig(scoreslabel, text=(" نقاطك\n"+str(scores)))
    change_year()

def checkanswer3():
    global scores
    if year >= 1964 and year <= 1975:
        scores +=1
    my_canvas.itemconfig(scoreslabel, text=("نقاطك\n"+str(scores)))
    change_year()
def checkanswer4():
    global scores
    if year >= 1975 and year <= 1982:
        scores +=1
    my_canvas.itemconfig(scoreslabel, text=("نقاطك\n"+str(scores)))
    change_year()

def checkanswer5 ():
    global scores
    if year >= 1982 and year <= 2008:
        scores +=1
    my_canvas.itemconfig(scoreslabel, text=(" نقاطك\n"+str(scores)))
    change_year()

def checkanswer6():
    global scores
    if year >= 2008 and year <= 2015:
        scores +=1
    my_canvas.itemconfig(scoreslabel, text=(" نقاطك\n"+str(scores)))
    change_year()

def checkanswer7():
    global scores
    if year >= 2015 and year <= 2022:
        scores +=1
    my_canvas.itemconfig(scoreslabel, text=("نقاطك\n"+str(scores)))
    change_year()
def change_year():
    global year
    year = random.randint(1932, 2022)
    my_canvas.itemconfig(yearlabel, text = year)






def update_image():
   my_canvas.itemconfig(image_container,image=bg2)
   my_canvas.itemconfig(qlabel,state = 'normal')
   my_canvas.itemconfig(yearlabel,state = 'normal')
   my_canvas.itemconfig(startbtn_window,state='hidden')
   my_canvas.itemconfig(scoreslabel, state='normal')
   my_canvas.itemconfig(timelabel, state='normal')
   my_canvas.itemconfig(AbdulAziz_window, state='normal')
   my_canvas.itemconfig(Saud_window, state='normal')
   my_canvas.itemconfig(Faisal_window, state='normal')
   my_canvas.itemconfig(Khalid_window, state='normal')
   my_canvas.itemconfig(Fahad_window, state='normal')
   my_canvas.itemconfig(Abdullah_window, state='normal')
   my_canvas.itemconfig(Salman_window, state='normal')
   countdowntimer()

#code start here -------------------------------------------
window = Tk()
# set window title
window.title("national day game")
# set window width and height
#window.configure(width=1000, height=750)
window.geometry("1000x750")
#photo------------------------------------------------------
bg = PhotoImage(file = "images/bg.png")
bg2 = PhotoImage(file = "images/bg2.png")
#canvas-----------------------------------------------------
my_canvas = Canvas(window,width=1000,height=750)
my_canvas.pack(fill="both",expand=True)
#set image in canvas-------------------------------------------------------------
image_container = my_canvas.create_image(0,0,image=bg,anchor="nw")
#add label---------------------------------------------------
qlabel = my_canvas.create_text(499,50,text="\n من كان الملك في عام ",font = ("GE Dinar Two Medium",25),fill="white",justify=CENTER)
my_canvas.itemconfig(qlabel,state = 'hidden')
yearlabel = my_canvas.create_text(499,115,text=year,font = ("GE Dinar Two Medium",25),fill="white",justify=CENTER)
my_canvas.itemconfig(yearlabel,state = 'hidden')
scoreslabel = my_canvas.create_text(100,100,text=("نقاطك\n"+str(scores)),font = ("GE Dinar Two Medium",18),fill="white",justify=CENTER)
my_canvas.itemconfig(scoreslabel,state = 'hidden')
timelabel = my_canvas.create_text(865,100,text=("الوقت المتبقي\n"+str(scores)),font = ("GE Dinar Two Medium",18),fill="white",justify=CENTER)
my_canvas.itemconfig(timelabel,state = 'hidden')
fscorelabel = my_canvas.create_text(495,600,text=("نقاطك\n"+str(scores)),font = ("GE Dinar Two Medium",45),fill="white",justify=CENTER)
my_canvas.itemconfig(fscorelabel,state = 'hidden')
timeuplabel = my_canvas.create_text(499,100,text="\n !انتهى الوقت ",font = ("GE Dinar Two Medium",45),fill="white",justify=CENTER)
my_canvas.itemconfig(timeuplabel,state = 'hidden')
#buttons style -----------------------------------------------
style1 = Style()
style1.configure('W.TButton', font =
               ('GE Dinar Two Medium', 28),
                foreground = 'black',
                  height = 70, width = 20
                 )
style2 = Style()
style2.configure('W2.TButton', font =
               ('GE Dinar Two Medium', 18, 'bold'),
                foreground = 'black',height = 500, width = 20)
#start button ------------------------------------------------
startbtn = Button(window,text="ابدأ",style = 'W.TButton')
startbtn.configure(command=lambda:update_image())
startbtn_window = my_canvas.create_window(395,645,anchor = "nw",window = startbtn)
#kings buttons------------------------------------------------
AbdulAziz = Button(window,text="عبدالعزيز" ,style = 'W2.TButton')
AbdulAziz.configure(command=lambda:checkanswer1())
AbdulAziz_window = my_canvas.create_window(428,435,anchor = "nw",window = AbdulAziz)
my_canvas.itemconfig(AbdulAziz_window, state='hidden')
Saud = Button(window,text="سعود",style = 'W2.TButton')
Saud.configure(command=lambda:checkanswer2())
Saud_window = my_canvas.create_window(250,550,anchor = "nw",window = Saud)
my_canvas.itemconfig(Saud_window, state='hidden')
Faisal = Button(window,text="فيصل",style = 'W2.TButton')
Faisal.configure(command=lambda:checkanswer3())
Faisal_window = my_canvas.create_window(428,550,anchor = "nw",window = Faisal)
my_canvas.itemconfig(Faisal_window, state='hidden')
Khalid = Button(window,text="خالد",style = 'W2.TButton')
Khalid.configure(command=lambda:checkanswer4())
Khalid_window = my_canvas.create_window(608,550,anchor = "nw",window = Khalid)
my_canvas.itemconfig(Khalid_window, state='hidden')
Fahad = Button(window,text="فهد",style = 'W2.TButton')
Fahad.configure(command=lambda:checkanswer5())
Fahad_window = my_canvas.create_window(250,660,anchor = "nw",window = Fahad)
my_canvas.itemconfig(Fahad_window, state='hidden')
Abdullah = Button(window,text="عبدالله",style = 'W2.TButton')
Abdullah.configure(command=lambda:checkanswer6())
Abdullah_window = my_canvas.create_window(428,660,anchor = "nw",window = Abdullah)
my_canvas.itemconfig(Abdullah_window, state='hidden')
Salman = Button(window,text="سلمان",style = 'W2.TButton')
Salman.configure(command=lambda:checkanswer7())
Salman_window = my_canvas.create_window(608,660,anchor = "nw",window = Salman)
my_canvas.itemconfig(Salman_window, state='hidden')


window.mainloop()
