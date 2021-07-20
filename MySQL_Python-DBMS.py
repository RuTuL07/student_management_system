"""
DBMS MINI PROJECT
Student record database(Student management system)
"""

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql


class ConnectorDB:
    def __init__(self, root):
        self.root = root

        self.root.title("MySQL Connector")
        self.root.geometry("750x620+300+0")
        self.root.resizable(width=False, height=False)

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief=RIDGE, bg="cadet blue")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=770, height=400, padx=2, relief=RIDGE, bg="cadet blue")
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=12, pady=9, relief=RIDGE)
        LeftFrame1.pack(side=TOP, padx=0, pady=0)

        RightFrame = Frame(TopFrame3, bd=5, width=100, height=400, padx=2, relief=RIDGE, bg="cadet blue")
        RightFrame.pack(side=RIGHT)
        RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame1.pack(side=TOP)

        StudentID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Email = StringVar()
        Phone_no = StringVar()
        Gender = StringVar()

        def i_exit():
            i_exit = tkinter.messagebox.askyesno("Database", "Confirm if you want to exit")
            if i_exit > 0:
                root.destroy()
                return

        def reset():
            self.eStudentID.delete(0, END)
            self.eFirstname.delete(0, END)
            self.eLastname.delete(0, END)
            self.eEmail.delete(0, END)
            self.ePhone_no.delete(0, END)
            Gender.set("")

        def addData():
            if StudentID.get() == "" or Firstname.get() == "" or Lastname.get() == "":
                tkinter.messagebox.showerror("Database", "Enter correct details")
            else:
                sql_connection = pymysql.connect(host='localhost', user='root', password='', database='DBMS')
                mycursor = sql_connection.cursor()  # my..obj cur fun
                mycursor.execute("insert into students_record values({},'{}','{}','{}',{},'{}')".format(
                    StudentID.get(),
                    Firstname.get(),
                    Lastname.get(),
                    Email.get(),
                    Phone_no.get(),
                    Gender.get()
                ))
                sql_connection.commit()
                sql_connection.close()
                tkinter.messagebox.showinfo("Database", "Record inserted successfully")

        def display_data():
            sql_connection = pymysql.connect(host='localhost', user='root', password='', database='DBMS')
            mycursor = sql_connection.cursor()  # my..obj cur fun
            mycursor.execute("SELECT * FROM students_record")
            result = mycursor.fetchall()
            if len(result) != 0:
                self.student_record.delete(*self.student_record.get_children())
                for row in result:
                    self.student_record.insert('', END, values=row)
                sql_connection.commit()
            sql_connection.close()

        def view_info(ev):
            viewInfo = self.student_record.focus()
            data = self.student_record.item(viewInfo)
            row = data['values']
            StudentID.set(row[0])
            Firstname.set(row[1])
            Lastname.set(row[2])
            Email.set(row[3])
            Phone_no.set(row[4])
            Gender.set(row[5])

        def update():
            sql_connection = pymysql.connect(host='localhost', user='root', password='', database='DBMS')
            mycursor = sql_connection.cursor()  # my..obj cur fun
            mycursor.execute("UPDATE students_record set firstname='{}',lastname='{}',email='{}',phone_no={},"
                             "gender='{}' WHERE std_id={}".format(

                Firstname.get(),
                Lastname.get(),
                Email.get(),
                Phone_no.get(),
                Gender.get(),
                StudentID.get(),
            ))

            sql_connection.commit()
            display_data()
            sql_connection.close()
            tkinter.messagebox.showinfo("Database", "Record Updated successfully")

        def delete():
            sql_connection = pymysql.connect(host='localhost', user='root', password='', database='DBMS')
            mycursor = sql_connection.cursor()  # my..obj cur fun
            mycursor.execute("DELETE FROM students_record WHERE std_id={}".format(
                StudentID.get(),
            ))
            sql_connection.commit()
            display_data()
            sql_connection.close()
            tkinter.messagebox.showinfo("Database", "'Record Deleted' successfully")
            reset()

        def search():

            try:
                sql_connection = pymysql.connect(host='localhost', user='root', password='', database='DBMS')
                mycursor = sql_connection.cursor()  # my..obj cur fun
                mycursor.execute("SELECT * FROM students_record WHERE std_id={}".format(
                    StudentID.get(),
                ))
                row = mycursor.fetchone()
                StudentID.set(row[0])
                Firstname.set(row[1])
                Lastname.set(row[2])
                Email.set(row[3])
                Phone_no.set(row[4])
                Gender.set(row[5])

                sql_connection.commit()
            except:
                tkinter.messagebox.showinfo("Database", "No Such Record Found")
                reset()
                sql_connection.close()

        # =====================================================================================================================
        self.title = Label(TitleFrame, font=('arial', 30, 'bold'), text='Database', bd=7)
        self.title.grid()

        self.lStudentID = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Student ID", bd=7)
        self.lStudentID.grid(row=1, column=0, sticky=W, padx=5)
        self.eStudentID = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=3, width=44, justify='left',
                                textvar=StudentID)
        self.eStudentID.grid(row=1, column=1, sticky=W, padx=5)

        self.lFirstname = Label(LeftFrame1, font=('arial', 10, 'bold'), text="First Name", bd=7)
        self.lFirstname.grid(row=2, column=0, sticky=W, padx=5)
        self.eFirstname = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=3, width=44, justify='left',
                                textvar=Firstname)
        self.eFirstname.grid(row=2, column=1, sticky=W, padx=5)

        self.lLastname = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Last Name", bd=7)
        self.lLastname.grid(row=3, column=0, sticky=W, padx=5)
        self.eLastname = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=3, width=44, justify='left',
                               textvar=Lastname)
        self.eLastname.grid(row=3, column=1, sticky=W, padx=5)

        self.lEmail = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Email-id", bd=7)
        self.lEmail.grid(row=4, column=0, sticky=W, padx=5)

        self.eEmail = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=3, width=44, justify='left',
                            textvar=Email)
        self.eEmail.grid(row=4, column=1, sticky=W, padx=5)

        self.lPhone_no = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Phone_no", bd=7)
        self.lPhone_no.grid(row=5, column=0, sticky=W, padx=5)

        self.ePhone_no = Entry(LeftFrame1, font=('arial', 10, 'bold'), bd=3, width=44, justify='left',
                               textvar=Phone_no)
        self.ePhone_no.grid(row=5, column=1, sticky=W, padx=5)

        self.lGender = Label(LeftFrame1, font=('arial', 10, 'bold'), text="Gender", bd=7)
        self.lGender.grid(row=6, column=0, sticky=W, padx=5)
        self.cboGender = ttk.Combobox(LeftFrame1, font=('arial', 10, 'bold'), width=20, state='readonly',
                                      textvar=Gender)
        self.cboGender['values'] = (' ', 'Female', 'Male', 'Other')
        self.cboGender.current(0)
        self.cboGender.grid(row=6, column=1, sticky=W)

        # =====================================================TABLE TREEVIEW==========================================
        scroll_y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.student_record = ttk.Treeview(LeftFrame, height=12,
                                           column=("std_id", "firstname", "lastname", "email", "phone_no", "gender"),
                                           yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.student_record.heading("std_id", text="StudentID")
        self.student_record.heading("firstname", text="First name")
        self.student_record.heading("lastname", text="Last name")
        self.student_record.heading("email", text="Email-id")
        self.student_record.heading("phone_no", text="Phone_no")
        self.student_record.heading("gender", text="Gender")

        self.student_record['show'] = 'headings'

        self.student_record.column("std_id", width=70)
        self.student_record.column("firstname", width=100)
        self.student_record.column("lastname", width=100)
        self.student_record.column("email", width=100)
        self.student_record.column("phone_no", width=70)
        self.student_record.column("gender", width=70)

        self.student_record.pack(fill=BOTH, expand=1)
        self.student_record.bind("<ButtonRelease-1>", view_info)  # on click it shows data view_info function
        # display_data()  ---- for always display_data data on display_data function call

        # ===============================================BUTTON======================================================================

        self.btnAddNew = Button(RightFrame1, font=('arial', 12, 'bold'), text="Add New", bd=4, pady=1, padx=24, width=8,
                                height=2, command=addData).grid(row=0, column=0, padx=1)

        self.btnUpdate = Button(RightFrame1, font=('arial', 12, 'bold'), text="Update", bd=4, pady=1, padx=24, width=8,
                                height=2, command=update).grid(row=1, column=0, padx=1)

        self.btnDelete = Button(RightFrame1, font=('arial', 12, 'bold'), text="Delete", bd=4, pady=1, padx=24, width=8,
                                height=2, command=delete).grid(row=2, column=0, padx=1)

        self.btnDisplay = Button(RightFrame1, font=('arial', 12, 'bold'), text="Display", bd=4, pady=1, padx=24,
                                 width=8, height=2, command=display_data).grid(row=3, column=0, padx=1)

        self.btnSearch = Button(RightFrame1, font=('arial', 12, 'bold'), text="Search", bd=4, pady=1, padx=24, width=8,
                                height=2, command=search).grid(row=4, column=0, padx=1)

        self.btnReset = Button(RightFrame1, font=('arial', 12, 'bold'), text="Reset", bd=4, pady=1, padx=24, width=8,
                               height=2, command=reset).grid(row=5, column=0, padx=1)

        self.btnExit = Button(RightFrame1, font=('arial', 12, 'bold'), text="Exit", bd=4, pady=1, padx=24, width=8,
                              height=2, command=i_exit).grid(row=6, column=0, padx=1)


if __name__ == "__main__":
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
