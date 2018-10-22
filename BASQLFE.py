#Brad Duvall
#3/7/17
#
#BASQLFE.py
#
#Bank App using Tkinter, SQLite3, datetime, and locale.
#This app has a front end which implements tkinter to display bank info, deposit and
#   withdraw history
#The backend uses sqlite3 to store the data generated by the user and the frontend
#The frontend has two main classes, mainWindow and popupWindow.
#   The main window class has two subclasses, checkingWindow and savingWindow
#The purpose of a checkingWindow and a savingWindow was to have the potential for
#   additional features to distingish between a savings and checking account
#popupWindow has three subclasses, DepositWindow, WithdrawWindow and UpdateWindow.
#

from tkinter import *
from tkinter import ttk
from datetime import datetime as dt
from BASQLBE import Database
import locale

locale.setlocale(locale.LC_ALL, '')

class popupWindow(object):
    '''Base class for all popupwindows.  DepositWindow, WithdrawWindow and UpdateWindow'''
    def __init__(self,window,account_path):
        self.account_path=account_path
        self.l1=Label(self.top,text="Amount")
        self.l1.grid(row=2, column=0)
        self.e1=Entry(self.top, width=30)
        self.e1.grid(row=2, column=1, padx=10, pady=5)
        self.l2=Label(self.top,text="Notes")
        self.l2.grid(row=3, column=0)
        self.e2=Entry(self.top, width=30)
        self.e2.grid(row=3, column=1, padx=10, pady=5)

class DepositWindow(popupWindow):
    '''Subclass for popupWindow'''
    def __init__(self,window,account_path):
        top=self.top=Toplevel(window)
        self.top.resizable(0,0)
        self.account_path=account_path
        popupWindow.__init__(self,window,self.account_path)
        self.top.wm_title("Deposit")
        self.top.b=Button(top,text='Ok',command=self.deposit_command, width=10, height=2)
        self.top.b.grid(row=4, column=0, columnspan=2, padx=2, pady=10)

    def deposit_command(self):
        deposit_value=float(self.e1.get())
        m.current_datetime()
        note_value=self.e2.get().replace(" ", "_")
        m.database.insert(m.date, m.time, deposit_value, note_value)
        self.top.destroy()
        m.commit_command()
        m.view_command()

class WithdrawWindow(popupWindow):
    '''Subclass for popupWindow'''
    def __init__(self,window,account_path):
        top=self.top=Toplevel(window)
        self.top.resizable(0,0)
        self.account_path=account_path
        popupWindow.__init__(self,window,self.account_path)
        self.top.wm_title("Withdraw")
        self.top.b=Button(top,text='Ok',command=self.withdraw_command, width=10, height=2)
        self.top.b.grid(row=4, column=0, columnspan=2, padx=2, pady=10)

    def withdraw_command(self):
        withdraw_value=float(self.e1.get())*-1
        m.current_datetime()
        note_value=self.e2.get()
        m.database.insert(m.date, m.time, withdraw_value, note_value)
        self.top.destroy()
        m.commit_command()
        m.view_command()

class UpdateWindow(popupWindow):
    '''Subclass for popupWindow'''
    def __init__(self,window,account_path, index):
        self.index=index
        top=self.top=Toplevel(window)
        self.top.resizable(0,0)
        self.account_path=account_path
        popupWindow.__init__(self,window,self.account_path)
        self.top.wm_title("Update")
        self.l3=Label(self.top,text="Date")
        self.l3.grid(row=0, column=0)
        self.e3=Entry(self.top, width=30)
        self.e3.grid(row=0, column=1, padx=10, pady=5)
        self.top.b=Button(top,text='Ok',command=self.update_command, width=10, height=2)
        self.top.b.grid(row=4, column=0, columnspan=2, padx=2, pady=10)

        self.e1.delete(0,END)
        self.e1.insert(END,m.database.view_row(self.index)[0][3])
        self.e2.delete(0,END)
        self.e2.insert(END,m.database.view_row(self.index)[0][4])
        self.e3.delete(0,END)
        self.e3.insert(END,m.database.view_row(self.index)[0][1])

    def update_command(self):
        date=self.e3.get()
        time=m.database.view_row(self.index)[0][2]
        value=self.e1.get()
        notes=self.e2.get()
        m.database.update(date, time, value, notes, self.index)
        self.top.destroy()
        m.commit_command()
        m.view_command()

