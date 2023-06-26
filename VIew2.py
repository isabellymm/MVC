from tkinter import *
from tkinter import ttk
from Controller import *



class View(ttk.Frame):
    def __init__(self) :

        self.jnla = Tk()
        self.frames_da_tela()
        self.widgets_frame1()
        self.jnla.mainloop()
        

    def tela (self):
        self.jnla
        self.jnla.title("Cadastro de Usuarios",)
        self.jnla.configure(background="#757575")
        self.jnla.geometry('1500x900')
        self.jnla.resizable(True,True)
        self.jnla.maxsize(width=1550, height=900)
        self.jnla.minsize(width=900, height=500)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.jnla, bd=1, bg="#BEBEBE", highlightbackground="#A9A9A9", highlightthickness=4)
        self.frame_1.place(relx=0.01 , rely=0.02 , relwidth=0.98, relheight=0.96)

    def widgets_frame1(self):
        self.lb_nome = Label(self.frame_1, text="Nome", bg="#A9A9A9")
        self.lb_nome.place(relx=0.03, rely=0.05,relwidth=0.055, relheight=0.035)


        self.text_login = Label(self.frame_1, bd= 2, background="#F64C17", text = "CADASTRO", relief="flat")
        self.text_login.place(relx=0.0 , rely= 0, relwidth=1, relheight=0.075)


        self.imgredondo = PhotoImage(file=r"C:\Users\isabe\OneDrive\Área de Trabalho\CAAV_Projeto\CADASTRO.png")

        self.bt_cadastro = Button(self.frame_1, image=self.imgredondo,relief=GROOVE,bd=0) 
        self.bt_cadastro.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.15)



View()