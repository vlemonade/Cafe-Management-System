#Honeyvhen A. Villaluz (BSIT 2-5)

from tkinter import *
from tkinter import messagebox
import random
import time

def on_print():
   
    if costofcoffeevar.get() != '' or costofpastriesvar.get() != '':
        MsgBox=messagebox.askquestion("Print", "Do you want to continue printing?", icon = 'info')
        if MsgBox == 'yes':
            messagebox.showinfo('Printing','Receipt is printing.....')
        else:
            messagebox.showinfo('Return','You will now return to the application screen')
    else:
        messagebox.showerror('Error','No Item to Print, Please Select Item!')


def on_receipt():
        if costofcoffeevar.get() != '' or costofpastriesvar.get() != '':
            textReceipt.delete(1.0,END)
            x=random.randint(100,10000)
            billnumber='BILL'+str(x)
            date=time.strftime('%d/%m/%y')
            textReceipt.insert(END,'Receipt Ref:\t\t'+billnumber+'\t\t'+date+'\n')
            textReceipt.insert(END,'**********************************************************\n')
            textReceipt.insert(END,'Order:\t\tQty:\t\tPrice:\n')
            textReceipt.insert(END,'**********************************************************\n')
            if e_espresso.get()!='0':
                textReceipt.insert(END,f'Espresso\t\t{(e_espresso.get())}\t\t{int(e_espresso.get())*90}.00\n')
            if e_americano.get()!='0':
                textReceipt.insert(END,f'Americano\t\t{(e_americano.get())}\t\t{int(e_americano.get())*115}.00\n')  
            if e_macchiato.get()!='0':
                textReceipt.insert(END,f'Macchiato\t\t{(e_macchiato.get())}\t\t{int(e_macchiato.get())*145}.00\n')
            if e_latte.get()!='0':
                textReceipt.insert(END,f'Latte\t\t{(e_latte.get())}\t\t{int(e_latte.get())*135}.00\n')
            if e_cappuccino.get()!='0':
                textReceipt.insert(END,f'Cappuccino\t\t{(e_cappuccino.get())}\t\t{int(e_cappuccino.get())*135}.00\n')
            if e_chai_tea.get()!='0':
                textReceipt.insert(END,f'Cha Tea\t\t{(e_chai_tea.get())}\t\t{int(e_chai_tea.get())*110}.00\n')
            if e_hot_choco.get()!='0':
                textReceipt.insert(END,f'Hot Choco\t\t{(e_hot_choco.get())}\t\t{int(e_hot_choco.get())*100}.00\n')
            if e_biscotti.get()!='0':
                textReceipt.insert(END,f'Biscotti\t\t{(e_biscotti.get())}\t\t{int(e_biscotti.get())*80}.00\n')
            if e_cannoli.get()!='0':
                textReceipt.insert(END,f'Cannoli\t\t{(e_cannoli.get())}\t\t{int(e_cannoli.get())*70}.00\n')
            if e_muffins.get()!='0':
                textReceipt.insert(END,f'Muffins\t\t{(e_muffins.get())}\t\t{int(e_muffins.get())*65}.00\n')
            if e_croissant.get()!='0':
                textReceipt.insert(END,f'Croissant\t\t{(e_croissant.get())}\t\t{int(e_croissant.get())*100}.00\n')
            if e_danish.get()!='0':
                textReceipt.insert(END,f'Danish\t\t{(e_danish.get())}\t\t{int(e_danish.get())*110}.00\n')
            if e_pizzelle.get()!='0':
                textReceipt.insert(END,f'Pizzelle\t\t{(e_pizzelle.get())}\t\t{int(e_pizzelle.get())*210}.00\n')
            if e_cookies.get()!='0':
                textReceipt.insert(END,f'Cookies\t\t{(e_cookies.get())}\t\t{int(e_cookies.get())*40}.00\n')
               
            textReceipt.insert(END,'**********************************************************\n')
            textReceipt.insert(END,f'Sub Total:\t\t---------------\t\t{subtotal}.00\n\n')
            textReceipt.insert(END,f'Service Tax:\t\t---------------\t\t20.00\n\n')
            textReceipt.insert(END,f'Total Bill:\t\t---------------\t\t{totalbill}.00\n\n')
        else:
            messagebox.showerror('Error','No Is selected, Please Select Item!')
       
