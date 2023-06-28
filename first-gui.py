# first-gui.py

from tkinter import *

GUI = Tk() # โปรแกรมหลัก
GUI.title('โปรแกรมแรกของฉัน') # ชื่อโปรแกรม
GUI.geometry('2000x300')

L = Label(GUI,text='สวัสดีจ้า',font=('Angsana New',100,'bold'))
# L.pack()
L.place(x=150,y=20)

L2 = Label(GUI,text='ยินดีต้อนรับสู่ Python GUI World',font=('Angsana New',100,'bold'))
# L.pack()
L2.place(x=150,y=20)


GUI.mainloop()
