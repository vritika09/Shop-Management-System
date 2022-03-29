from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import sqlite3  as db

mainwindow=Tk()
mainwindow.title("Shop Management System")
tab = ttk.Notebook(mainwindow) 
w1= ttk.Frame(tab)
w2=ttk.Frame(tab)


tab.add(w2, text ='sell') 
tab.add(w1, text ='stock') 
tab.pack(expand = 1, fill ="both")

def establishconnect():
    connectobj = db.connect("shopManagement.db")
    c = connectobj.cursor()
    sql = '''
    create table if not exists sell (
        date string,
        product string,
        price number,
        quantity number,
        total number
        )
    '''
    c.execute(sql)
    connectobj.commit()   
 
establishconnect()

def connection2():
    connectobj2 = db.connect("shopManagement.db")
    c = connectobj2.cursor()
    sql = '''
    create table if not exists stock (
        date string,
        product string,
        price number,
        quantity number
        )
    '''
    c.execute(sql)
    connectobj2.commit()   
 
connection2()

def Stock():
    global dateE2,quantity,name,price
 
    connectobj = db.connect("shopManagement.db")
    c = connectobj.cursor()  
    sql = '''
            INSERT INTO stock VALUES 
            (?, ?, ?, ?)
            '''
    c.execute(sql,(dateE2.get(),name.get(),price.get(),quantity.get()))
    connectobj.commit()

def viewingStock():
    connectobj = db.connect("shopManagement.db")
    c = connectobj.cursor()  
 
    sql = 'Select * from stock'
    c.execute(sql)
 
    rows=c.fetchall()
    viewingarea2.insert(END,f"Date \tProduct\t  Price\t  Quantity\t \n")
    
    for i in rows:
        allrows=""
        for j in i:
            allrows+=str(j)+'\t'
        allrows+='\n'
        viewingarea2.insert(END,allrows)

dateL=Label(w1,text="Date",width=12,font=('arial',15,'bold'))
dateL.grid(row=0,column=0,padx=7,pady=7)
 
dateE2=DateEntry(w1,width=12,font=('arial',15,'bold'))
dateE2.grid(row=0,column=1,padx=7,pady=7)
 
l1=Label(w1, text="Product",font=('arial',15,'bold'),width=12)
l1.grid(row=1,column=0,padx=7,pady=7)
 
l1=Label(w1, text="Price",font=('arial',15,'bold'),width=12)
l1.grid(row=2,column=0,padx=7,pady=7)
 
l1=Label(w1, text="Quantity",font=('arial',15,'bold'),width=12)
l1.grid(row=3,column=0,padx=7,pady=7)
 
name=StringVar()
price=IntVar()
quantity=IntVar()
 
Name=Entry(w1,textvariable=name,font=('arial',15,'bold'),width=12)
Name.grid(row=1,column=1,padx=7,pady=7)
 
Price=Entry(w1,textvariable=price,font=('arial',15,'bold'),width=12)
Price.grid(row=2,column=1,padx=7,pady=7)
 
Quantity=Entry(w1,textvariable=quantity,font=('arial',15,'bold'),width=12)
Quantity.grid(row=3,column=1,padx=7,pady=7)
 
addbutton=Button(w1,command=Stock,text="Add",font=('arial',15,'bold'),bg="pink",width=20)
addbutton.grid(row=4,column=1,padx=7,pady=7)
 
viewingarea2=Text(w1)
viewingarea2.grid(row=5,column=0,columnspan=2)
 
viewbutton2=Button(w1,command=viewingStock,text="View Stock",font=('arial',15,'bold'),bg="pink",width=20 )
viewbutton2.grid(row=4,column=0,padx=7,pady=7)

def Bill():
    connectobj = db.connect("shopManagement.db")
    c = connectobj.cursor()  
 
    global areaforbill
    if p1quant.get()==0 and p2quant.get()==0 and p3quant.get()==0 and p4quant.get()==0:
        messagebox.showerror("Error","No product purchased")
    else:
        areaforbill.delete('1.0',END)
        areaforbill.insert(END,"\t|| Shop Management Project ||")
        areaforbill.insert(END,"\n_________________________________________\n")
        areaforbill.insert(END,"\nDate\t Products\tPrice\t   QTY\t Total")
        areaforbill.insert(END,"\n==========================================")
 
        price= IntVar()
        price2=IntVar()
        price3=IntVar()
        price4=IntVar()
 
        print(datee.get())
        price=price2=price3=price4=0
 
        if p1quant.get()!=0:
            price=p1quant.get()*pricep1.get()
            print(price)
            areaforbill.insert(END,f"\n{datee.get()}\t Product-1 \t{pricep1.get()}\t {p1quant.get()}\t {price}")
 
            sql = '''
            INSERT INTO Sell VALUES 
            (?, ?, ?, ?,?)
            '''
            c.execute(sql,(datee.get(),'Product-1',pricep1.get(),p1quant.get(),price))
            connectobj.commit() 
 
        if p2quant.get()!=0:
            price2=(p2quant.get()*pricep2.get())
            print(price2)
            areaforbill.insert(END,f"\n{datee.get()}\t Product-2 \t{pricep2.get()}\t {p2quant.get()}\t {price2}")
 
            sql = '''
            INSERT INTO Sell VALUES 
            (?, ?, ?, ?,?)
            '''
            print(datee.get(),'Product-2',pricep2.get(),p2quant.get(),price2)
            c.execute(sql,(datee.get(),'Product-2',pricep2.get(),p2quant.get(),price2))
            connectobj.commit() 
 
        if p3quant.get()!=0:
            price3=p3quant.get()*pricep1.get()
            print(price3)
            areaforbill.insert(END,f"\n{datee.get()}\tProduct-3 \t{pricep3.get()}\t {p3quant.get()}\t {price3}")
 
            sql = '''
            INSERT INTO Sell VALUES 
            (?, ?, ?, ?,?)
            '''
            c.execute(sql,(datee.get(),'Product-3',pricep3.get(),p3quant.get(),price3))
            connectobj.commit() 
 
        if p4quant.get()!=0:
            price4=p4quant.get()*pricep1.get()
            areaforbill.insert(END,f"\n{datee.get()}\tProduct-4 \t{pricep4.get()}\t {p4quant.get()}\t {price4}")
 
            sql = '''
            INSERT INTO Sell VALUES 
            (?, ?, ?, ?,?)
            '''
            c.execute(sql,(datee.get(),'Product-4',pricep4.get(),p4quant.get(),price4))
            connectobj.commit() 
 
        Total=IntVar()
        Total=price+price2+price3+price4
 
        quantity=IntVar()
        quantity=p1quant.get()+p2quant.get()+p3quant.get()+p4quant.get()
        areaforbill.insert(END,f"\nTotal \t \t  \t{quantity}\t {Total}")