def on_total():
    global priceofcoffee, priceofpastries, subtotal, totalbill
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0:
       
        coffee1=int(e_espresso.get())
        coffee2=int(e_americano.get())
        coffee3=int(e_macchiato.get())
        coffee4 = int(e_latte.get())
        coffee5 = int(e_cappuccino.get())
        coffee6 = int(e_chai_tea.get())
        coffee7 = int(e_hot_choco.get())
       
        pastry8 = int(e_biscotti.get())
        pastry9 = int(e_cannoli.get())
        pastry10 = int(e_muffins.get())
        pastry11 = int(e_croissant.get())
        pastry12 = int(e_danish.get())
        pastry13 = int(e_pizzelle.get())
        pastry14 = int(e_cookies.get())
       
        priceofcoffee = (coffee1*90)+(coffee2*115)+(coffee3*145)+(coffee4*135)+(coffee5*135)+(coffee6*110)+(coffee7*100)
        priceofpastries = (pastry8*80)+(pastry9*70)+(pastry10*65)+(pastry11*100)+(pastry12*110)+(pastry13*210)+(pastry14*40)
        ServiceTaxvar.set('20.00')
        subtotal=priceofcoffee+priceofpastries
        SubTotalvar.set(str(subtotal)+'.00')
        costofcoffeevar.set(str(priceofcoffee)+'.00')
        costofpastriesvar.set(str(priceofpastries)+'.00')
        totalbill=subtotal+20
        Totalvar.set(str(totalbill)+'.00')
    else:
        messagebox.showerror('Error','No Is selected, Please Select Item!')

def on_reset():
    textReceipt.delete(1.0,END)
    e_espresso.set('0')
    e_americano.set('0')
    e_macchiato.set('0')
    e_latte.set('0')
    e_cappuccino.set('0')
    e_chai_tea.set('0')
    e_hot_choco.set('0')
    e_biscotti.set('0')
    e_cannoli.set('0')
    e_muffins.set('0')
    e_croissant.set('0')
    e_danish.set('0')
    e_pizzelle.set('0')
    e_cookies.set('0')
   
    textespresso.config(state=DISABLED)
    textamericano.config(state=DISABLED)
    textmacchiato.config(state=DISABLED)
    textlatte.config(state=DISABLED)
    textcappuccino.config(state=DISABLED)
    textchai_tea.config(state=DISABLED)
    texthot_choco.config(state=DISABLED)
    textbiscotti.config(state=DISABLED)
    textcannoli.config(state=DISABLED)
    textmuffins.config(state=DISABLED)
    textcroissant.config(state=DISABLED)
    textdanish.config(state=DISABLED)
    textpizzelle.config(state=DISABLED)
    textcookies.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)

    costofcoffeevar.set('')
    costofpastriesvar.set('')
    ServiceTaxvar.set('')
    SubTotalvar.set('')
    Totalvar.set('')
   



def espresso():
    if var1.get() == 1:
        textespresso.config(state=NORMAL)
        textespresso.focus()
        textespresso.delete(0, END)
    elif var1.get() == 0:
        textespresso.config(state=DISABLED)
        e_espresso.set('0')

def americano():
    if var2.get() == 1:
        textamericano.config(state=NORMAL)
        textamericano.focus()
        textamericano.delete(0, END)
    elif var2.get() == 0:
        textamericano.config(state=DISABLED)
        e_americano.set('0')

       
def macchiato():
    if var3.get() == 1:
        textmacchiato.config(state=NORMAL)
        textmacchiato.focus()
        textmacchiato.delete(0, END)
    elif var3.get() == 0:
        textmacchiato.config(state=DISABLED)
        e_macchiato.set('0')

       
