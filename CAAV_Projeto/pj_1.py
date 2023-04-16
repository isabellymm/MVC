from tkinter import *
from tkinter import ttk

jnla = Tk()

class Aplicacao():

    def __init__(self) :
        self.jnla = jnla
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()


        
        jnla.mainloop()

    def tela (self):
        self.jnla
        self.jnla.title("Cadastro de Usuarios",)
        self.jnla.configure(background="#757575")
        self.jnla.geometry('800x600')
        self.jnla.resizable(True,True)
        self.jnla.maxsize(width=1000, height=700)
        self.jnla.minsize(width=900, height=500)


    def frames_da_tela(self):
        self.frame_1 = Frame(self.jnla, bd=1, bg="#BEBEBE", highlightbackground="#A9A9A9", highlightthickness=4)
        self.frame_1.place(relx=0.02 , rely=0.02 , relwidth=0.96 , relheight=0.95)

    
    def widgets_frame1(self):
        self.lb_nome = Label(self.frame_1, text="Nome", bg="#A9A9A9")
        self.lb_nome.place(relx=0.2, rely=0.25,relwidth=0.08, relheight=0.05)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.32 , rely=0.25, relwidth=0.48, relheight=0.05)

        self.lb_email = Label(self.frame_1, text="Email", bg="#A9A9A9")
        self.lb_email.place(relx=0.2, rely=0.35,relwidth=0.08, relheight=0.05)

        self.email_entry = Entry(self.frame_1)
        self.email_entry.place(relx=0.32 , rely=0.35, relwidth=0.48, relheight=0.05)

        self.lb_fone = Label(self.frame_1, text="Telefone", bg="#A9A9A9")
        self.lb_fone.place(relx=0.2, rely=0.45,relwidth=0.08, relheight=0.05)

        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx=0.32 , rely=0.45, relwidth=0.48, relheight=0.05)

        self.lb_usuario = Label(self.frame_1, text="Usuario", bg="#A9A9A9")
        self.lb_usuario.place(relx=0.2, rely=0.55,relwidth=0.08, relheight=0.05)

        self.usuario_entry = Entry(self.frame_1)
        self.usuario_entry.place(relx=0.32 , rely=0.55, relwidth=0.48, relheight=0.05)

        self.lb_senha = Label(self.frame_1, text="Senha", bg="#A9A9A9")
        self.lb_senha.place(relx=0.2, rely=0.65,relwidth=0.08, relheight=0.05)

        self.senha_entry = Entry(self.frame_1)
        self.senha_entry.place(relx=0.32 , rely=0.65, relwidth=0.48, relheight=0.05)

        self.bt_cadastar = Button(self.frame_1, text="Cadastar",bg="#0088DE" ,fg="white", relief="flat") 
        self.bt_cadastar.place(relx=0.6, rely=0.75, relwidth=0.2, relheight=0.09)

        
        self.bt_login = Button(self.frame_1, text="Login",bg="#0088DE" ,fg="white", relief="flat") 
        self.bt_login.place(relx=0.32, rely=0.75, relwidth=0.2, relheight=0.09)

        self.text_login = Label(self.frame_1, bd= 2, background="#0088DE", text = "CADASTRO", relief="flat")
        self.text_login.place(relx=0.0 , rely=0, relwidth=1, relheight=0.1)



Aplicacao()