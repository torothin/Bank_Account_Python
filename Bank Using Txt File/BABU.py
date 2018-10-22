from tkinter import *
import time
from datetime import datetime as dt
import pandas
"""
class DepositWindow(object):
    def __init__(self,window,account_path):
        top=self.top=Toplevel(window)
        self.account_path=account_path
        self.top.wm_title("Deposit")
        self.top.resizable(0,0)
        self.l1=Label(top,text="Amount")
        self.l1.grid(row=0, column=0)
        self.e1=Entry(top, width=30)
        self.e1.grid(row=0, column=1, padx=10, pady=5)
        self.l2=Label(top,text="Notes")
        self.l2.grid(row=1, column=0)
        self.e2=Entry(top, width=30)
        self.e2.grid(row=1, column=1, padx=10, pady=5)
        self.b=Button(top,text='Ok',command=self.deposit_command, width=10, height=2)
        self.b.grid(row=2, column=0, columnspan=2, padx=2, pady=10)

    def deposit_command(self):
        deposit_value=self.e1.get()
        note_value=self.e2.get()
        with open(self.account_path, 'a') as file:
            file.write(str(dt(dt.now().year, dt.now().month, dt.now().day,dt.now().hour,dt.now().minute,dt.now().second)) + "," + deposit_value + "," + note_value + "\n")
        self.top.destroy()
        m.view()

class WithdrawWindow(object):
    def __init__(self,window,account_path):
        top=self.top=Toplevel(window)
        self.account_path=account_path
        self.top.wm_title("Withdraw")
        self.top.resizable(0,0)
        self.l1=Label(top,text="Amount")
        self.l1.grid(row=0, column=0)
        self.e1=Entry(top, width=30)
        self.e1.grid(row=0, column=1, padx=10, pady=5)
        self.l2=Label(top,text="Notes")
        self.l2.grid(row=1, column=0)
        self.e2=Entry(top, width=30)
        self.e2.grid(row=1, column=1, padx=10, pady=5)
        self.b=Button(top,text='Ok',command=self.withdraw_command, width=10, height=2)
        self.b.grid(row=2, column=0, columnspan=2, padx=2, pady=10)

    def withdraw_command(self):
        withdraw_value=str(float(self.e1.get())*-1)
        note_value=self.e2.get()
        with open(self.account_path, 'a') as file:
            file.write(str(dt(dt.now().year, dt.now().month, dt.now().day,dt.now().hour,dt.now().minute,dt.now().second)) + "," + withdraw_value + "," + note_value + "\n")
        self.top.destroy()
        m.view()
"""
class popupWindow(object):
    def __init__(self,window,account_path):
        self.account_path=account_path
        self.l1=Label(self.top,text="Amount")
        self.l1.grid(row=0, column=0)
        self.e1=Entry(self.top, width=30)
        self.e1.grid(row=0, column=1, padx=10, pady=5)
        self.l2=Label(self.top,text="Notes")
        self.l2.grid(row=1, column=0)
        self.e2=Entry(self.top, width=30)
        self.e2.grid(row=1, column=1, padx=10, pady=5)


class DepositWindow(popupWindow):
    def __init__(self,window,account_path):
        top=self.top=Toplevel(window)
        self.top.resizable(0,0)
        self.account_path=account_path
        popupWindow.__init__(self,window,self.account_path)
        self.top.wm_title("Deposit")
        self.top.b=Button(top,text='Ok',command=self.deposit_command, width=10, height=2)
        self.top.b.grid(row=2, column=0, columnspan=2, padx=2, pady=10)

    def deposit_command(self):
        deposit_value=self.e1.get()
        note_value=self.e2.get()
        with open(self.account_path, 'a') as file:
            file.write(str(dt(dt.now().year, dt.now().month, dt.now().day,dt.now().hour,dt.now().minute,dt.now().second)) + "," + deposit_value + "," + note_value + "\n")
        self.top.destroy()
        m.view()

class WithdrawWindow(popupWindow):
    def __init__(self,window,account_path):
        top=self.top=Toplevel(window)
        self.top.resizable(0,0)
        self.account_path=account_path
        popupWindow.__init__(self,window,self.account_path)
        self.top.wm_title("Withdraw")
        self.top.b=Button(top,text='Ok',command=self.withdraw_command, width=10, height=2)
        self.top.b.grid(row=2, column=0, columnspan=2, padx=2, pady=10)

    def withdraw_command(self):
        withdraw_value=str(float(self.e1.get())*-1)
        note_value=self.e2.get()
        with open(self.account_path, 'a') as file:
            file.write(str(dt(dt.now().year, dt.now().month, dt.now().day,dt.now().hour,dt.now().minute,dt.now().second)) + "," + withdraw_value + "," + note_value + "\n")
        self.top.destroy()
        m.view()

class mainWindow(object):
    def __init__(self,window,account_path):
        self.window=window
        self.account_path=account_path
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

        self.list1=Listbox(window, height=30, width=57)
        self.list1.grid(row=2, column=0, columnspan=5)
        self.sb1=Scrollbar(window)
        self.sb1.grid(row=2, column=6,sticky="NS")
        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>') #,self.delete_line

        self.b1=Button(window,text="Deposit",width=15, command=self.deposit_popup)
        self.b1.grid(row=3, column=0, columnspan=2)
        self.b2=Button(window, text="Withdrawl", width=15, command=self.withdraw_popup)
        self.b2.grid(row=3, column=2, columnspan=2)
        self.b3=Button(window, text="Delete Entry", width=15, command=self.delete_line)
        self.b3.grid(row=3, column=4, columnspan=2)


    def delete_line(self):
        global selected_tuple
        index=self.list1.curselection()[0]+1
        self.selected_tuple=self.list1.get(index)
        with open(self.account_path, 'r') as fr:
            lines = fr.readlines()
            if index in range(len(lines)):

                del lines[index]

        with open(self.account_path, 'w') as fw:
            fw.writelines(lines)
        self.view()

    def view(self):
        self.df=pandas.read_csv(self.account_path)
        self.list1.delete(0, END)
        for datetime,notes,amount in zip(self.df['DateTime'],self.df['Notes'],self.df['Amount']):
            value=datetime+"   "+str(amount.item())+"    "+notes
            self.list1.insert(END,value)
        self.balance()

    def balance(self):
        value=0
        for amount in self.df['Amount']:
            value=value+float(amount)
        self.e2.delete(0, END)
        self.e2.insert(END,value)

    def deposit_popup(self):
        self.top=DepositWindow(self.window,self.account_path)

    def withdraw_popup(self):
        self.w=WithdrawWindow(self.window,self.account_path)

    def entryValue(self):
        return self.w.value

class checkingWindow(mainWindow):
    def __init__(self, window, account_number, account_path):
        self.account_number=account_number
        self.account_path=account_path
        mainWindow.__init__(self,window,self.account_path)
        self.e1.insert(END,self.account_number)
        self.window.wm_title("Bank App-Checking Account")
        self.view()

class savingWindow(mainWindow):
    def __init__(self, window, account_number, account_path):
        self.account_number=account_number
        self.account_path=account_path
        mainWindow.__init__(self,window,self.account_path)
        self.e1.insert(END,self.account_number)
        self.window.wm_title("Bank App-Saving Account")
        self.view()

window=Tk()
m=checkingWindow(window, 123456, "BankAccount.txt")
window.mainloop()
