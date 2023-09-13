import mysql.connector as m
import sys
from prettytable import PrettyTable as PT
def Menu():
    file = open('invoice.txt','a+')
    file.close()
    file = open('invoice.txt','r')
    x = file.read()
    file.close()
    fi = open("Notes.txt",'a+')
    fi.close()
    if len(x) == 0:
        i_name = input('Enter the Company Name :')
        file = open('invoice.txt','w')
        file.write(i_name)
        file.close()
    file = open("invoice.txt")
    k = file.read()
    j = " "
    for i in k:
        j = j+i
        j = j+" "
    while True:
        import sys
        import mysql.connector
        import prettytable
        print("\t!! WELCOME TO '"+j.upper()+"' DEPARTMENT !!")
        print("\t===========================================")
        print("\n\n")
        print("\t1. Managing Details")
        print("\t2. Staff details")
        print("\t3. Settings")
        print("\t4. Quit")
        inp = int(input("Enter your Choice :"))
        if inp == 1:
            while True:
                print("\t!! Welcome To Managing Room!!")
                print("\t=============================\n")
                print("\t1. Invoice Generator")
                print("\t2. Product Generator")
                print("\t3. Display Room")
                print("\t4. Search Room")
                print("\t5. Updation Room")
                print("\t6. Deletion Room")
                print("\t7. Exit")
                a = int(input("Enter your Choice :"))
                if a == 1:
                    while True:
                        print("SUB INVOICE MENU")
                        print("================")
                        print("\n")
                        print("\t1. Create Invoice")
                        print("\t2. View all Invoices Created")
                        print("\t3. Back to Menu")
                        b = int(input("Enter your Choice :"))
                        if b == 1:
                            def invoice():
                                try:
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root')
                                    cur = con.cursor()
                                    db = 'create database if not exists invoices'
                                    cur.execute(db)
                                    use = 'use invoices'
                                    cur.execute(use)
                                    tb = 'create table if not exists invoice(I_id int(10) primary key,Customer_Name varchar(200),Item varchar(100),Price int(50),Quantity int(10),Total int(200))'
                                    cur.execute(tb)
                                    I_id = int(input("\tEnter Invoice id :"))
                                    Customer_Name = input("\tEnter Customer Name :")
                                    Item = input("\tEnter item name :")
                                    Price = int(input("\tEnter item Price :"))
                                    Quantity = int(input("\tEnter Quantity bought by customer:"))
                                    Total = int(Price*Quantity)
                                    rec = (I_id,Customer_Name,Item,Price,Quantity,Total)
                                    insert = "insert into invoice values(%s,%s,%s,%s,%s,%s)"
                                    cur.execute(insert,rec)
                                    con.commit()
                                    print("Invoice created Sucessfully :-)")
                                    cur.close()
                                    con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            invoice()
                        elif b == 2:
                            def view():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                cur.execute("select * from invoice")
                                a = cur.fetchall()
                                if cur.rowcount == 0:
                                   sys.stderr.write('No Invoice Created Yet')
                                else:
                                   from prettytable import PrettyTable as PT
                                   x = PT()
                                   b=['I_id','Customer_Name','Items','Price','Quantity','Total']
                                   x.field_names = b
                                   for i in a:
                                       x.add_row(i)
                                   print(x)
                                   con.commit()
                                   cur.close()
                                   con.close()
                            view()
                        elif b == 3:
                            break
                        else:
                            sys.stderr.write("Wrong choice......Enter again....")
                elif a == 2:
                    while True:
                        print("SUB PRODUCT MENU")
                        print("================")
                        print("\n")
                        print("\t1. Add a product")
                        print("\t2. View Products")
                        print("\t3. Back To Menu")
                        b = int(input("Enter your Choice :"))
                        if b == 1:
                            def add():
                                try:
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    tb = 'create table if not exists product(P_id int(10) primary key,P_Name varchar(200),Price int(50),Stock int(10))'
                                    cur.execute(tb)
                                    P_id = int(input("\tEnter Product id :"))
                                    P_Name = input("\tEnter Product Name :")
                                    Price = int(input("\tEnter Item Price :"))
                                    Stock = int(input("\tEnter Quantity :"))
                                    rec = (P_id,P_Name,Price,Stock)
                                    insert = "insert into product values(%s,%s,%s,%s)"
                                    cur.execute(insert,rec)
                                    con.commit()
                                    print("Product Added Sucessfully :-)")
                                    cur.close()
                                    con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            add()
                        elif b == 2:
                            def view_p():
                                try:
                                    import sys
                                    import mysql.connector as m
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    pro = 'select * from product'
                                    cur.execute(pro)
                                    a = cur.fetchall()
                                    if cur.rowcount == 0:
                                        sys.stderr.write("No Product Added yet")
                                    else:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['P_id','P_Name','Price','Stock']
                                        x.field_names = b
                                        for i in a:
                                            x.add_row(i)
                                        print(x)
                                        con.commit()
                                        cur.close()
                                        con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            view_p()
                        elif b == 3:
                            break
                        else:
                            sys.stderr.write("Wrong choice......Enter again....")
                elif a == 3:
                    while True:
                        print("SUB DISPLAY MENU")
                        print("================")
                        print("\n")
                        print("\t1. View all Invoices in")
                        print("\t2. View all Products in")
                        print("\t3. Back To Menu")
                        b = int(input("Enter your Choice :"))
                        if b == 1:
                            while True:
                                print("SUB DISPLAY-INVOICE MENU")
                                print("========================")
                                print("\n")
                                print("\t1. View Invoices in Asc order of their id")
                                print("\t2. View Invoices in Desc order of their id")
                                print("\t3. View Invoices in Asc order of their Customer Name")
                                print("\t4. View Invoices in Desc order of their Customer Name")
                                print("\t5. View Invoices in Asc order of their Item")
                                print("\t6. View Invoices in Desc order of their Item")
                                print("\t7. View Invoices in Asc order of their Price")
                                print("\t8. View Invoices in Desc order of their Price")
                                print("\t9. View Invoices in Asc order of their Quantity")
                                print("\t10. View Invoices in Desc order of their Quantity")
                                print("\t11. Back to Menu")
                                inp = int(input("Enter your Choice :"))
                                if inp == 1:
                                    def id_asc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from invoice order by I_id"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Invoice Created Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['I_id','Customer_Name','Items','Price','Quantity','Total']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    id_asc()
                                elif inp == 2:
                                    def id_desc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from invoice order by I_id desc"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Invoice Created Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['I_id','Customer_Name','Items','Price','Quantity','Total']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    id_desc()
                                elif inp == 3:
                                    def C_asc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from invoice order by Customer_Name"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Invoice Created Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['I_id','Customer_Name','Items','Price','Quantity','Total']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    C_asc()
                                elif inp == 4:
                                    def C_desc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from invoice order by Customer_Name desc"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Invoice Created Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['I_id','Customer_Name','Items','Price','Quantity','Total']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    C_desc()
                                elif inp == 5:
                                    def item_asc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from invoice order by Item"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Invoice Created Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['I_id','Customer_Name','Items','Price','Quantity','Total']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    item_asc()
                                elif inp == 6:
                                    def item_desc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from invoice order by Item desc"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Invoice Created Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['I_id','Customer_Name','Items','Price','Quantity','Total']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    item_desc()
                                elif inp == 7:
                                    def Price_asc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from invoice order by Price"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Invoice Created Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['I_id','Customer_Name','Items','Price','Quantity','Total']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    Price_asc()
                                elif inp == 8:
                                    def Price_desc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from invoice order by Price desc"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Invoice Created Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['I_id','Customer_Name','Items','Price','Quantity','Total']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    Price_desc()

                                elif inp == 9:
                                    def Qty_asc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from invoice order by Quantity"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Invoice Created Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['I_id','Customer_Name','Items','Price','Quantity','Total']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    Qty_asc()
                                elif inp == 10:
                                    def Qty_desc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from invoice order by Quantity desc"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Invoice Created Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['I_id','Customer_Name','Items','Price','Quantity','Total']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    Qty_desc()
                                elif inp == 11:
                                    break
                                else:
                                    print("Wrong Choice...Enter Again....")
                        elif b == 2:
                            while True:
                                print("SUB DISPLAY-PRODUCT MENU")
                                print("========================")
                                print("\n")
                                print("\t1. View Products in Asc order of their id")
                                print("\t2. View Products in Desc order of their id")
                                print("\t3. View Products in Asc order of their Product Name")
                                print("\t4. View Products in Desc order of their Product Name")
                                print("\t5. View Products in Asc order of their Price")
                                print("\t6. View Products in Desc order of their Price")
                                print("\t7. View Products in Asc order of their Stock")
                                print("\t8. View Products in Desc order of their Stock")
                                print("\t9. Back to Menu")
                                inp = int(input("Enter your Choice"))
                                if inp == 1:
                                    def id_asc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from product order by P_id"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Product Added Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['P_id','P_Name','Price','Stock']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    id_asc()
                                elif inp == 2:
                                    def id_desc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from product order by P_id desc"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Product Added Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['P_id','P_Name','Price','Stock']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    id_desc()
                                    
                                elif inp == 3:
                                    def n_asc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from product order by P_Name"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Product Added Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['P_id','P_Name','Price','Stock']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    n_asc()
                                elif inp == 4:
                                    def n_desc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from product order by P_Name desc"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Product Added Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['P_id','P_Name','Price','Stock']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    n_desc()
                                elif inp == 5:
                                    def price_asc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from product order by Price"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Product Added Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['P_id','P_Name','Price','Stock']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    price_asc()
                                elif inp == 6:
                                    def price_desc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from product order by Price desc"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Product Added Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['P_id','P_Name','Price','Stock']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    price_desc()
                                elif inp == 7:
                                    def s_asc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from product order by Stock"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Product Added Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['P_id','P_Name','Price','Stock']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    s_asc()
                                elif inp == 8:
                                    def s_desc():
                                        try:
                                            import mysql.connector as m
                                            import sys
                                            con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                            cur = con.cursor()
                                            y = "select * from product order by Stock desc"
                                            cur.execute(y)
                                            a = cur.fetchall()
                                            if cur.rowcount == 0:
                                                sys.stderr.write('No Product Added Yet')
                                            else:
                                                from prettytable import PrettyTable as PT
                                                x = PT()
                                                b=['P_id','P_Name','Price','Stock']
                                                x.field_names = b
                                                for i in a:
                                                    x.add_row(i)
                                                print(x)
                                                con.commit()
                                                cur.close()
                                                con.close()
                                        except:
                                            sys.stderr.write("Some Error Occured\n")
                                    s_desc()
                                elif inp == 9:
                                    break
                                else:
                                    print("Wrong Choice...Enter Again")
                        elif b == 3:
                            break
                        else:
                            sys.stderr.write("Wrong Choice...Enter Again")
                elif a == 4:
                    while True:
                        print("\tSUB SEARCH ROOM")
                        print("\t===============")
                        print("\n")
                        print("\t1. To Search in Invoices")
                        print("\t2. To Search in Products")
                        print("\t3. Back To Menu")
                        inp = int(input("Enter your choice :"))
                        if inp == 1:
                            while True:
                                print('\n')
                                print("\t1. To search by invoice id")
                                print("\t2. To search by Customer name")
                                print("\t3. To search by item name")
                                print("\t4. To search by item Price")
                                print("\t5. Back to Menu")
                                a = int(input("Enter your Choice :"))
                                if a == 1:
                                    def S_I_id():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        i_id = input("Enter Invoice id you want to search :")
                                        s = "select * from invoice where I_id = '"+i_id+"'"
                                        cur.execute(s)
                                        t=cur.fetchall()
                                        if cur.rowcount != 0:
                                            from prettytable import PrettyTable as PT
                                            x = PT()
                                            b=['Invoice_id','Customer_name','Item','Price','Quantity','Total']
                                            x.field_names = b    
                                            for i in t:
                                                x.add_row(i)
                                            print(x)
                                            cur.close()
                                            con.close()
                                        else:
                                            sys.stderr.write("\nNo Such Invoice Exists...\n")
                                    S_I_id()
                                elif a == 2:
                                    def S_I_Cname():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        c_name = input("Enter Customer Name you want to search :")
                                        try:   
                                            s = "select * from invoice where Customer_Name = '"+c_name+"'"
                                            from prettytable import PrettyTable as PT 
                                            x = PT()
                                            cur.execute(s)
                                            t=cur.fetchall()
                                            if cur.rowcount != 0:
                                                b=['Invoice_id','Customer_name','Item','Price','Quantity','Total']
                                                x.field_names = b
                                                for i in t:
                                                    x.add_row(i)
                                                print(x)
                                            else:
                                                sys.stderr.write("\nNo Such Invoice Exists...\n")
                                        except:
                                            sys.stderr.write("\nSome Error Occured...\n")
                                    S_I_Cname()
                                elif a == 3:
                                    def S_Item():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        item = input("Enter Product Name you want to search :")
                                        try:   
                                            s = "select * from invoice where Item = '"+item+"'"
                                            from prettytable import PrettyTable as PT #prettytable module is for creating table
                                            x = PT()
                                            cur.execute(s)
                                            t=cur.fetchall()
                                            if cur.rowcount != 0:
                                                b=['Invoice_id','Customer_name','Item','Price','Quantity','Total']
                                                x.field_names = b
                                                for i in t:
                                                    x.add_row(i)
                                                print(x)
                                            else:
                                                sys.stderr.write("\nNo Such Invoice Exists...\n")
                                        except:
                                            sys.stderr.write("\nSome Error Occured...\n")
                                    S_Item()
                                elif a == 4:
                                    def S_Price():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        price = input("Enter Product Name you want to search :")
                                        try:   
                                            s = "select * from invoice where Price = '"+price+"'"
                                            from prettytable import PrettyTable as PT #prettytable module is for creating table
                                            x = PT()
                                            cur.execute(s)
                                            t=cur.fetchall()
                                            if cur.rowcount != 0:
                                                b=['Invoice_id','Customer_name','Item','Price','Quantity','Total']
                                                x.field_names = b
                                                for i in t:
                                                    x.add_row(i)
                                                print(x)
                                            else:
                                                sys.stderr.write("\nNo Such Invoice Exists...\n")   
                                        except:
                                            sys.stderr.write("\nSome Error Occured...\n")
                                    S_Price()
                                elif a == 5:
                                    break
                                else:
                                    sys.stderr.write("Wrong Choice... Enter Again...\n")
                        elif inp == 2:
                            while True:
                                print('\t1. To search by Product id')
                                print('\t2. To search by Product name')
                                print('\t3. To search by Product Price')
                                print('\t4. To search by Product Stock')
                                print('\t5. Back to Menu')
                                a = int(input("Enter your Choice :"))
                                if a == 1:
                                    def S_P_id():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        try:
                                            p_id = input("Enter Product id you want to search :")
                                            s = "select * from product where P_id = '"+p_id+"'"
                                            from prettytable import PrettyTable as PT #prettytable module is for creating table
                                            x = PT()
                                            cur.execute(s)
                                            t=cur.fetchall()
                                            if cur.rowcount != 0:
                                                b=['P_id','P_name','Price','Stock']
                                                x.field_names = b                                            
                                                for i in t:
                                                    x.add_row(i)
                                                print(x)
                                            else:
                                                sys.stderr.write("\nNo Such Product Exists...\n")
                                        except:
                                            sys.stderr.write("\nSome Error Occured...\n")
                                    S_P_id()
                                elif a == 2:
                                    def S_P_name():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        p_name = input("Enter Product Name you want to search :")
                                        try:   
                                            s = "select * from product where P_Name = '"+p_name+"'"
                                            from prettytable import PrettyTable as PT #prettytable module is for creating table
                                            x = PT()
                                            cur.execute(s)
                                            t=cur.fetchall()
                                            if cur.rowcount != 0:
                                                b=['P_id','P_name','Price','Stock']
                                                x.field_names = b
                                                for i in t:
                                                    x.add_row(i)
                                                print(x)
                                            else:
                                                sys.stderr.write("\nNo Such Product Exists...\n")
                                        except:
                                            sys.stderr.write("\nSome Error Occured...\n")
                                    S_P_name()
                                elif a == 3:
                                    def S_Price():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        price = input("Enter Product Price you want to search :")
                                        try:   
                                            s = "select * from product where Price = '"+price+"'"
                                            from prettytable import PrettyTable as PT #prettytable module is for creating table
                                            x = PT()
                                            cur.execute(s)
                                            t=cur.fetchall()
                                            if cur.rowcount != 0:
                                                b=['P_id','P_name','Price','Stock']
                                                x.field_names = b
                                                for i in t:
                                                    x.add_row(i)
                                                print(x)
                                            else:
                                                sys.stderr.write("\nNo Such Product Exists...\n")
                                        except:
                                            sys.stderr.write("\nSome Error Occured...\n")
                                    S_Price()
                                elif a == 4:
                                    def S_Stock():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        stock = input("Enter Product Name you want to search :")
                                        try:   
                                            s = "select * from product where Stock = '"+stock+"'"
                                            from prettytable import PrettyTable as PT #prettytable module is for creating table
                                            x = PT()
                                            cur.execute(s)
                                            t=cur.fetchall()
                                            if cur.rowcount != 0:
                                                b=['P_id','P_name','Price','Stock']
                                                x.field_names = b
                                                for i in t:
                                                    x.add_row(i)
                                                print(x)
                                            else:
                                                sys.stderr.write("\nNo Such Product Exists...\n")
                                        except:
                                            sys.stderr.write("\nSome Error Occured...")
                                    S_Stock()
                                elif a == 5:
                                    break
                                else:
                                    sys.stderr.write("Wrong Choice... Enter Again...\n")
                        elif inp == 3:
                            break
                        else:
                            sys.stderr.write("Wrong Choice... Enter Again...\n")
                elif a ==  5:
                    while True:
                        print("\tSUB UPDATE ROOM")
                        print("\t===============")
                        print("\n")
                        print("\t1. To Update Invoices")
                        print("\t2. To Update Products")
                        print("\t3. Back To Menu")
                        inp = int(input("Enter your choice :"))
                        if inp == 1:
                            while True:
                                print("\t1. To update invoice id")
                                print("\t2. To update Customer name")
                                print("\t3. To update item name")
                                print("\t4. To update item Price")
                                print("\t5. Back to Menu")
                                a = int(input("Enter your Choice :"))
                                if a == 1:
                                    def U_I_id():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        cur.execute("select * from invoice")
                                        t = cur.fetchall()
                                        if cur.rowcount != 0:
                                            from prettytable import PrettyTable as PT
                                            x = PT()
                                            b=['Invoice_id','Customer_name','Item','Price','Quantity','Total']
                                            x.field_names = b    
                                            for i in t:
                                                x.add_row(i)
                                            print(x)
                                            i_id = input("Enter Invoice id you want to update :")
                                            n_id = input("Enter New Invoice id you want to enter :")
                                            s = "update invoice set I_id = '"+n_id+"' where I_id = '"+i_id+"'"
                                            cur.execute(s)
                                            print("Invoice Updated Sucessfully..")
                                            con.commit()
                                            cur.close()
                                            con.close()
                                        else:
                                            sys.stderr.write("\nNo Such Invoice Exists...\n")
                                    U_I_id()
                                elif a == 2:
                                    def U_I_Cname():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        cur.execute("select * from invoice")
                                        t = cur.fetchall()
                                        if cur.rowcount != 0:
                                            from prettytable import PrettyTable as PT
                                            x = PT()
                                            b=['Invoice_id','Customer_name','Item','Price','Quantity','Total']
                                            x.field_names = b    
                                            for i in t:
                                                x.add_row(i)
                                            print(x)
                                            c_name = input("Enter Customer Name you want to update :")
                                            n_name = input("Enter New Customer Name you want to enter :")
                                            s = "update invoice set Customer_Name = '"+n_name+"' where Customer_Name = '"+c_name+"'"
                                            cur.execute(s)
                                            con.commit()
                                            print("Invoice Updated Sucessfully")
                                            cur.close()
                                            con.close()
                                        else:
                                            sys.stderr.write("\nNo Such Invoice Exists...\n")
                                    U_I_Cname()
                                elif a == 3:
                                    def U_Item():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        cur.execute("select * from invoice")
                                        t = cur.fetchall()
                                        if cur.rowcount != 0:
                                            from prettytable import PrettyTable as PT
                                            x = PT()
                                            b=['Invoice_id','Customer_name','Item','Price','Quantity','Total']
                                            x.field_names = b    
                                            for i in t:
                                                x.add_row(i)
                                            print(x)
                                            item = input("Enter New Item Name you want to enter :")
                                            n_item = input("Enter Item Name you want to update :")
                                            s = "update invoice set Item = '"+item+"' where Item = '"+n_item+"'"
                                            cur.execute(s)
                                            con.commit()
                                            print("Invoice Updated Sucessfully")
                                            cur.close()
                                            con.close()
                                        else:
                                            sys.stderr.write("\nNo Such Invoice Exists...\n")
                                    U_Item()
                                elif a == 4:
                                    def U_Price():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        cur.execute("select * from invoice")
                                        t = cur.fetchall()
                                        if cur.rowcount != 0:
                                            from prettytable import PrettyTable as PT
                                            x = PT()
                                            b=['Invoice_id','Customer_name','Item','Price','Quantity','Total']
                                            x.field_names = b    
                                            for i in t:
                                                x.add_row(i)
                                            print(x)
                                            i_id = input("Enter Invoice Id :")
                                            n_price = input("Enter New Price you want to enter :")
                                            s = "update invoice set Price = '"+n_price+"' where I_id = '"+i_id+"'"
                                            cur.execute(s)
                                            u = "select * from invoice where I_id = '"+i_id+"'"
                                            cur.execute(u)
                                            y = cur.fetchone()
                                            if cur.rowcount != 0:
                                                if y[4]>0:
                                                    total = str(int(n_price)*int(y[4]))
                                                    z = "update invoice set Total = '"+total+"' where I_id = '"+i_id+"'"
                                                    cur.execute(z)
                                                    con.commit()
                                                else:
                                                    return -1
                                            print("Invoice Updated Sucessfully")
                                            con.commit()
                                            cur.close()
                                            con.close()
                                        else:
                                            sys.stderr.write("\nNo Such Invoice Exists...\n")
                                    U_Price()
                                elif a == 5:
                                    break
                                else:
                                    sys.stderr.write("Wrong Choice... Enter Again...\n")
                        elif inp == 2:
                            while True:
                                print('\t1. To Update by Product id')
                                print('\t2. To Update by Product name')
                                print('\t3. To Update by Product Price')
                                print('\t4. To Update by Product Stock')
                                print('\t5. Back to Menu')
                                a = int(input("Enter your Choice :"))
                                if a == 1:
                                    def U_P_id():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        cur.execute("select * from product")
                                        t = cur.fetchall()
                                        if cur.rowcount != 0:
                                            from prettytable import PrettyTable as PT
                                            x = PT()
                                            b=['P_id','P_name','Price','Stock']
                                            x.field_names = b    
                                            for i in t:
                                                x.add_row(i)
                                            print(x)
                                            p_id = input("Enter Product id you want to update :")
                                            n_id = input("Enter New Product id you want to update :")
                                            s = "update product set P_id = '"+n_id+"' where P_id = '"+p_id+"'"
                                            cur.execute(s)
                                            print("Product Updated Sucessfully")
                                            con.commit()
                                            cur.close()
                                            con.close()
                                        else:
                                            sys.stderr.write("\nNo Such Product Exists...\n")
                                    U_P_id()
                                elif a == 2:
                                    def U_P_name():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        cur.execute("select * from product")
                                        t = cur.fetchall()
                                        if cur.rowcount != 0:
                                            from prettytable import PrettyTable as PT
                                            x = PT()
                                            b=['P_id','P_name','Price','Stock']
                                            x.field_names = b    
                                            for i in t:
                                                x.add_row(i)
                                            print(x)
                                            p_name = input("Enter Product Name you want to update :")
                                            n_name = input("Enter New Product Name you want to update :")
                                            s = "update product set P_Name = '"+n_name+"' where P_Name = '"+p_name+"'"
                                            cur.execute(s)
                                            print("Product Updated Sucessfully")
                                            con.commit()
                                            cur.close()
                                            con.close()
                                        else:
                                            sys.stderr.write("\nNo Such Product Exists...\n")
                                    U_P_name()
                                elif a == 3:
                                    def U_Price():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        cur.execute("select * from product")
                                        t = cur.fetchall()
                                        if cur.rowcount != 0:
                                            from prettytable import PrettyTable as PT
                                            x = PT()
                                            b=['P_id','P_name','Price','Stock']
                                            x.field_names = b    
                                            for i in t:
                                                x.add_row(i)
                                            print(x)
                                            p_id = input("Enter Product Id you want to update :")
                                            n_price = input("Enter New Product Price you want to update :")
                                            s = "update product set Price = '"+n_price+"' where P_id = '"+p_id+"'"
                                            cur.execute(s)
                                            print("Product Updated Sucessfully")
                                            con.commit()
                                            cur.close()
                                            con.close()
                                        else:
                                            sys.stderr.write("\nNo Such Product Exists...\n")
                                    U_Price()
                                elif a == 4:
                                    def U_Stock():
                                        import mysql.connector as m
                                        import sys
                                        con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                        cur = con.cursor()
                                        cur.execute("select * from product")
                                        t = cur.fetchall()
                                        if cur.rowcount != 0:
                                            from prettytable import PrettyTable as PT
                                            x = PT()
                                            b=['P_id','P_name','Price','Stock']
                                            x.field_names = b    
                                            for i in t:
                                                x.add_row(i)
                                            print(x)
                                            p_stock = input("Enter Product id you want to update :")
                                            n_stock = input("Enter New Product Stock you want to update :")
                                            s = "update product set Stock = '"+n_stock+"' where P_id = '"+p_stock+"'"
                                            cur.execute(s)
                                            print("Product Updated Sucessfully")
                                            con.commit()
                                            cur.close()
                                            con.close()
                                        else:
                                            sys.stderr.write("\nNo Such Product Exists...\n")
                                    U_Stock()
                                elif a == 5:
                                    break
                                else:
                                    sys.stderr.write("Wrong Choice... Enter Again...\n")
                        elif inp == 3:
                            break
                        else:
                            sys.stderr.write("Wrong Choice... Enter Again...\n")
                elif a == 6:
                    while True:
                        print("\tSUB DELETE ROOM")
                        print("\t===============")
                        print("\n")
                        print("\t1. To Delete Invoice")
                        print("\t2. To Delete Product")
                        print("\t3. Back To Menu")
                        inp = int(input("Enter Your Choice :"))
                        if inp == 1:
                            print("\t1. To Delete Invoice by Id")
                            print("\t2. To Delete Invoice by Customer Name")
                            print("\t3. To Delete Invoice by Item")
                            print("\t4. Back To Menu")
                            a = int(input("Enter Your Choice :"))
                            if a == 1:
                                def D_id():
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from invoice")
                                    t = cur.fetchall()
                                    if cur.rowcount != 0:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['Invoice_id','Customer_name','Item','Price','Quantity','Total']
                                        x.field_names = b    
                                        for i in t:
                                            x.add_row(i)
                                        print(x) 
                                        i_id = input("Enter Invoice id you want to delete :")
                                        s = "delete from invoice where I_id = '"+i_id+"'"
                                        cur.execute(s)
                                        print("Invoice Deleted Sucessfully..")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("\nNo Such Invoice Exists...\n")
                                D_id()
                            elif a == 2:
                                def D_Cname():
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from invoice")
                                    t = cur.fetchall()
                                    if cur.rowcount != 0:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['Invoice_id','Customer_name','Item','Price','Quantity','Total']
                                        x.field_names = b    
                                        for i in t:
                                            x.add_row(i)
                                        print(x)
                                        C_name = input("Enter Customer Name you want to delete :")
                                        s = "delete from invoice where Customer_Name = '"+C_name+"'"
                                        cur.execute(s)
                                        print("Invoice Deleted Sucessfully..")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("\nNo Such Invoice Exists...\n")
                                D_Cname()
                            elif a == 3:
                                def D_item():
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from invoice")
                                    t = cur.fetchall()
                                    if cur.rowcount != 0:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['Invoice_id','Customer_name','Item','Price','Quantity','Total']
                                        x.field_names = b    
                                        for i in t:
                                            x.add_row(i)
                                        print(x)
                                        i_item = input("Enter Item you want to delete :")
                                        s = "delete from invoice where Item = '"+i_item+"'"
                                        cur.execute(s)
                                        print("Invoice Deleted Sucessfully..")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("\nNo Such Invoice Exists...\n")
                                D_item()
                            elif a == 4:
                                break
                            else:
                                sys.stderr.write("Wrong Choice...Enter Again....\n")
                        elif inp == 2:
                            print("\t1. To Delete Product by Id")
                            print("\t2. To Delete Product by Product Name")
                            print("\t3. To Delete Product by Price")
                            print("\t4. Back To Menu")
                            a = int(input("Enter Your Choice :"))
                            if a == 1:
                                def D_id():
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from product")
                                    t = cur.fetchall()
                                    if cur.rowcount != 0:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['Product_id','Product_name','Price','Stock']
                                        x.field_names = b    
                                        for i in t:
                                            x.add_row(i)
                                        print(x)
                                        i_id = input("Enter Product id you want to delete :")
                                        s = "delete from product where P_id = '"+i_id+"'"
                                        cur.execute(s)
                                        print("Product Deleted Sucessfully..")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("\nNo Such Product Exists...\n")
                                D_id()
                            elif a == 2:
                                def D_Pname():
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from product")
                                    t = cur.fetchall()
                                    if cur.rowcount != 0:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b = ['Product_id','Product_name','Price','Stock']
                                        x.field_names = b    
                                        for i in t:
                                            x.add_row(i)
                                        print(x)
                                        C_name = input("Enter Product Name you want to delete :")
                                        s = "delete from product where P_Name = '"+C_name+"'"
                                        cur.execute(s)
                                        print("Product Deleted Sucessfully..")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("\nNo Such Product Exists...\n")
                                D_Pname()
                            elif a == 3:
                                def D_item():
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from product")
                                    t = cur.fetchall()
                                    if cur.rowcount != 0:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b = ['Product_id','Product_name','Price','Stock']
                                        x.field_names = b    
                                        for i in t:
                                            x.add_row(i)
                                        print(x)
                                        i_item = input("Enter Product Price you want to delete :")
                                        s = "delete from product where Price = '"+i_item+"'"
                                        cur.execute(s)
                                        print("Product Deleted Sucessfully..")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("\nNo Such Product Exists...\n")
                                D_item()
                            elif a == 4:
                                break
                            else:

                                sys.stderr.write("Wrong Choice...Enter Again....\n")
                        elif inp == 3:
                            break
                        else:
                            sys.stderr.write("Wrong Choice...Enter Again....\n")
                elif a == 7:
                    break
                else:
                    sys.stderr.write("Wrong Choice...Enter Again....\n")
        elif inp == 2:
            while True:
                print("\t\t!! Welcome To Staff Room !!")
                print("\t\t===========================")
                print("\t1. Add Staff")
                print("\t2. View Staff")
                print("\t3. Search Staff")
                print("\t4. Update Staff")
                print("\t5. Remove Staff")
                print("\t6. Go back to Menu")
                inp = int(input("Enter Your Choice :"))
                if inp == 1:
                    def staff():
                        import mysql.connector as m
                        import sys
                        con = m.connect(host='localhost',user='root',password='root')
                        cur = con.cursor()
                        db = 'create database if not exists invoices'
                        cur.execute(db)
                        use = 'use invoices'
                        cur.execute(use)
                        tb = 'create table if not exists staff(S_id int(10) primary key,S_Name varchar(200),Department varchar(100),Salary int(50),Experience varchar(20))'
                        cur.execute(tb)
                        try:
                            S_id = int(input("\tEnter Staff id :"))
                            S_Name = input("\tEnter Staff Name :")
                            Department = input("\tEnter Type of Work Assigned to Staff :")
                            Salary = int(input("\tEnter Staff Salary :"))
                            Experience = int(input("\tEnter Experience of the Staff :"))
                            rec = (S_id,S_Name,Department,Salary,Experience)
                            insert = "insert into staff values(%s,%s,%s,%s,%s)"
                            cur.execute(insert,rec)
                            con.commit()
                            print("Staff Added Sucessfully :-)")
                            cur.close()
                            con.close()
                        except:
                            sys.stderr.write("Some Error Occured...\n")
                    staff()
                elif inp == 2:
                    while True:
                        print("\t1. View All Staff")
                        print("\t2. View All Staff in Ascending order of their Id")
                        print("\t3. View All Staff in Descending order of their Id")
                        print("\t4. View All Staff in Ascending order of their Name")
                        print("\t5. View All Staff in Descending order of their Name")
                        print("\t6. View All Staff in Ascending order of their Department")
                        print("\t7. View All Staff in Descending order of their Department")
                        print("\t8. View All Staff in Ascending order of their Salary")
                        print("\t9. View All Staff in Descending order of their Salary")
                        print("\t10. View All Staff in Ascending order of their Experience")
                        print("\t11. View All Staff in Descending order of their Experience")
                        print("\t12. Go Back to Menu")
                        a = int(input("Enter Your Choice :"))
                        if a == 1:    
                            def view():
                                try:
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from staff")
                                    a = cur.fetchall()
                                    if cur.rowcount == 0:
                                        sys.stderr.write('No Staff Added Yet\n')
                                    else:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in a:
                                            x.add_row(i)
                                        print(x)
                                        con.commit()
                                        cur.close()
                                        con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            view()
                        elif a == 2:
                            def v_asc_id():
                                try:
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from staff order by S_id")
                                    a = cur.fetchall()
                                    if cur.rowcount == 0:
                                        sys.stderr.write('No Staff Added Yet\n')
                                    else:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in a:
                                            x.add_row(i)
                                        print(x)
                                        con.commit()
                                        cur.close()
                                        con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            v_asc_id()
                        elif a == 3:
                            def v_desc_id():
                                try:
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from staff order by S_id desc")
                                    a = cur.fetchall()
                                    if cur.rowcount == 0:
                                        sys.stderr.write('No Staff Added Yet\n')
                                    else:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in a:
                                            x.add_row(i)
                                        print(x)
                                        con.commit()
                                        cur.close()
                                        con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            v_desc_id()
                        elif a == 4:
                            def v_asc_name():
                                try:
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from staff order by S_Name")
                                    a = cur.fetchall()
                                    if cur.rowcount == 0:
                                        sys.stderr.write('No Staff Added Yet\n')
                                    else:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in a:
                                            x.add_row(i)
                                        print(x)
                                        con.commit()
                                        cur.close()
                                        con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            v_asc_name()
                        elif a == 5:
                            def v_desc_name():
                                try:
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from staff order by S_Name desc")
                                    a = cur.fetchall()
                                    if cur.rowcount == 0:
                                        sys.stderr.write('No Staff Added Yet\n')
                                    else:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in a:
                                            x.add_row(i)
                                        print(x)
                                        con.commit()
                                        cur.close()
                                        con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            v_desc_name()
                        elif a == 6:
                            def v_asc_D():
                                try:
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from staff order by Department")
                                    a = cur.fetchall()
                                    if cur.rowcount == 0:
                                        sys.stderr.write('No Staff Added Yet\n')
                                    else:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in a:
                                            x.add_row(i)
                                        print(x)
                                        con.commit()
                                        cur.close()
                                        con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            v_asc_D()
                        elif a == 7:
                            def v_desc_D():
                                try:
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from staff order by Department desc")
                                    a = cur.fetchall()
                                    if cur.rowcount == 0:
                                        sys.stderr.write('No Staff Added Yet\n')
                                    else:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in a:
                                            x.add_row(i)
                                        print(x)
                                        con.commit()
                                        cur.close()
                                        con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            v_desc_D()
                        elif a == 8:
                            def v_asc_S():
                                try:
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from staff order by Salary")
                                    a = cur.fetchall()
                                    if cur.rowcount == 0:
                                        sys.stderr.write('No Staff Added Yet\n')
                                    else:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in a:
                                            x.add_row(i)
                                        print(x)
                                        con.commit()
                                        cur.close()
                                        con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            v_asc_S()
                        elif a == 9:
                            def v_desc_S():
                                try:
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from staff order by Salary desc")
                                    a = cur.fetchall()
                                    if cur.rowcount == 0:
                                        sys.stderr.write('No Staff Added Yet\n')
                                    else:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in a:
                                            x.add_row(i)
                                        print(x)
                                        con.commit()
                                        cur.close()
                                        con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            v_desc_S()
                        elif a == 10:
                            def v_asc_E():
                                try:
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from staff order by Experience")
                                    a = cur.fetchall()
                                    if cur.rowcount == 0:
                                        sys.stderr.write('No Staff Added Yet\n')
                                    else:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in a:
                                            x.add_row(i)
                                        print(x)
                                        con.commit()
                                        cur.close()
                                        con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            v_asc_E()
                        elif a == 11:
                            def v_desc_E():
                                try:
                                    import mysql.connector as m 
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    cur.execute("select * from staff order by Experience desc")
                                    a = cur.fetchall()
                                    if cur.rowcount == 0:
                                        sys.stderr.write('No Staff Added Yet\n')
                                    else:
                                        from prettytable import PrettyTable as PT
                                        x = PT()
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in a:
                                            x.add_row(i)
                                        print(x)
                                        con.commit()
                                        cur.close()
                                        con.close()
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            v_desc_E()
                        elif a == 12:
                            break
                        else:
                            sys.stderr.write("Wrong Choice...Enter Again...")
                elif inp == 3:
                    while True:
                        print("\t1. Search by Staff Id")
                        print("\t2. Search by Staff Name")
                        print("\t3. Search by Staff Department")
                        print("\t4. Search by Staff Salary")
                        print("\t5. Search by Staff Experience")
                        print("\t6. Back To Menu")
                        a = int(input("Enter Your Choice :"))
                        if a == 1:
                            def S_S_id():
                                    import mysql.connector as m
                                    import sys
                                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                    cur = con.cursor()
                                    s_id = input("Enter Staff Id you want to search :")
                                    try:   
                                        s = "select * from staff where S_id = '"+s_id+"'"
                                        from prettytable import PrettyTable as PT 
                                        x = PT()
                                        cur.execute(s)
                                        t=cur.fetchall()
                                        if cur.rowcount != 0:
                                            b=['S_id','S_Name','Department','Salary','Experience']
                                            x.field_names = b
                                            for i in t:
                                                x.add_row(i)
                                            print(x)
                                        else:
                                            sys.stderr.write("No Such Staff Exists...\n")
                                    except:
                                        sys.stderr.write("Some Error Occured...\n")
                            S_S_id()
                        elif a == 2:
                            def S_S_name():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                s_name = input("Enter Staff Name you want to search :")
                                try:   
                                    s = "select * from staff where S_Name = '"+s_name+"'"
                                    from prettytable import PrettyTable as PT 
                                    x = PT()
                                    cur.execute(s)
                                    t=cur.fetchall()
                                    if cur.rowcount != 0:
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in t:
                                            x.add_row(i)
                                        print(x)
                                    else:
                                        sys.stderr.write("No Such Staff Exists...\n")
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            S_S_name()
                        elif a == 3:
                            def S_S_D():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                d = input("Enter Staff Department you want to search :")
                                try:   
                                    s = "select * from staff where Department = '"+d+"'"
                                    from prettytable import PrettyTable as PT 
                                    x = PT()
                                    cur.execute(s)
                                    t=cur.fetchall()
                                    if cur.rowcount != 0:
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in t:
                                            x.add_row(i)
                                        print(x)
                                    else:
                                        sys.stderr.write("No Such Staff Exists...\n")
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            S_S_D()
                        elif a == 4:
                            def S_S_S():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                s = input("Enter Staff Salary you want to search :")
                                try:   
                                    s = "select * from staff where Salary = '"+s+"'"
                                    from prettytable import PrettyTable as PT 
                                    x = PT()
                                    cur.execute(s)
                                    t=cur.fetchall()
                                    if cur.rowcount != 0:
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in t:
                                            x.add_row(i)
                                        print(x)
                                    else:
                                        sys.stderr.write("No Such Staff Exists...\n")
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            S_S_S()
                        elif a == 5:
                            def S_S_E():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                e = input("Enter Staff Experience you want to search :")
                                try:   
                                    s = "select * from staff where Experience = '"+e+"'"
                                    from prettytable import PrettyTable as PT
                                    x = PT()
                                    cur.execute(s)
                                    t=cur.fetchall()
                                    if cur.rowcount != 0:
                                        b=['S_id','S_Name','Department','Salary','Experience']
                                        x.field_names = b
                                        for i in t:
                                            x.add_row(i)
                                        print(x)
                                    else:
                                        sys.stderr.write("No Such Staff Exists...\n")
                                except:
                                    sys.stderr.write("Some Error Occured...\n")
                            S_S_E()
                        elif a == 6:
                            break
                        else:
                            sys.stderr.write("Wrong Choice... Enter Again...\n")
                elif inp == 4:
                    while True:
                        print("\t1. Update by Staff Id")
                        print("\t2. Update by Staff Name")
                        print("\t3. Update by Staff Department")
                        print("\t4. Update by Staff Salary")
                        print("\t5. Update by Staff Experience")
                        print("\t6. Go Back to Menu")
                        a = int(input("Enter Yoyr Choice :"))
                        if a == 1:
                            def U_S_id():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                try:
                                    s_id = input("Enter Staff id you want to Update :")
                                    n_id = input("Enter New Staff id :")
                                    s = "update staff set S_id = '"+n_id+"' where S_id = '"+s_id+"'"
                                    cur.execute(s)
                                    if cur.rowcount != 0:
                                        print("Staff updated Sucessfully")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("No Such Staff Exists...\n")
                                except:
                                    sys.stderr.write("Wrong Choice...Enter Again...\n")
                            U_S_id()
                        elif a == 2:
                            def U_S_name():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                try:
                                    s_name = input("Enter Staff Name you want to Update :")
                                    n_name = input("Enter New Staff Name :")
                                    s = "update staff set S_Name = '"+n_name+"' where S_Name = '"+s_name+"'"
                                    cur.execute(s)
                                    if cur.rowcount != 0:
                                        print("Staff Updated Sucessfully")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("No Such Staff Exists...\n")
                                except:
                                    sys.stderr.write("Wrong Choice...Enter Again...\n")
                            U_S_name()
                        elif a == 3:
                            def U_S_D():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                try:
                                    d = input("Enter Staff Department you want to Update :")
                                    n_d = input("Enter New Staff Department :")
                                    s = "update staff set Department = '"+n_d+"' where Department = '"+d+"'"
                                    cur.execute(s)
                                    if cur.rowcount != 0:
                                        print("Staff Updated Sucessfully")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("No Such Staff Exists...\n")
                                except:
                                    sys.stderr.write("Wrong Choice...Enter Again...\n")
                            U_S_D()
                        elif a == 4:
                            def U_S_S():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                try:
                                    s = input("Enter Staff Salary you want to Update :")
                                    n_s = input("Enter New Staff Salary :")
                                    s = "update staff set Salary = '"+n_s+"' where Salary = '"+s+"'"
                                    cur.execute(s)
                                    if cur.rowcount != 0:
                                        print("Staff Updated Sucessfully")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("No Such Staff Exists...\n")
                                except:
                                    sys.stderr.write("Wrong Choice...Enter Again...\n")
                            U_S_S()
                        elif a == 5:
                            def U_S_E():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                try:
                                    e = input("Enter Staff Experience you want to Update :")
                                    n_e = input("Enter New Staff Experience :")
                                    s = "update staff set Experience = '"+n_e+"' where Experience = '"+e+"'"
                                    cur.execute(s)
                                    if cur.rowcount != 0:
                                        print("Staff Updated Sucessfully")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("No Such Staff Exists...\n")
                                except:
                                    sys.stderr.write("Wrong Choice...Enter Again...\n")
                            U_S_E()
                        elif a == 6:
                            break
                        else:
                            sys.stderr.write("Wrong Choice...Enter Again...\n")
                elif inp == 5:
                    while True:
                        print("\t1. Remove Staff by Staff Id")
                        print("\t2. Remove Staff by Staff Name")
                        print("\t3. Remove Staff by Staff Department")
                        print("\t4. Remove Staff by Staff Salary")
                        print("\t5. Remove Staff by Staff Experience")
                        print("\t6. Go Back To Menu")
                        a = int(input("Enter Your Choice :"))
                        if a == 1:
                            def D_S_id():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                try:
                                    id = input("Enter Staff Id you want to Remove :")
                                    s = "delete from staff where S_id = '"+id+"'"
                                    cur.execute(s)
                                    if cur.rowcount != 0:
                                        print("Staff Removed Sucessfully")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("No Such Staff Exists...\n")    
                                except:
                                    sys.stderr.write("Wrong Choice...Enter Again...\n")    
                            D_S_id()
                        elif a == 2:
                            def D_S_name():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                try:
                                    s_name = input("Enter Staff Name you want to Remove :")
                                    s = "delete from staff  where S_Name = '"+s_name+"'"
                                    cur.execute(s)
                                    if cur.rowcount != 0:
                                        print("Staff Removed Sucessfully")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("No Such Staff Exists..\n")
                                except:
                                    sys.stderr.write("Wrong Choice...Enter Again...\n")
                            D_S_name()
                        elif a == 3:
                            def D_S_D():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                try:
                                    d = input("Enter Staff Department you want to Remove :")
                                    s = "delete from staff  where Department = '"+d+"'"
                                    cur.execute(s)
                                    if cur.rowcount != 0:
                                        print("Staff Removed Sucessfully")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("No Such Staff Exists...\n")
                                except:
                                    sys.stderr.write("Wrong Choice...Enter Again...\n")
                            D_S_D()
                        elif a == 4:
                            def D_S_S():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                try:
                                    s = input("Enter Staff Salary you want to Remove :")
                                    s = "delete from staff where Salary = '"+s+"'"
                                    cur.execute(s)
                                    if cur.rowcount != 0:
                                        print("Staff Removed Sucessfully")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("No Such Staff Exists...\n")
                                except:
                                    sys.stderr.write("Wrong Choice...Enter Again...\n")
                            D_S_S()
                        elif a == 5:
                            def D_S_E():
                                import mysql.connector as m
                                import sys
                                con = m.connect(host='localhost',user='root',password='root',database='invoices')
                                cur = con.cursor()
                                try:
                                    e = input("Enter Staff Experience you want to Remove :")
                                    s = "delete from staff  where Experience = '"+e+"'"
                                    cur.execute(s)
                                    if cur.rowcount != 0:
                                        print("Staff Removed Sucessfully")
                                        con.commit()
                                        cur.close()
                                        con.close()
                                    else:
                                        sys.stderr.write("No Such Staff Exists...\n")
                                except:
                                    sys.stderr.write("Wrong Choice...Enter Again...\n")
                            D_S_id()
                        elif a == 6:
                            break
                        else:
                            sys.stderr.write("Wrong Choice... Enter Again...\n")
                elif inp == 6:
                    break
                else:
                    sys.stderr.write("Wrong Choice... Enter Again...\n")
        elif inp == 3:
            while True:
                print("\t\t!! Welcome To Settings !!")
                print("\t\t=========================")
                print("\n")
                print("\t1. Add Personal Notes")
                print("\t2. See Notes")
                print("\t2. Want To See Structure of Invoice Table")
                print("\t3. Want To See Structure of Products Table")
                print("\t4. Want To See Structure of Staff Table")
                print("\t5. Want To Format Everything")
                print("\t6. Back to Menu")
                a = int(input("Enter your Choice :"))
                if a == 1:
                    def note():
                        with open ("Notes.txt","a") as f:
                            s = input("Add Your Note Here :")
                            f.write("\n")
                            f.write(s)
                            f.write("\n")
                            f.close()
                        print("Note added sucessfully")
                    note()
                elif a == 2:
                    def see_note():
                        with open ("Notes.txt","r") as f:
                            data = f.read()
                            print(data)
                        print("Notes displayed sucessfully")
                    see_note()
                elif a == 3:
                    import mysql.connector as m
                    import sys
                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                    cur = con.cursor()
                    try:
                        cur.execute("desc product")
                        b = cur.fetchall()
                        if cur.rowcount != 0:
                            from prettytable import PrettyTable as PT
                            x = PT()
                            for i in b:
                                x.add_row(i)
                            print(x)
                        else:
                            sys.stderr.write("No Such Table Exists...\n")
                    except:
                        sys.stderr.write("Some Error Occured...\n")
                elif a == 4:
                    import mysql.connector as m
                    import sys
                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                    cur = con.cursor()
                    try:
                        cur.execute("desc staff")
                        b = cur.fetchall()
                        if cur.rowcount != 0:
                            from prettytable import PrettyTable as PT
                            x = PT()
                            for i in b:
                                x.add_row(i)
                            print(x)
                        else:
                            sys.stderr.write("No Such Table Exists...\n")
                    except:
                        sys.stderr.write("Some Error Occured...\n")
                elif a == 5:
                    import mysql.connector as m
                    import sys
                    con = m.connect(host='localhost',user='root',password='root',database='invoices')
                    cur = con.cursor()
                    sys.stderr.write("Note: By pressing Yes you will lose your whole data from your account. Manager will be removed completely\n")
                    try:
                        inp = input("\tEnter Y/N for formatting :")
                        if inp == "Y" or inp == "y" or inp == "Yes" or inp == "yes":
                            print("Formatting Started")
                            cur.execute("drop table invoice")
                            print("Invoice Details Deleted Sucessfuly")
                            con.commit()
                            cur.execute("drop table product")
                            print("Product Details Deleted Sucessfuly")
                            con.commit()
                            cur.execute("drop table staff")
                            print("Staff Details Deleted Sucessfuly")
                            con.commit()
                            with open ("Notes.txt",'r+') as f:
                                f.truncate(0)
                                f.close()
                                print("Notes Erased Sucessfully")
                            with open ("invoice.txt",'r+') as f1:
                                f1.truncate(0)
                                print("Products Erased Sucessfully")
                                f1.close()
                        elif inp == 'N' or inp == 'n' or inp == 'no' or inp == 'NO':
                            print("Formatting Stopped")
                        else:
                            sys.stderr.write("Wrong Choice... Enter Again...\n")
                    except:
                        sys.stderr.write("Already Formatted Please Check...\n")
                    break
                elif a == 6:
                    break
                else:
                    sys.stderr.write("Wrong Choice...Enter Again...\n")
        elif inp == 4:
            quit()
        else:
            sys.stderr.write("Wrong Choice...Enter Again...\n")
Menu()
