from tkinter import *
from tkinter import ttk
import sqlite3



root = Tk()

class Funcs():
    def limpa_cliente(self):
        self.codigo_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.nome_entry.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")

    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")

    def montaTabelas(self):
        self.conecta_bd()
        ### Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)               
            );
        """)
        
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def add_cliente(self):
        self.codigo = self.codigo_entry.get()
        self.nome =  self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_bd()

class Aplicacao(Funcs):

    def __init__(self) :
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()

    
        root.mainloop()



    def tela(self):
        self.root.title("Cadastro de Clientes",)
        self.root.configure(background="#1e3743")
        self.root.geometry('800x600')
        self.root.resizable(True,True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=600, height=500)
        

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd=1, bg="#dfe3ee", highlightbackground="#749fe6", highlightthickness=3)
        self.frame_1.place(relx=0.02 , rely=0.02, relwidth=0.96 , relheight=0.46)

        self.frame_2 = Frame(self.root, bd=1, bg="#dfe3ee", highlightbackground="#749fe6", highlightthickness=3)
        self.frame_2.place(relx=0.02 , rely=0.52, relwidth=0.96 , relheight=0.46)


    def widgets_frame1(self):
        
        #criacao do botao limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar",bg="#107db2" ,fg="white", command=self.limpa_cliente)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        #criacao do botao buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar",bg="#107db2" ,fg="white") 
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        #criacao do botao novo
        self.bt_novo = Button(self.frame_1, text="Novo",bg="#107db2" ,fg="white", command=self.add_cliente) 
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        #criacao do botao alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar",bg="#107db2" ,fg="white") 
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        #criacao do botao apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar",bg="#107db2" ,fg="white") 
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)


        #criacao da label e entrada do codigo
        self.lb_codigo = Label(self.frame_1, text="Código")
        self.lb_codigo.place(relx=0.05, rely=0.09,relwidth=0.08)


        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05 , rely=0.18, relwidth=0.08)

        #criacao da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text="Nome", bg="#dfe3ee")
        self.lb_nome.place(relx=0.05, rely=0.35)


        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05 , rely=0.45, relwidth=0.85, relheight=0.1)


        #criacao da label e entrada do telefone
        self.lb_fone = Label(self.frame_1, text="Telefone", bg="#dfe3ee")
        self.lb_fone.place(relx=0.05, rely=0.65)


        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx=0.05 , rely=0.75, relwidth=0.4, relheight=0.1)

        #criacao da label e entrada do cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade", bg="#dfe3ee")
        self.lb_cidade.place(relx=0.5, rely=0.65)


        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5 , rely=0.75, relwidth=0.4, relheight=0.1 )

    def lista_frame2(self):
    
        self.listaCli = ttk.Treeview(self.frame_2, height=3, column=("col1", "col12", "col3","col4"))
        self.listaCli.heading("#0", text="",)
        self.listaCli.heading("#1", text="Código")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidades")

        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=200)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        self.listaCli.place(relx=0.01 , rely=0.1, relwidth=0.98, relheight=0.85)


        self.scroolLista = Scrollbar(self.frame_2, orient="vertical")
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.97, rely=0.1, relwidth=0.025, relheight=0.85,)
    
Aplicacao()