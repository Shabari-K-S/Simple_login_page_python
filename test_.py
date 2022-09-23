from tkinter import *
from tkinter import messagebox
import tkinter
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.geometry("925x500")
app.title("Login")
app.resizable(False, False)


img = PhotoImage(file='111.png')
label_1 = customtkinter.CTkLabel(master=app, image=img, justify = tkinter.LEFT)
label_1.place(x=50,y=50)
frame_1 = customtkinter.CTkFrame(master=app, width = 350, height = 350)
frame_1.place(x=480,y=70)

label_2 = customtkinter.CTkLabel(master=frame_1, text="Sign In",text_font = ('Microsoft Yahei UI Light',23,"bold"),  justify=tkinter.LEFT)
label_2.place(x=100,y=5)

username= customtkinter.CTkEntry(master=frame_1, width=280, text_font = ('Microsoft Yahei UI Light',11), placeholder_text="Username")
username.place(x=30,y=80)

password= customtkinter.CTkEntry(master=frame_1, width=280, text_font = ('Microsoft Yahei UI Light',11), placeholder_text="Password")
password.place(x=30,y=150)

button_2 = customtkinter.CTkButton(master=frame_1, text="Sign in", corner_radius=6, command=None, width=200).place(x=70,y=204)

label = customtkinter.CTkLabel(master=frame_1,text="Don't have an account?",text_font=("Microsoft YaHei UI Light",9))
label.place(x=55,y=270)

sign_up = customtkinter.CTkButton(master=frame_1, text="Sign up",text_color="#57a1f8",border_width=0,bg_color=None,fg_color=None,hover_color=None, command=None)
sign_up.place(x=195,y=270)
app.mainloop()