def latte():
    if var4.get() == 1:
        textlatte.config(state=NORMAL)
        textlatte.focus()
        textlatte.delete(0, END)
    elif var4.get() == 0:
        textlatte.config(state=DISABLED)
        e_latte.set('0')

       
def cappuccino():
    if var5.get() == 1:
        textcappuccino.config(state=NORMAL)
        textcappuccino.focus()
        textcappuccino.delete(0, END)
    elif var5.get() == 0:
        textcappuccino.config(state=DISABLED)
        e_cappuccino.set('0')

       
def chai_tea():
    if var6.get() == 1:
        textchai_tea.config(state=NORMAL)
        textchai_tea.focus()
        textchai_tea.delete(0, END)
    elif var6.get() == 0:
        textchai_tea.config(state=DISABLED)
        e_chai_tea.set('0')

       
def hot_choco():
    if var7.get() == 1:
        texthot_choco.config(state=NORMAL)
        texthot_choco.focus()
        texthot_choco.delete(0, END)
    elif var7.get() == 0:
        texthot_choco.config(state=DISABLED)
        e_hot_choco.set('0')

def biscotti():
    if var8.get() == 1:
        textbiscotti.config(state=NORMAL)
        textbiscotti.focus()
        textbiscotti.delete(0, END)
    elif var8.get() == 0:
        textbiscotti.config(state=DISABLED)
        e_biscotti.set('0')
       
               
def cannoli():
    if var9.get() == 1:
        textcannoli.config(state=NORMAL)
        textcannoli.focus()
        textcannoli.delete(0, END)
    elif var9.get() == 0:
        textcannoli.config(state=DISABLED)
        e_cannoli.set('0')

               
def muffins():
    if var10.get() == 1:
        textmuffins.config(state=NORMAL)
        textmuffins.focus()
        textmuffins.delete(0, END)
    elif var10.get() == 0:
        textmuffins.config(state=DISABLED)
        e_muffins.set('0')
           
def croissant():
    if var11.get() == 1:
        textcroissant.config(state=NORMAL)
        textcroissant.focus()
        textcroissant.delete(0, END)
    elif var11.get() == 0:
        textcroissant.config(state=DISABLED)
        e_croissant.set('0')
       
def danish():
    if var12.get() == 1:
        textdanish.config(state=NORMAL)
        textdanish.focus()
        textdanish.delete(0, END)
    elif var12.get() == 0:
        textdanish.config(state=DISABLED)
        e_danish.set('0')
       
def pizzelle():
    if var13.get() == 1:
        textpizzelle.config(state=NORMAL)
        textpizzelle.focus()
        textpizzelle.delete(0, END)
    elif var13.get() == 0:
        textpizzelle.config(state=DISABLED)
        e_pizzelle.set('0')
       
def cookies():
    if var14.get() == 1:
        textcookies.config(state=NORMAL)
        textcookies.focus()
        textcookies.delete(0, END)
    elif var14.get() == 0:
        textcookies.config(state=DISABLED)
        e_cookies.set('0')

       
root=Tk()
root.geometry('1270x690+0+0')
root.resizable(0,0)
root.title('Cafe Management System by Honeyvhen Villaluz')
root.config(bg='#353C45')


#topframe
topFrame=Frame(root, bd=10, relief=RIDGE, bg="#353C45")
topFrame.pack(side=TOP)
labelTitle=Label(topFrame, text='Cafe Management System',font=('arial',29,'bold'),fg='#D9A322',bd=9, bg='#353C45',width=51)
labelTitle.grid(row=0,column=0)

#leftframe
leftFrame=Frame(root, bd=6, relief=RIDGE, bg='#353C45')
leftFrame.pack(side=LEFT)
costFrame=Frame(leftFrame,bd=4,relief=RIDGE,bg='#353C45',pady=7)
costFrame.pack(side=BOTTOM)
MenuFrame=Frame(leftFrame, bd=10,relief=RIDGE, bg='#353C45',padx=20)
MenuFrame.pack(side=LEFT)
CoffeeFrame=LabelFrame(leftFrame, text='Coffee', font=('arial',19,'bold'),bd=9,relief=RIDGE,pady=5,padx=10)
CoffeeFrame.pack(side=LEFT)
PastriesFrame=LabelFrame(leftFrame, text='Pastries', font=('arial',19,'bold'),bd=9,relief=RIDGE,pady=5, padx=10)
PastriesFrame.pack(side=LEFT)

