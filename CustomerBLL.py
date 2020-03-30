import pymysql
class Customer:
    #To run this project Create a database with any name
    # and create table with name Customer with column Id int,Name varchar(50),Address Varchar(250)
    #you have to change user,password,database accordind to ur database and mysql setting
    myCon = pymysql.connect(host="localhost", user="root", password="sahil123", database="cms")
    cusList = []

    def __init__(self):
        print()
        self.id=0
        self.Name=""
        self.address=""

    def addCustomer(self):
        try:
            myCursor = Customer.myCon.cursor()
            strQuery = "insert into Customer values(%s,%s,%s)"
            myCursor.execute(strQuery,(self.id,self.Name,self.address))
            Customer.myCon.commit()
        except Exception as ex:
            Customer.myCon.rollback()
            raise Exception(ex)

    def getDetails(self,id):
        myCursor = Customer.myCon.cursor()
        strQuery = "select * from Customer where id=%s"
        rowAffected=myCursor.execute(strQuery, (id))
        if(rowAffected!=0):
            row=myCursor.fetchone()
            self.id = row[0]
            self.Name = row[1]
            self.address = row[2]

        else:
            raise Exception("Id Not Found")


    def deleteCus(self,id):
        myCursor = Customer.myCon.cursor()
        strQuery = "delete from Customer where id=%s"
        rowAffected = myCursor.execute(strQuery, (id))
        Customer.myCon.commit()
        if (rowAffected == 0):
            raise Exception("Id not found")

    def updateCus(self):
        myCursor = Customer.myCon.cursor()
        strQuery = "update Customer set name=%s,address=%s where id=%s"
        rowAffected = myCursor.execute(strQuery, (self.Name,self.address,self.id))
        Customer.myCon.commit()
        if (rowAffected == 0):
            raise Exception("Id not found")

    @staticmethod
    def FillCustomerList():
        myCursor = Customer.myCon.cursor()
        strQuery = "select * from Customer"
        rowAffected = myCursor.execute(strQuery)

        Customer.cusList.clear()
        for row in myCursor.fetchall():
            cus = Customer()
            cus.id = row[0]
            cus.Name = row[1]
            cus.address = row[2]
            Customer.cusList.append(cus)


