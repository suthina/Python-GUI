from tkinter import *
from tkinter import ttk # theme of Tk

GUI = Tk()
GUI.geometry('700x600')
GUI.title('โปรแกรมหมูกะทะ')

L = Label(GUI,text='โปรแกรมคำนวณราคาหมูกะทะ',font=('TH SarabunPSK',30,'bold'),fg='#9c42f5')
L.pack(pady=10)

###############หัวละ###################
L = Label(GUI,text='หัวละ(คน)',font=('TH SarabunPSK',25,'bold'),fg='#f542b0')
L.pack(pady=10)

L = Label(GUI,text='เด็ก 200 บาท',font=('TH SarabunPSK',20),fg='#f542b0')
L.place(x=120,y=120)

L = Label(GUI,text='ผู้ใหญ่ 250 บาท',font=('TH SarabunPSK',20),fg='#f542b0')
L.place(x=430,y=120)

v_chil = StringVar() #StringVar ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(GUI,textvariable=v_chil,font=('TH SarabunPSK',20))
E1.place(x=70,y=170)

v_adult = StringVar() #StringVar ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(GUI,textvariable=v_adult,font=('TH SarabunPSK',20))
E1.place(x=400,y=170)

###############เพิ่มเตา###################
L = Label(GUI,text='เพิ่มเตา (50 บาทต่อเตา)',font=('TH SarabunPSK',25,'bold'),fg='#42f542')
L.place(x=250,y=230)

v_tao = StringVar() #StringVar ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(GUI,textvariable=v_tao,font=('TH SarabunPSK',20))
E1.place(x=260,y=270)


###############BUTTON###################
def Calculate():
    personchil = int(v_chil.get()) # .get() ดึงข้อมูลจากตัวแปรที่เปลี่ยนเป็น StringVar
    calc_result = personchil * 200
    print('total bath: ',calc_result)


    personadult = int(v_adult.get()) # .get() ดึงข้อมูลจากตัวแปรที่เปลี่ยนเป็น StringVar
    cala_result = personadult * 250
    print('total bath: ',cala_result)

    totaltao = int(v_tao.get()) # .get() ดึงข้อมูลจากตัวแปรที่เปลี่ยนเป็น StringVar
    caltao_result = totaltao * 50
    print('total bath: ',caltao_result)

    caltotal = calc_result + cala_result + caltao_result
    print('total bath: ',caltotal)

    text_result1 = f'จำนวนเด็ก {personchil} คน ราคา {calc_result:,.2f} THB'
    text_result2 = f'จำนวนผู้ใหญ่ {personadult} คน ราคา {cala_result:,.2f} THB'
    text_result3 = f'จำนวนเพิ่มเตา {totaltao} เตา ราคา {caltao_result:,.2f} THB'
    text_result4 = f'รวมราคาทั้งหมด {caltotal:,.2f} THB'
    v_result1.set(text_result1)
    v_result2.set(text_result2)
    v_result3.set(text_result3)
    v_result4.set(text_result4)


B1 = ttk.Button(GUI,text='คำนวณราคา', command=Calculate)
B1.place(x=320,y=330)


v_result1 = StringVar()
v_result2 = StringVar()
v_result3 = StringVar()
v_result4 = StringVar()
result_display1 = ttk.Label(GUI,textvariable=v_result1,font=('TH SarabunPSK',20,),foreground='#f542b0')
result_display2 = ttk.Label(GUI,textvariable=v_result2,font=('TH SarabunPSK',20,),foreground='#f542b0')
result_display3 = ttk.Label(GUI,textvariable=v_result3,font=('TH SarabunPSK',20,),foreground='#42f542')
result_display4 = ttk.Label(GUI,textvariable=v_result4,font=('TH SarabunPSK',30,'bold'),foreground='#f70202')
result_display1.place(x=180,y=380)
result_display2.place(x=180,y=430)
result_display3.place(x=180,y=480)
result_display4.place(x=150,y=530)

GUI.mainloop()
