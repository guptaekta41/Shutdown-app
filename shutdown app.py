from tkinter import *
import os

def Restart():
    os.system("shutdown/r/t 1")
def restart_time():
    os.system("shutdown/r/t 20")
def log_off():
    os.system("shutdown -1")
# def shutdown():
    # os.system("shutdown /s /t 1")


st = Tk() # class
st.title("shutdown app")
st.geometry("500x500")
st.config(bg= "Yellow")

r_button = Button(st,text="Restart",font=("time new roman",20,"bold"),relief=RAISED,cursor="circle",command=Restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(st,text="Restart_time",font=("time new roman",20,"bold"),relief=RAISED,cursor="circle",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button = Button(st,text="log_off",font=("time new roman",20,"bold"),relief=RAISED,cursor="circle",command=log_off)
lg_button.place(x=150,y=270,height=50,width=200)

# st_button = Button(st,text="shutdown",font=("time new roman",20,"bold"),relief=RAISED,cursor="circle",command=shutdown)
# st_button.place(x=150,y=370,height=50,width=200)

st.mainloop()


