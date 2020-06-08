from tkinter import *
import tkinter as tk
import playsound
from playsound import playsound
from texttos import texttos
import googletrans
from googletrans import Translator
from translate import *




def func(entry,entry_1,label_5,label_4):
    try:
        m=googletrans.LANGUAGES
        m1=swap(m)
        text=entry
        lng_detect,a=detect(text)
        b=entry_1
        b=b.lower()
        b=m1[b]
        trans_1=translate(text,a,b)
        label_5['text']=lng_detect
        label_8['text']=trans_1
        label_4.insert(tk.END,trans_1)

    except:
        m=googletrans.LANGUAGES
        m1=swap(m)
        text=entry
        lng_detect,a=detect(text)
        b=entry_1
        b=b.lower()
        trans_1=translate(text,a,b)
        label_5['text']=lng_detect
        label_8['text']=trans_1
        label_4.insert(tk.END,trans_1)

#def func_1(label_7):
    #text_1=record()
    #label_7['text']=text_1

def func_2(label_8):
    text=label_8['text']
    m=texttos(text)
    playsound(m)




#---------------------------------------------------------------------------------------------------------------------
HEIGHT=400
WIDTH=900
root=tk.Tk()
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH,bg='black',bd='10')
canvas.pack()
#---------------------------------------------------------------------------------------------------------
frame=tk.Frame(canvas,bg='#80B8AF')
frame.place(x=12,y=12,height=400,width=900)
#----------------------------------------------------------------------------------------------------------------------
label=tk.Label(frame,text="Translate",font=('Helvetica',40),bg='#80B8AF',fg='black')
label.place(x=310,y=30)
#label_1=tk.Label(frame,font=('Helvetica',180),bg='black',fg='black')
#label_1.place(x=400,y=85)
label_2=tk.Label(frame,text='Input:',font=('Helvetica',16),bg='#80B8AF',fg='black')
label_2.place(x=20,y=110)
label_3=tk.Label(frame,text='Translated:',font=('Helvetica',16),bg='#80B8AF',fg='black')
label_3.place(x=400,y=110)
label_4=tk.Text(frame,font=('Helvetica',12),bg='white',fg='black')
label_4.place(x=520,y=110,height=240,width=250)
label_7=tk.Label(frame,text='Input Lang',font=('Helvetica',16),bg='#80B8AF',fg='black')
label_7.place(x=365,y=150)
label_5=tk.Label(frame,font=('Helvetica',14),bg='white',fg='black')
label_5.place(x=375,y=180,width=110)
label_6=tk.Label(frame,text='Output Lang',font=('Helvetica',16),bg='#80B8AF',fg='black')
label_6.place(x=360,y=210)
label_8=tk.Label(frame,font=('Helvetica',12),bg='white',fg='black')

#----------------------------------------------------------------------------------------------------------------------
entry=tk.Entry(frame)
entry.place(x=100,y=110,height=240,width=250)
entry_1=tk.Entry(frame)
entry_1.place(x=375,y=240,height=30,width=110)
#---------------------------------------------------------------------------------------------------------------------
button=Button(frame,text='Translate',bg='black',fg='white',command=lambda:func(entry.get(),entry_1.get(),label_5,label_4))
button.place(x=393,y=320)
button_2=Button(frame,text='Speak',command=lambda:func_2(label_8))
button_2.place(x=785,y=310,height=30,width=60)
#---------------------------------------------------------------------------------------------------------------------------
root.mainloop()