#rightframe
rightFrame=Frame(root, bd=6, relief=RIDGE, bg='#353C45')
rightFrame.pack(side=RIGHT)
totalFrame=Frame(rightFrame,bd=10,relief=RIDGE, bg='#353C45')
totalFrame.pack()
receiptFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='#353C45')
receiptFrame.pack()
buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='#353C45')
buttonFrame.pack()

menu=Label(MenuFrame, text='MENU LIST',font =('arial',25,'bold'), fg='#BB86FC', bg='#353C45')
menu.grid(row=0, column=0)
Label(MenuFrame, text='COFFEE:',font =('arial',19,'bold'), fg='#BB86FC', bg='#353C45').grid(row=1, column=0,  ipady=4, sticky='w')
Label(MenuFrame, text='Espresso  ------------------  90.00',font =('arial',10,'italic'), fg='white', bg='#353C45').grid(row=2, column=0, sticky='w')
Label(MenuFrame, text='Americano  ---------------- 115.00',font =('arial',10,'italic'),fg='white', bg='#353C45').grid(row=3, column=0, sticky='w')
Label(MenuFrame, text='Macchiato  ---------------- 145.00',font =('arial',10,'italic'), fg='white', bg='#353C45').grid(row=4, column=0, sticky='w')
Label(MenuFrame, text='Latte      -------------------- 135.00',font =('arial',10,'italic'), fg='white', bg='#353C45').grid(row=5, column=0, sticky='w')
Label(MenuFrame, text='Cappuccino --------------- 135.00',font =('arial',10,'italic'), fg='white', bg='#353C45').grid(row=6, column=0, sticky='w')
Label(MenuFrame, text='Chai Tea   ----------------- 110.00',font =('arial',10,'italic'), fg='white', bg='#353C45').grid(row=7, column=0, sticky='w')
Label(MenuFrame, text='Hot Choco  ---------------- 100.00',font =('arial',10,'italic'), fg='white', bg='#353C45').grid(row=8, column=0, sticky='w')

Label(MenuFrame, text='PASTRIES:',font =('arial',19,'bold') , fg='#BB86FC', bg='#353C45').grid(row=9, column=0, ipady=5, sticky='w')
Label(MenuFrame, text='Biscotti  --------------------  80.00',font =('arial',10,'italic'), fg='white', bg='#353C45').grid(row=10, column=0, sticky='w')
Label(MenuFrame, text='Cannoli  --------------------- 70.00',font =('arial',10,'italic'), fg='white', bg='#353C45').grid(row=11, column=0, sticky='w')
Label(MenuFrame, text='Muffins  --------------------- 65.00',font =('arial',10,'italic'), fg='white', bg='#353C45').grid(row=12, column=0, sticky='w')
Label(MenuFrame, text='Croissant ----------------- 100.00',font =('arial',10,'italic'), fg='white', bg='#353C45').grid(row=13, column=0, sticky='w')
Label(MenuFrame, text='Danish --------------------- 110.00',font =('arial',10,'italic'), fg='white', bg='#353C45').grid(row=14, column=0, sticky='w')
Label(MenuFrame, text='Pizzelle ------------------- 210.00',font =('arial',10,'italic'), fg='white', bg='#353C45').grid(row=15, column=0, sticky='w')
Label(MenuFrame, text='Cookies -------------------- 40.00',font =('arial',10,'italic'), fg='white', bg='#353C45').grid(row=16, column=0, sticky='w')


var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()

var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()

e_espresso=StringVar()
e_americano=StringVar()
e_macchiato=StringVar()
e_latte=StringVar()
e_cappuccino=StringVar()
e_chai_tea=StringVar()
e_hot_choco=StringVar()

