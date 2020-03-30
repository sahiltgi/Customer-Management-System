import tkinter
from tkinter import *
import tkinter.messagebox
from CustomerBLL import Customer


class CustomerForm(Frame):
    countIndex = 0

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.lblid = Label(self, text="Customer Id")
        self.lblid.grid(row=0, column=0, columnspan=2)
        self.lblName = Label(self, text="Customer Name")
        self.lblName.grid(row=1, column=0, columnspan=2)
        self.lblAddress = Label(self, text="Customer Address")
        self.lblAddress.grid(row=2, column=0, columnspan=2)
        self.txtid = Entry(self, text="Customer Id")
        self.varid = IntVar()
        self.txtid["textvariable"] = self.varid
        self.txtid.grid(row=0, column=2, columnspan=2)
        self.txtName = Entry(self, text="Customer Id")
        self.varName = StringVar()
        self.txtName["textvariable"] = self.varName
        self.txtName.grid(row=1, column=2, columnspan=2)
        self.txtAddress = Entry(self, text="Customer Address")
        self.varAddress = StringVar()
        self.txtAddress["textvariable"] = self.varAddress
        self.txtAddress.grid(row=2, column=2, columnspan=2)
        self.btnAdd = Button(self, text="Add", width=7, command=self.btnAdd_Click).grid(row=3, column=0)
        self.btnGetDetails = Button(self, text="Details", width=7, command=self.btnGetDetails_Click).grid(row=3,
                                                                                                          column=1)
        self.btnDelete = Button(self, text="Delete", width=7, command=self.btnDelete_Click).grid(row=3, column=2)
        self.btnModify = Button(self, text="Update", width=7, command=self.btnUpdate_Click).grid(row=3, column=3)
        self.btnFirst = Button(self, text="First", width=7, command=self.btnFirst_Click).grid(row=4, column=0)
        self.btnPrev = Button(self, text="Prev", width=7, command=self.btnPrev_Click).grid(row=4, column=1)
        self.btnNext = Button(self, text="Next", width=7, command=self.btnNext_Click).grid(row=4, column=2)
        self.btnModify = Button(self, text="Last", width=7, command=self.btnLast_Click).grid(row=4, column=3)
        # self.btnLoadData = Button(self, text="Load",width=7, command=self.btnLoadData_Click).grid(row=5, column=1)
        # self.btnSaveData = Button(self, text="Save",width=7, command=self.btnSaveData_Click).grid(row=5, column=2)
        # self.btnSort = Button(self, text="Sort",width=7, command=self.btnSort_Click).grid(row=5, column=3)
        # # Button.bind(self.btnSort,"<Enter>",self.mouse_Enter)
        # self.btnSort.bind("<Enter>",self.mouse_Enter)

    def mouse_Enter(self):
        tkinter.messagebox.showinfo("Sucess!", "Customer Enter Sucessfully")

    def btnAdd_Click(self):
        global countIndex
        try:
            cus = Customer()
            cus.id = self.varid.get()
            cus.Name = self.varName.get()
            cus.address = self.varAddress.get()
            cus.addCustomer()
            tkinter.messagebox.showinfo("Sucess!", "Customer Added Sucessfully")
            Customer.FillCustomerList()
            countIndex = 0
        except Exception as ex:
            tkinter.messagebox.showinfo("Failure!", ex)

    def btnGetDetails_Click(self):
        try:
            cus = Customer()

            cus.getDetails(self.varid.get())
            self.varid.set(cus.id)
            self.varName.set(cus.Name)
            self.varAddress.set(cus.address)
        except Exception as ex:
            tkinter.messagebox.showinfo("Failure!", ex)

    def btnDelete_Click(self):
        global countIndex
        try:
            cus = Customer()
            cus.deleteCus(self.varid.get())
            tkinter.messagebox.showinfo("Sucess!", "Customer Deleted Sucessfully")
            Customer.FillCustomerList()
            countIndex = 0
        except Exception as ex:
            tkinter.messagebox.showinfo("Failure!", ex)

    def btnUpdate_Click(self):
        global countIndex
        try:
            cus = Customer()
            cus.id = self.varid.get()
            cus.Name = self.varName.get()
            cus.address = self.varAddress.get()
            cus.updateCus()
            tkinter.messagebox.showinfo("Sucess!", "Customer Updated Sucessfully")
            Customer.FillCustomerList()
            countIndex = 0

        except Exception as ex:
            tkinter.messagebox.showinfo("Failure!", ex)

    def showCustomerByIndex(self, index):
        if (len(Customer.cusList) != 0):
            self.varid.set(Customer.cusList[index].id)
            self.varName.set(Customer.cusList[index].Name)
            self.varAddress.set(Customer.cusList[index].address)

    def btnFirst_Click(self):
        CustomerForm.countIndex = 0
        self.showCustomerByIndex(CustomerForm.countIndex)

    def btnPrev_Click(self):
        if (CustomerForm.countIndex > 0):
            CustomerForm.countIndex -= 1
        self.showCustomerByIndex(CustomerForm.countIndex)

    def btnNext_Click(self):
        if (CustomerForm.countIndex < len(Customer.cusList) - 1):
            CustomerForm.countIndex += 1
        self.showCustomerByIndex(CustomerForm.countIndex)

    def btnLast_Click(self):
        CustomerForm.countIndex = len(Customer.cusList) - 1
        self.showCustomerByIndex(CustomerForm.countIndex)

    def btnLoadData_Click(self):
        Customer.loadDatafromFile_Pickle()
        tkinter.messagebox.showinfo("Sucess!", "Data Loaded Sucessfully")

    def btnSaveData_Click(self):
        Customer.saveDatainFile_Pickle()
        tkinter.messagebox.showinfo("Sucess!", "Data Saved Sucessfully")

    def btnSort_Click(self):
        Customer.sortCustomer()
        tkinter.messagebox.showinfo("Sucess!", "Customer Sorted Sucessfully")


root = Tk()
Customer.FillCustomerList()
cusForm = CustomerForm(master=root)
root.title("Customer Form")
root.mainloop()
