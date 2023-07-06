from tkinter import *
from tkinter import ttk #Theme ของ Tk
import csv
from datetime import datetime

def writecsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file :
        fw = csv.writer(file)
        fw.writerow(data)

def readcsv():
    with open('data.csv',newline='',encoding='utf-8') as file:
              fr = list(csv.reader(file))
              #print(fr)
    return fr



GUI = Tk()
GUI.geometry('800x700') # กว้างxสูง
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')

FONT1 = ('TH SarabunPSK',25)

################################# Config TAB 1##########################################
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)

icon_Tab1 = PhotoImage(file='tab1.png')
icon_Tab2 = PhotoImage(file='tab2.png')

Tab.add(T1,text='บันทึกค่าใช้จ่าย',image=icon_Tab1,compound='left')
Tab.add(T2,text='ประวัติค่าใช้จ่าย',image=icon_Tab2,compound='left')
#################################TAB 1##################################################

#F1 = Frame(T1)
#F1.place(x=0,y=0)

#F1 = LabelFrame(T1,text='กรุณากรอกข้อมูล')
#F1.place(x=50,y=50)

# IMAGE
icon = 'C:\\Users\\ACER\\Desktop\\suthina\\Python GUI 2023\\Python GUI 2023\\expense.png'
# หรือ icon = r'C:\Users\ACER\Desktop\suthina\Python GUI 2023\Python GUI 2023\expense.png'
iconimage = PhotoImage(file=icon)
L = Label(T1,image=iconimage)
L.pack()

# ช่องรายการค่าใช้จ่าย
L = Label(T1,text='รายการค่าใช้จ่าย', font=(None,30))
L.pack(pady=5)

v_expense = StringVar()
E1 = ttk.Entry(T1, textvariable=v_expense, font=FONT1)
E1.pack(pady=5)

# ช่องกรอกจำนวนเงินค่าใช้จ่าย
L = Label(T1,text='จำนวนเงิน  (THB)', font=(None,30))
L.pack(pady=5)

v_amount = StringVar()
E2 = ttk.Entry(T1, textvariable=v_amount, font=FONT1)
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


B1 = ttk.Button(T1,text='บันทึก',command=SaveData)
B1.pack(ipadx=20,ipady=10,pady=5)
#หรือ B1.place(x=30,y=60)

#เพิ่มรูปในbutton
#B1 = ttk.Button(GUI,text='น้ำเต้าหู้',command=Fav1, image=iconimage, compound='top')
#B1.pack(ipadx=20,ipady=10,pady=5)

#################################TAB 2##################################################
#ค่ารถไฟฟ้า BTS,20,2023-01-11 8:00:05
header = ['ลำดับ','รายการ','ค่าใช้จ่าย','วัน-เวลา']
width = [70,300,150,170]

table = ttk.Treeview(T2, columns=header, show='headings',height=20)
table.pack()

# resize
style = ttk.Style()
style.configure('Treeview.Heading',font=(None,15))
style.configure('Treeview',font=(None,13),rowhight=30)

#table.column('ลำดับ',width=50)
#table.heading('ลำดับ',text='ลำดับ')

table.column('ค่าใช้จ่าย',anchor=E)
table.column('รายการ',anchor=CENTER)

for h,w in zip(header,width):
    table.column(h,width=w)
    table.heading(h,text=h)

#table.insert('','end',values=['A','B','C','D'])  # เรียก table แบบ manual
data = readcsv()

for i,d in enumerate(data,start=1):
     #d.insert(0,i)
     #table.insert('','end',values=d)
     table.insert('','end',values=[i,d[0],d[1],d[2]])

GUI.mainloop()