def view():
    connectobj = db.connect("shopManagement.db")
    c = connectobj.cursor()  
 
    sql = 'Select * from Sell'
    c.execute(sql)
 
    rows=c.fetchall()
    viewingarea.insert(END,f"Date\t Product\t  Price of 1\t  Quantity\t  Price\n")
    
    
    for i in rows:
        allrows=""
        for j in i:
            allrows+=str(j)+'\t'
        allrows+='\n'
        viewingarea.insert(END,allrows)
 
datel=Label(w1,text="Date",width=12,font=('arial',15,'bold'))
datel.grid(row=0,column=0,padx=7,pady=7)
 
datee=DateEntry(w1,width=12,font=('arial',15,'bold'))
datee.grid(row=0,column=1,padx=7,pady=7)
 
l1=Label(w1, text="Product Name",font=('arial',15,'bold'),width=12)
l1.grid(row=1,column=0,padx=7,pady=7)
 
 
namep1=StringVar()
namep1.set('Maggie')
 
pricep1=IntVar()
pricep1.set(80)
 
p1quant=IntVar()
p1quant.set(0)
 
l1=Label(w2, text=namep1.get(),font=('arial',15,'bold'),width=12)
l1.grid(row=2,column=0,padx=7,pady=7)
 
l1=Label(w2, text=pricep1.get(),font=('arial',15,'bold'),width=12)
l1.grid(row=2,column=1,padx=7,pady=7)
 
t1=Entry(w2,textvariable=p1quant,font=('arial',15,'bold'),width=12)
t1.grid(row=2,column=2,padx=7,pady=7)
 
 
namep2=StringVar()
namep2.set('biscuits')
 
pricep2=IntVar()
pricep2.set(20)
 
p2quant=IntVar()
p2quant.set(0)
 
l1=Label(w2, text=namep2.get(),font=('arial',15,'bold'),width=12)
l1.grid(row=3,column=0,padx=7,pady=7)
 
l1=Label(w2, text=pricep2.get(),font=('arial',15,'bold'),width=12)
l1.grid(row=3,column=1,padx=7,pady=7)
 
t1=Entry(w2,textvariable=p2quant,font=('arial',15,'bold'),width=12)
t1.grid(row=3,column=2,padx=7,pady=7)
 
namep3=StringVar()
namep3.set('Noodles')
 
pricep3=IntVar()
pricep3.set(100)
 
p3quant=IntVar()
p3quant.set(0)
 
l1=Label(w2, text=namep3.get(),font=('arial',15,'bold'),width=12)
l1.grid(row=4,column=0,padx=7,pady=7)
 
l1=Label(w2, text=pricep3.get(),font=('arial',15,'bold'),width=12)
l1.grid(row=4,column=1,padx=7,pady=7)
 
t1=Entry(w2,textvariable=p3quant,font=('arial',15,'bold'),width=12)
t1.grid(row=4,column=2,padx=7,pady=7)
 
 
namep4=StringVar()
namep4.set('Rice')
 
pricep4=IntVar()
pricep4.set(60)
 
p4quant=IntVar()
p4quant.set(0)
 
l1=Label(w2, text=namep4.get(),font=('arial',15,'bold'),width=12)
l1.grid(row=5,column=0,padx=7,pady=7)
 
l1=Label(w2, text=pricep4.get(),font=('arial',15,'bold'),width=12)
l1.grid(row=5,column=1,padx=7,pady=7)
 
t1=Entry(w2,textvariable=p4quant,font=('arial',15,'bold'),width=12)
t1.grid(row=5,column=2,padx=7,pady=7)
 
areaforbill=Text(w2)
 
submitbutton=Button(w2,command=Bill,text="Bill",font=('arial',15,'bold'),bg="red",width=20 )
submitbutton.grid(row=6,column=2,padx=7,pady=7)
 
viewbutton=Button(w2,command=view,text="View All Sellings",font=('arial',15,'bold'),bg="red",width=20 )
viewbutton.grid(row=6,column=0,padx=7,pady=7)
 
areaforbill.grid(row=9,column=2)
viewingarea=Text(w2)
viewingarea.grid(row=9,column=0)
 
mainloop()