class mainWindow(object):
    '''This is the base class for the app.  checkingWindow and savingWindow are subclasses.
    This class creates the app window'''
    def __init__(self,window,account_path):
        self.database=Database(account_path)
        self.window=window
        self.window.resizable(0,0)

        self.l1=Label(window, justify="right", text="Account Number")
        self.l1.grid(row=0, column=0)
        self.e1_value=StringVar()
        self.e1=Entry(window, textvariable=self.e1_value, width=30)
        self.e1.grid(row=0, column=2, columnspan=5)

        self.l2=Label(window, justify="right", text="Current Balance")
        self.l2.grid(row=1, column=0)
        self.e2_value=StringVar()
        self.e2=Entry(window, textvariable=self.e2_value, width=30)
        self.e2.grid(row=1, column=2, columnspan=5)

        tree_columns = ("Date", "Amount", "Notes")
        self.tree = ttk.Treeview(window,columns=tree_columns, show="headings")
        self.tree.grid(row=2, column=0, columnspan=5)
        self.tree.column("Date",width=75)
        self.tree.column("Amount",width=70,anchor=E)
        self.tree.column("Notes",width=190)
        self.sb1=Scrollbar(window)
        self.sb1.grid(row=2, column=6,sticky="NS")
        self.tree.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.tree.yview)

        self.b1=Button(window,text="Deposit",width=14, command=self.deposit_popup)
        self.b1.grid(row=3, column=0, columnspan=2)
        self.b2=Button(window, text="Withdrawl", width=14, command=self.withdraw_popup)
        self.b2.grid(row=3, column=2, columnspan=2)
        self.b3=Button(window, text="Delete Entry", width=14, command=self.delete_line)
        self.b3.grid(row=4, column=0, columnspan=2)
        self.b4=Button(window, text="Update Entry", width=14, command=self.update_line)
        self.b4.grid(row=4, column=2, columnspan=2)

        for col in tree_columns:
            self.tree.heading(col, text=col.title(),command=lambda c=col: sortby(self.tree, c, 0)) #I dont understand this code

    def current_datetime(self):
        current_datetime=dt.today()
        self.date=current_datetime.strftime("%d/%b/%y")
        self.time=current_datetime.strftime("%H:%M")

    def delete_line(self):
        index = (self.tree.index(self.tree.focus())+1)
        self.database.delete(index)
        self.commit_command()
        self.view_command()

    def update_line(self):
        self.index = (self.tree.index(self.tree.focus())+1)
        self.w=UpdateWindow(self.window,self.account_path, self.index)

    def view_command(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for row in self.database.view():
            value=row[1]+" "+locale.currency(row[3], grouping=True)+" "+row[4]
            self.tree.insert('','end', values=value)
        self.balance()

    def commit_command(self):
        self.database.commit()

    def balance(self):
        value=0
        for row in self.database.view():
            value=value+row[3]
        self.e2.delete(0, END)
        self.e2.insert(END,locale.currency(value, grouping=True))

    def deposit_popup(self):
        self.w=DepositWindow(self.window,self.account_path)

    def withdraw_popup(self):
        self.w=WithdrawWindow(self.window,self.account_path)

class checkingWindow(mainWindow):
    '''subclass of mainWindow'''
    def __init__(self, window, account_number, account_path):
        self.account_number=account_number
        self.account_path=account_path
        mainWindow.__init__(self,window,self.account_path)
        self.e1.insert(END,self.account_number)
        self.window.wm_title("Bank App-Checking Account")
        self.view_command()

class savingWindow(mainWindow):
    '''subclass of mainWindow'''
    def __init__(self, window, account_number, account_path):
        self.account_number=account_number
        self.account_path=account_path
        mainWindow.__init__(self,window,self.account_path)
        self.e1.insert(END,self.account_number)
        self.window.wm_title("Bank App-Savings Account")
        self.view_command()

window=Tk()
m=checkingWindow(window, 123456, "BradsChecking.db")
window.mainloop()
