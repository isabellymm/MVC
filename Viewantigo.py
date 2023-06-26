from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controller import *



class View(ttk.Frame):
    def __init__(self , controller) :
        self.controller =  controller


        self.jnla = tk.Tk()
        self.selected = tk.IntVar()
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
        self.lb_nome.place(relx=0.03, rely=0.15,relwidth=0.055, relheight=0.035)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.1 , rely=0.15, relwidth=0.22, relheight=0.035)

        self.lb_telefone = Label(self.frame_1, text="Telefone", bg="#A9A9A9")
        self.lb_telefone.place(relx=0.03, rely=0.25,relwidth=0.055, relheight=0.035)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.1 , rely=0.25, relwidth=0.1, relheight=0.035)


        self.lb_email = Label(self.frame_1, text="Email", bg="#A9A9A9")
        self.lb_email.place(relx=0.03, rely=0.35,relwidth=0.055, relheight=0.035)

        self.email_entry = Entry(self.frame_1)
        self.email_entry.place(relx=0.1 , rely=0.35, relwidth=0.22, relheight=0.035)

        
        self.lb_data_nasc = Label(self.frame_1, text="Data Nascimento", bg="#A9A9A9")
        self.lb_data_nasc.place(relx=0.03, rely=0.45,relwidth=0.065, relheight=0.035)

        self.data_nasc_entry = Entry(self.frame_1)
        self.data_nasc_entry.place(relx=0.1 , rely=0.45, relwidth=0.22, relheight=0.035)


        self.lb_sexo = Label(self.frame_1, text="Sexo", bg="#A9A9A9")
        self.lb_sexo.place(relx=0.03, rely=0.55,relwidth=0.055, relheight=0.035)

        self.radiobuttonM_sexo = ttk.Radiobutton(self.frame_1, text="Masculino", value=1, style='TRadiobutton', cursor='hand2',variable=self.selected)
        self.radiobuttonM_sexo.place(relx=0.1, rely=0.55, relwidth=0.07, relheight=0.035)

        self.radiobuttonF_sexo = ttk.Radiobutton(self.frame_1, text="Feminino", value=2, style='TRadiobutton', cursor='hand2',variable=self.selected)
        self.radiobuttonF_sexo.place(relx=0.18, rely=0.55, relwidth=0.07, relheight=0.035)
        
        self.lb_altura = Label(self.frame_1, text="Altura", bg="#A9A9A9")
        self.lb_altura.place(relx=0.03, rely=0.65,relwidth=0.055, relheight=0.035)

        self.altura_entry = Entry(self.frame_1)
        self.altura_entry.place(relx=0.1 , rely=0.65, relwidth=0.05, relheight=0.035)

        self.lb_peso = Label(self.frame_1, text="Peso", bg="#A9A9A9")
        self.lb_peso.place(relx=0.17, rely=0.65,relwidth=0.055, relheight=0.035)

        self.peso_entry = Entry(self.frame_1)
        self.peso_entry.place(relx=0.24 , rely=0.65, relwidth=0.05, relheight=0.035)


        self.lb_observacao= Label(self.frame_1, text="Observações", bg="#A9A9A9")
        self.lb_observacao.place(relx=0.03, rely=0.75,relwidth=0.055, relheight=0.035)
        
        self.observacao_text = Text(self.frame_1)
        self.observacao_text.place(relx=0.1 , rely=0.75, relwidth=0.22, relheight=0.09)


        self.lb_objetivo = Label(self.frame_1, text="Objetivos", bg="#A9A9A9")
        self.lb_objetivo.place(relx=0.03, rely=0.9,relwidth=0.055, relheight=0.035)
        
        self.objetivo_text = Text(self.frame_1)
        self.objetivo_text.place(relx=0.1 , rely=0.9, relwidth=0.22, relheight=0.09)
        
        #Endereço

        self.lb_cep = Label(self.frame_1, text="CEP", bg="#A9A9A9")
        self.lb_cep.place(relx=0.6, rely=0.15,relwidth=0.055, relheight=0.035)

        self.cep_entry= Entry(self.frame_1)
        self.cep_entry.place(relx=0.67 , rely=0.15, relwidth=0.05, relheight=0.035)

        self.lb_rua= Label(self.frame_1, text="Rua", bg="#A9A9A9")
        self.lb_rua.place(relx=0.6, rely=0.25,relwidth=0.055, relheight=0.035)

        self.rua_entry= Entry(self.frame_1)
        self.rua_entry.place(relx=0.67 , rely=0.25, relwidth=0.22, relheight=0.035)

        self.lb_numero= Label(self.frame_1, text="Numero", bg="#A9A9A9")
        self.lb_numero.place(relx=0.6, rely=0.35,relwidth=0.055, relheight=0.035)

        self.numero_entry= Entry(self.frame_1)
        self.numero_entry.place(relx=0.67 , rely=0.35, relwidth=0.05, relheight=0.035)

        self.lb_bairro= Label(self.frame_1, text="Bairro", bg="#A9A9A9")
        self.lb_bairro.place(relx=0.6, rely=0.45,relwidth=0.055, relheight=0.035)

        self.bairro_entry= Entry(self.frame_1)
        self.bairro_entry.place(relx=0.67 , rely=0.45, relwidth=0.22, relheight=0.035)

        self.lb_cidade= Label(self.frame_1, text="Cidade", bg="#A9A9A9")
        self.lb_cidade.place(relx=0.6, rely=0.55,relwidth=0.055, relheight=0.035)

        self.cidade_entry= Entry(self.frame_1)
        self.cidade_entry.place(relx=0.67 , rely=0.55, relwidth=0.22, relheight=0.035)

        self.lb_estado= Label(self.frame_1, text="Estado", bg="#A9A9A9")
        self.lb_estado.place(relx=0.6, rely=0.65,relwidth=0.055, relheight=0.035)

        self.estado_entry= Entry(self.frame_1)
        self.estado_entry.place(relx=0.67 , rely=0.65, relwidth=0.22, relheight=0.035)

        self.frequencia_treino= Label(self.frame_1, text="Frequencia de Treinamento Semanal", bg="#A9A9A9")
        self.frequencia_treino.place(relx=0.6, rely=0.75,relwidth=0.15, relheight=0.035)

        self.frequencia_treino_entry= Entry(self.frame_1)
        self.frequencia_treino_entry.place(relx=0.77, rely=0.75, relwidth=0.02, relheight=0.035)

        self.cadastro_label = Label(self.frame_1, bd= 2, background="#0088DE", text = "CADASTRO", relief="flat")
        self.cadastro_label.place(relx=0.0 , rely= 0, relwidth=1, relheight=0.075)


        ##botoes

        self.bt_cadastro = Button(self.frame_1, text="Cadastar", bg="#0088DE" ,fg="white", relief="flat",command=self.save_button) 
        self.bt_cadastro.place(relx=0.7, rely=0.85, relwidth=0.2, relheight=0.09)



    

    def clear_fields(self):
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.data_nasc_entry.delete(0, END)
        self.altura_entry.delete(0, END)
        self.peso_entry.delete(0, END)
        self.observacao_text.delete(0, END)
        self.objetivo_text.delete(0, END)
        self.cep_entry.delete(0, END)
        self.rua_entry.delete(0, END)
        self.numero_entry.delete(0, END)
        self.bairro_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.estado_entry.delete(0, END)
        self.frequencia_treino_entry.delete(0, END)

    def save_button(self):
        if self.controller:

            if self.selected.get() ==  1:
                sexo = "Masculino"
            else:
                sexo = "Feminino"
    
            nome = self.nome_entry.get()
            telefone = self.telefone_entry.get()
            email = self.email_entry.get()
            data_nasc = self.data_nasc_entry.get()
            altura = self.altura_entry.get()
            peso = self.peso_entry.get()
            cep = self.cep_entry.get()
            rua = self.rua_entry.get()
            numero = self.numero_entry.get()
            bairro = self.bairro_entry.get()
            cidade = self.cidade_entry.get()
            estado = self.estado_entry.get()


        self.controller.save_cadastro(sexo, nome, telefone, email, data_nasc, altura, peso,
        cep, rua, numero, bairro, cidade, estado)


        self.clear_fields()


                

            