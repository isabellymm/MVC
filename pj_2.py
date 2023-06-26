from tkinter import *
from tkinter import ttk

jnla = Tk()

class Aplicacao():

    def __init__(self) :
        self.jnla = jnla
        self.frames_da_tela()
        self.tela_2()
        self.widgets_frame2()

        jnla.mainloop()

    def frames_da_tela(self):
        self.frame_2 = Frame(self.jnla, bd=1, bg="#BEBEBE", highlightbackground="#A9A9A9", highlightthickness=4)
        self.frame_2.place(relx=0.02 , rely=0.02 , relwidth=0.96 , relheight=0.95)

    def tela_2(self):
        self.jnla
        self.jnla.title("Login")
        self.jnla.configure(background="#757575")
        self.jnla.geometry('800x600')
        self.jnla.resizable(True,True)
        self.jnla.maxsize(width=600, height=500)
        self.jnla.minsize(width=600, height=500)

    def widgets_frame2(self):
        self.lb_usuario = Label(self.frame_2, text="Usuario", bg="#A9A9A9")
        self.lb_usuario.place(relx=0.18, rely=0.28,relwidth=0.08, relheight=0.05)

        self.usuario_entry = Entry(self.frame_2)
        self.usuario_entry.place(relx=0.32 , rely=0.28, relwidth=0.48, relheight=0.05)


        self.lb_senha = Label(self.frame_2, text="Senha", bg="#A9A9A9")
        self.lb_senha.place(relx=0.18, rely=0.4,relwidth=0.08, relheight=0.05)

        self.senha_entry = Entry(self.frame_2)
        self.senha_entry.place(relx=0.32 , rely=0.4, relwidth=0.48, relheight=0.05)
        

        self.bt_login = Button(self.frame_2, text="Login",bg="#0088DE" ,fg="white", relief="flat") 
        self.bt_login.place(relx=0.28, rely=0.55, relwidth=0.2, relheight=0.09)

        self.bt_esq_senha = Button(self.frame_2, text="Esqueci a senha",bg="#0088DE" ,fg="white", relief="flat") 
        self.bt_esq_senha.place(relx=0.58, rely=0.55, relwidth=0.2, relheight=0.09)

        self.text_login = Label(self.frame_2, bd= 2, background="#0088DE", text = "LOGIN", relief="flat")
        self.text_login.place(relx=0 , rely=0, relwidth=1 , relheight=0.1)


Aplicacao()

