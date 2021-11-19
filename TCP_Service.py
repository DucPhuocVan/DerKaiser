from tkinter import *

#grid() = geometry manager that organizes widgets in a table-like structure in a parent widget

window = Tk()
window.geometry("700x400") #kich thuoc cua so
window.title("TCP Server") # tieu de cua so
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
            font=("Arial",10),
            fg="black",
            bg="white")
IP_addr_entry.place(x=25,y=50)

Port=Label(window,
              text="Port",
              font=("Arial",15),
             compound='left',
               bg="white")
Port.place(x=200,y=20)
Port_entry=Entry(window,
            font=("Arial",10),
            fg="black",
            bg="white")
Port_entry.place(x=200,y=50)

def run_def():
    pass
run_button=Button(window,text="RUN",command=run_def,
                    height=1,
                    width=10,
                    font=("Arial",10,'bold'),
                    bg='#0099FF')
run_button.place(x=380,y=45)

def stop_def():
    pass
stop_button=Button(window,text="STOP",command=stop_def,
                    height=1,
                    width=10,
                    font=("Arial",10,'bold'),
                    bg='red')
stop_button.place(x=480,y=45)

def Restart_def():
    pass
register_button=Button(window,text="RESTART",command=Restart_def,
                    height=1,
                    width=10,
                    font=("Arial",10,'bold'),
                    bg='grey')
register_button.place(x=580,y=45)

text_Server = Label(window,
            bg="light grey",
            font=("Arial",10),
            height=17,
            width=53,
            compound='top')
text_Server.place(x=15,y=110)

text = Label(window,
            text="Server is running...",
            bg="light grey",
            font=("Arial",10))
text.place(x=15,y=110)

Client_Status=Label(window,
              text="Client status (conected)",
              font=("Arial",10),
             compound='left',
               bg="white")
Client_Status.place(x=460,y=90)

text_Client_Status = Label(window,
            bg="light grey",
            font=("Arial",10),
            height=16,
            width=25,
            padx=10,
            pady=10,
            fg="purple")
text_Client_Status.place(x=460,y=110)

window.mainloop()