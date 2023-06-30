from tkinter import *
from tkinter import ttk #Theme ของ Tk
import csv
from datetime import datetime

def writecsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file :
        fw = csv.writer(file)
        fw.writerow(data)

GUI = Tk()
GUI.geometry('600x600')
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')

FONT1 = ('TH SarabunPSK',25)

# IMAGE
icon = 'C:\\Users\\ACER\\Desktop\\suthina\\Python GUI 2023\\Python GUI 2023\\expense.png'
# หรือ icon = r'C:\Users\ACER\Desktop\suthina\Python GUI 2023\Python GUI 2023\expense.png'
iconimage = PhotoImage(file=icon)
L = Label(GUI,image=iconimage)
L.pack()

# ช่องรายการค่าใช้จ่าย
L = Label(GUI,text='รายการค่าใช้จ่าย', font=(None,30))
L.pack(pady=5)

v_expense = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_expense, font=FONT1)
E1.pack(pady=5)

# ช่องกรอกจำนวนเงินค่าใช้จ่าย
L = Label(GUI,text='จำนวนเงิน  (THB)', font=(None,30))
L.pack(pady=5)

v_amount = StringVar()
E2 = ttk.Entry(GUI, textvariable=v_amount, font=FONT1)
E2.pack(pady=5)

# ปุ่มบันทึกข้อมูล

def SaveData(event=None):
    expense = v_expense.get()
    amount = float(v_amount.get())
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = (expense, amount,timestamp)
    writecsv(data)
    v_expense.set('')
    v_amount.set('')
    E1.focus()

E2.bind('<Return>',SaveData) # event=None
E1.bind('<Return>', lambda x: E2.focus()) # ฟังก์ชั่นพิเศษ bind โดยไม่ต้องสร้างฟังก์ชั่น


def Fav1(event=None):
    v_expense.set('น้ำเต้าหู้')
    v_amount.set('15')


GUI.bind('<F1>',Fav1)


B1 = ttk.Button(GUI,text='บันทึก',command=SaveData)
B1.pack(ipadx=20,ipady=10,pady=5)
#หรือ B1.place(x=30,y=60)

#เพิ่มรูปในbutton
#B1 = ttk.Button(GUI,text='น้ำเต้าหู้',command=Fav1, image=iconimage, compound='top')
#B1.pack(ipadx=20,ipady=10,pady=5)


GUI.mainloop()
