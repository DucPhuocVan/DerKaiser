from tkinter import *
import os
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date

"""Cửa sổ TCP client"""

window = Tk()
window.geometry("805x100") #kich thuoc cua so
window.title("TCP Client") # tieu de cua so
register_img=PhotoImage(file='image//login.png')
window.iconphoto(True,register_img)
window.config(background="white")

IP_addr=Label(window,
              text="ID Address",
              font=("Arial",15),
             compound='left',
               bg="white")
IP_addr.place(x=25,y=20)
IP_addr_entry=Entry(window,
            font=("Arial",12),
            fg="black",
            bg="white")
IP_addr_entry.place(x=25,y=50)

Port=Label(window,
              text="Port",
              font=("Arial",15),
             compound='left',
               bg="white")
Port.place(x=250,y=20)
Port_entry=Entry(window,
            font=("Arial",12),
            fg="black",
            bg="white")
Port_entry.place(x=250,y=50)

"""Hàm nút conect của TCP Client đi vào login form"""

def Conect_def():

    """Cửa sổ login form"""
    window = Toplevel()
    window.geometry("330x400")  # kich thuoc cua so
    window.title("Login Form")  # tieu de cua so
    login_img = PhotoImage(file='image//login.png')
    window.iconphoto(True, login_img)
    window.config(background="white")

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    login = Label(window,
                  image=login_img,
                  text="USER LOGIN",
                  font=('Arial', 25, 'bold'),
                  fg="black",
                  compound='top',
                  bg="white")
    login.pack()

    """label và nhập username trong cửa sổ Login form"""
    username_img = PhotoImage(file='image//username.png')
    username = Label(window,
                     image=username_img,
                     text="User name",
                     compound='left',
                     bg="white")
    username.place(x=55, y=150)
    username_entry = Entry(window,
                           font=("Arial", 15),
                           fg="black",
                           bg="white",
                           textvariable=username_verify)
    username_entry.place(x=55, y=185)

    """label và nhập password trong cửa sổ Login form"""
    password_img = PhotoImage(file='image//password.png')
    password = Label(window,
                     image=password_img,
                     text="Password",
                     compound='left',
                     bg="white")
    password.place(x=55, y=215)
    password_entry = Entry(window,
                           font=("Arial", 15),
                           fg="black",
                           bg="white",
                           show="*",
                           textvariable=password_verify)
    password_entry.place(x=55, y=252)

    def mark():

        if var.get() == 1:
            password_entry.configure(show="")
        elif var.get() == 0:
            password_entry.configure(show="*")

    var = IntVar()

    bt = Checkbutton(window, command=mark, offvalue=0, onvalue=1, variable=var, bg="white")
    bt.place(x=50, y=280)
    show_password = Label(window,
                     text="Show password",
                     compound='left',
                     bg="white")
    show_password.place(x=70, y=282)


    """Hàm nút login từ login form đi vào cửa sổ search form """

    def login_def():
        """Cửa sổ search form"""
        window = tk.Toplevel()
        window.geometry("700x400")  # kich thuoc cua so
        window.title("Search Form")  # tieu de cua so
        register_img = PhotoImage(file='image//search.png')
        window.iconphoto(True, register_img)
        window.config(background="white")

        text_header = Label(window,
                            bg="light grey",
                            font=("Arial", 10),
                            height=3,
                            width=83,
                            compound='top')
        text_header.place(x=15, y=0)

        """Hàm xử lí và nút log out trong cửa sổ Search form"""
        def logout_def():
            if messagebox.askokcancel(title='Log out !!!',message='Do you want to log out of your account ??'):
                window.destroy()
                Conect_def()

        img_logout = PhotoImage(file='image//logout.png')

        logout_img_button = Button(window, command=logout_def,
                                   image=img_logout,
                                   compound='right',
                                   bg="white")
        logout_img_button.place(x=630, y=3)

        logout_button = Label(window, text="Log out",
                              bg="light grey")
        logout_button.place(x=623, y=33)

        """Xử lí Hello username trong cửa sổ Search form"""
        text_hello = Label(window,
                           text="Hello {} ".format(username_verify),
                           font=("Console", 15),
                           compound='left',
                           bg="light grey")
        text_hello.place(x=30, y=15)

        """Xử lí đoạn combo box tra cứu ngày tháng"""
        ttk.Label(window,
                  text="DATE",
                  font=("Console", 10, "bold")).place(x=25, y=60)

        cal = DateEntry(window, width=12,
                        background='darkblue',
                        cursor="hand1",
                        foreground='white',
                        borderwidth=2)
        cal.place(x=25, y=80)


        """Xử lí đoạn combo box tra cứu current"""
        ttk.Label(window,
                  text="CURRENT",
                  font=("Console", 10, "bold")).place(x=200, y=60)

        n = tk.StringVar()
        currentchoosen = ttk.Combobox(window, width=27,textvariable=n)

        currentchoosen['values'] = ('Tất cả',
                                    ' USD-Đôla Mĩ',
                                    ' EUR-Euro',
                                    ' GBP-Bảng Anh',
                                    ' HKD-Đô Hồng Kông',
                                    ' CHF-Franc Thuỵ Sĩ',
                                    ' JPY-Yên Nhật',
                                    ' AUD-Đô Úc',
                                    ' SGD-Đô Singapore',
                                    ' THB-Bat Thái Lan',
                                    ' CAD-Đô Canada',
                                    ' NZD-Đô New Zealand',
                                    ' KRW-Won Korean')
        currentchoosen.place(x=200, y=80)
        currentchoosen.current()

        """Nút và hàm xử lí của nút search trong cửa sổ Search form"""
        def search_def():
            pass

        img_search = PhotoImage(file='image//search.png')
        search_button = Button(window, text="Search  ", command=search_def,
                               height=20,
                               width=100,
                               font=("Console", 12),
                               bg='#0099FF',
                               image=img_search,
                               compound='right')
        search_button.place(x=410, y=73)

        """Nút và hàm xử lí của nút reset trong cửa sổ Search form"""
        def reset_def():
            pass

        img_reset = PhotoImage(file='image//reset.png')
        reset_button = Button(window, text="Reset  ", command=reset_def,
                              height=20,
                              width=100,
                              font=("Console", 12),
                              bg='#0099FF',
                              image=img_reset,
                              compound='right')
        reset_button.place(x=550, y=73)

        """Phần chứa dữ liệu lấy từ trang web sẽ hiển thị ở đây"""
        text_Server = Label(window,
                            bg="light grey",
                            font=("Arial", 10),
                            height=17,
                            width=83,
                            compound='top')
        text_Server.place(x=15, y=110)

        window.mainloop()

    """Hàm nút register của login form đi vào register form"""

    def register_def():
        window = Toplevel()
        window.geometry("350x430")  # kich thuoc cua so
        window.title("Register Form")  # tieu de cua so
        register_img = PhotoImage(file='image//register.png')
        window.iconphoto(True, register_img)
        window.config(background="white")

        global username_var
        global password_var
        global username_entry
        global password_entry

        username_var = StringVar()
        password_var = StringVar()
        confirm_password_var = StringVar()

        login = Label(window,
                      image=register_img,
                      text="REGISTER",
                      font=('Arial', 20, 'bold'),
                      fg="black",
                      compound='top',
                      bg="white")
        login.pack()

        """Nút và label của username trong cửa sổ register form"""
        username_img = PhotoImage(file='image//username.png')
        username = Label(window,
                         image=username_img,
                         text="User name",
                         compound='left',
                         bg="white")
        username.place(x=55, y=160)
        username_entry = Entry(window,
                               font=("Arial", 15),
                               fg="black",
                               bg="white",
                               textvariable=username_var)
        username_entry.place(x=55, y=195)

        """Nút và label của password trong cửa sổ register form"""
        password_img = PhotoImage(file='image//password.png')
        password = Label(window,
                         image=password_img,
                         text="Password",
                         compound='left',
                         bg="white")
        password.place(x=55, y=225)
        password_entry = Entry(window,
                               font=("Arial", 15),
                               fg="black",
                               bg="white",
                               show="*",
                               textvariable=password_var)
        password_entry.place(x=55, y=262)

        def mark():

            if var.get() == 1:
                password_entry.configure(show="")
            elif var.get() == 0:
                password_entry.configure(show="*")

        var = IntVar()

        bt = Checkbutton(window, command=mark, offvalue=0, onvalue=1, variable=var, bg="white")
        bt.place(x=55, y=290)
        show_password = Label(window,
                              text="Show password",
                              compound='left',
                              bg="white")
        show_password.place(x=75, y=292)

        """Nút và label của confirm password trong cửa sổ register form"""
        confirm_password_img = PhotoImage(file='image//confirmpass.png')
        confirm_password = Label(window,
                                 image=confirm_password_img,
                                 text="Confirm password",
                                 compound='left',
                                 bg="white")
        confirm_password.place(x=55, y=312)
        confirm_password_entry = Entry(window,
                                       font=("Arial", 15),
                                       fg="black",
                                       bg="white",
                                       show="*",
                                       textvariable=confirm_password_var)
        confirm_password_entry.place(x=55, y=345)

        """Hàm xử lí lưu username và password trong cửa sổ register form"""
        def register_user():
            username_info = username_var.get()
            password_info = password_var.get()
            confirm_password_info = confirm_password_var.get()
            if password_info == confirm_password_info:
                file = open(username_info, "w")
                file.write(username_info + "\n")
                file.write(password_info)
                file.close()

                username_entry.delete(0, END)
                password_entry.delete(0, END)
                confirm_password_entry.delete(0, END)
                if messagebox.askokcancel(title='Registration Success',message='Congratulations on your successful registration !!'):
                        window.destroy()

            elif password_info != confirm_password_info:
                messagebox.showerror(title='Registration failed!',message='Password and confirm password do not match !!')

        """Nút register trong cửa sổ register form"""
        register_button = Button(window, text="REGISTER", command=register_user,
                                 height=1,
                                 width=27,
                                 font=("Arial", 10, 'bold'),
                                 bg='#0099FF',
                                 )
        register_button.place(x=55, y=385)

        window.mainloop()

    """Các hàm xử lí phần password của login form"""

    def password_not_recognised():
        messagebox.showerror(title='Incorrect password!', message='Incorrect password !!')

    def user_not_found():
        messagebox.showerror(title='User not found!', message='User not found !!')

    def login_verify():
        username1 = username_verify.get()
        password1 = password_verify.get()

        username_entry.delete(0, END)
        password_entry.delete(0, END)

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                if messagebox.askokcancel(title='Login Success',message='Congratulations on your successful login, please look up the currency rate here !!'):
                    window.destroy()
                    login_def()


            else:
                password_not_recognised()

        else:
            user_not_found()
    """Nút login của cửa sổ login form"""
    login_button = Button(window, text="LOGIN", command=login_verify,
                          height=1,
                          width=27,
                          font=("Arial", 10, 'bold'),
                          bg='#0099FF')
    login_button.place(x=55, y=315)

    """Nút register của cửa sổ login form"""
    register_button = Button(window, text="REGISTER", command=register_def,
                             height=1,
                             width=27,
                             font=("Arial", 10, 'bold'),
                             bg='#736F6E')
    register_button.place(x=55, y=350)

    window.mainloop()

"""Nút CONECT của cửa sổ TCP-Client"""
login_button=Button(window,text="CONECT",command=Conect_def,
                    height=1,
                    width=15,
                    font=("Arial",10,'bold'),
                    bg='#0099FF')
login_button.place(x=480,y=45)

def Disconect_def():
    window.destroy()

"""Nút DISCONECT của cửa sổ TCP-Client"""
register_button=Button(window,text="DISCONECT",command=Disconect_def,
                    height=1,
                    width=15,
                    font=("Arial",10,'bold'),
                    bg='#736F6E')
register_button.place(x=650,y=45)

window.mainloop()