e_biscotti=StringVar()
e_cannoli=StringVar()
e_muffins=StringVar()
e_croissant=StringVar()
e_danish=StringVar()
e_pizzelle=StringVar()
e_cookies=StringVar()

costofcoffeevar=StringVar()
costofpastriesvar=StringVar()
ServiceTaxvar=StringVar()
SubTotalvar=StringVar()
Totalvar=StringVar()

e_espresso.set('0')
e_americano.set('0')
e_macchiato.set('0')
e_latte.set('0')
e_cappuccino.set('0')
e_chai_tea.set('0')
e_hot_choco.set('0')
e_biscotti.set('0')
e_cannoli.set('0')
e_muffins.set('0')
e_croissant.set('0')
e_danish.set('0')
e_pizzelle.set('0')
e_cookies.set('0')

espresso=Checkbutton(CoffeeFrame, text='Espresso',font=('arial',17,'bold'), onvalue=1,offvalue=0,variable=var1,command=espresso)
espresso.grid(row=0,column=0,sticky=W)
americano=Checkbutton(CoffeeFrame, text='Americano',font=('arial',17,'bold'),onvalue=1,offvalue=0,variable=var2, command=americano)
americano.grid(row=1,column=0,sticky=W)
macchiato=Checkbutton(CoffeeFrame, text='Macchiato',font=('arial',17,'bold'),onvalue=1,offvalue=0,variable=var3,command=macchiato)
macchiato.grid(row=2,column=0,sticky=W)
latte=Checkbutton(CoffeeFrame, text='Latte',font=('arial',17,'bold'),onvalue=1,offvalue=0,variable=var4, command=latte)
latte.grid(row=3,column=0,sticky=W)
cappuccino=Checkbutton(CoffeeFrame, text='Cappuccino',font=('arial',17,'bold'),onvalue=1,offvalue=0,variable=var5, command=cappuccino)
cappuccino.grid(row=4,column=0,sticky=W)
chai_tea=Checkbutton(CoffeeFrame, text='Chai Tea',font=('arial',17,'bold'),onvalue=1,offvalue=0,variable=var6, command=chai_tea)
chai_tea.grid(row=5,column=0,sticky=W)
hot_choco=Checkbutton(CoffeeFrame, text='Hot Choco',font=('arial',17,'bold'),onvalue=1,offvalue=0,variable=var7, command=hot_choco)
hot_choco.grid(row=6,column=0,sticky=W)

textespresso=Entry(CoffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_espresso)
textespresso.grid(row=0,column=1, pady=7)
textamericano=Entry(CoffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_americano)
textamericano.grid(row=1,column=1, pady=7)
textmacchiato=Entry(CoffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_macchiato)
textmacchiato.grid(row=2,column=1, pady=7)
textlatte=Entry(CoffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_latte)
textlatte.grid(row=3,column=1, pady=7)
textcappuccino=Entry(CoffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cappuccino)
textcappuccino.grid(row=4,column=1, pady=7)
textchai_tea=Entry(CoffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chai_tea)
textchai_tea.grid(row=5,column=1, pady=7)
texthot_choco=Entry(CoffeeFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_hot_choco)
texthot_choco.grid(row=6,column=1, pady=7, padx = 10)


biscotti=Checkbutton(PastriesFrame, text='Biscotti',font=('arial',17,'bold'), onvalue=1,offvalue=0,variable=var8, command=biscotti)
biscotti.grid(row=0,column=0,sticky=W)
cannoli=Checkbutton(PastriesFrame, text='Cannoli',font=('arial',17,'bold'),onvalue=1,offvalue=0,variable=var9, command=cannoli)
cannoli.grid(row=1,column=0,sticky=W)
muffins=Checkbutton(PastriesFrame, text='Muffins',font=('arial',17,'bold'),onvalue=1,offvalue=0,variable=var10, command=muffins)
muffins.grid(row=2,column=0,sticky=W)
croissant=Checkbutton(PastriesFrame, text='Croissant',font=('arial',17,'bold'),onvalue=1,offvalue=0,variable=var11, command=croissant)
croissant.grid(row=3,column=0,sticky=W)
danish=Checkbutton(PastriesFrame, text='Danish',font=('arial',17,'bold'),onvalue=1,offvalue=0,variable=var12, command=danish)
danish.grid(row=4,column=0,sticky=W)
pizzelle=Checkbutton(PastriesFrame, text='Pizzelle',font=('arial',17,'bold'),onvalue=1,offvalue=0,variable=var13, command=pizzelle)
pizzelle.grid(row=5,column=0,sticky=W)
cookies=Checkbutton(PastriesFrame, text='Cookies',font=('arial',17,'bold'),onvalue=1,offvalue=0,variable=var14, command=cookies)
cookies.grid(row=6,column=0,sticky=W)

textbiscotti=Entry(PastriesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_biscotti)
textbiscotti.grid(row=0,column=1, pady=7)
textcannoli=Entry(PastriesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cannoli)
textcannoli.grid(row=1,column=1, pady=7)
textmuffins=Entry(PastriesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_muffins)
textmuffins.grid(row=2,column=1, pady=7)
textcroissant=Entry(PastriesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_croissant)
textcroissant.grid(row=3,column=1, pady=7)
textdanish=Entry(PastriesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_danish)
textdanish.grid(row=4,column=1, pady=7)
textpizzelle=Entry(PastriesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pizzelle)
textpizzelle.grid(row=5,column=1, pady=7)
textcookies=Entry(PastriesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cookies)
textcookies.grid(row=6,column=1, pady=7, padx = 20)

labelCostofCoffee=Label(costFrame,text='Total Cost of Coffee',font=('arial',16,'bold'),bg='#353C45',fg='white')
labelCostofCoffee.grid(row=0,column=0)
textCostofCoffee=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcoffeevar)
textCostofCoffee.grid(row=0,column=1,padx=41, pady=8)

labelCostofPastries=Label(costFrame,text='Total cost of Pastries',font=('arial',16,'bold'),bg='#353C45',fg='white')
labelCostofPastries.grid(row=1,column=0)
textCostofPastries=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofpastriesvar)
textCostofPastries.grid(row=1,column=1,padx=41, pady=8)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='#353C45',fg='white')
labelServiceTax.grid(row=0,column=2)
textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=ServiceTaxvar)
textServiceTax.grid(row=0,column=3,padx=41, pady=8)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='#353C45',fg='white')
labelSubTotal.grid(row=1,column=2)
textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=SubTotalvar)
textSubTotal.grid(row=1,column=3,padx=41, pady=8)

labelTotal=Label(totalFrame,text='Total Bill',font=('arial',16,'bold'),bg='#353C45',fg='white')
labelTotal.grid(row=0,column=0, padx=13)
textTotal=Entry(totalFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=Totalvar)
textTotal.grid(row=0,column=1,padx=25, pady=12)

Label(receiptFrame, text='BILL AREA',font=('arial',20,'bold'),bg='#353C45',fg='white').grid(row=0, column=0)

textReceipt=Text(receiptFrame,font=('arial',12,'bold'),bd=3,width=40,height=21)
textReceipt.grid(row=1,column=0)

#buttons
btnTotal=Button(buttonFrame, text='Total',font=('arial',15,'bold'),bg='#BB86FC',fg='black', padx=9, pady=8, command=on_total)
btnTotal.grid(row=0, column=0)
btnReceipt=Button(buttonFrame, text='Receipt',font=('arial',15,'bold'),bg='#BB86FC',fg='black', padx=9, pady=8, command=on_receipt)
btnReceipt.grid(row=0, column=1)
btnPrint=Button(buttonFrame, text='Print',font=('arial',15,'bold'),bg='#BB86FC',fg='black', padx=9, pady=8, command=on_print)
btnPrint.grid(row=0, column=2)
btnReset=Button(buttonFrame, text='Reset',font=('arial',15,'bold'),bg='#BB86FC',fg='black', padx=9, pady=8, command=on_reset)
btnReset.grid(row=0, column=3)

root.mainloop()