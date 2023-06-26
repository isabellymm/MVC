
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import tkinter as tk
import matplotlib 
import matplotlib.pyplot as plt


matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)



matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


jnla = Tk()
estilo = ttk.Style()

class Aplicacao(tk.Tk):

    def __init__(self) :
        self.jnla = jnla
        self.estilo = estilo
        self.frames_da_tela()
        self.tela_4()
        self.widgets_frame4()
        self.grafico()
        

        jnla.mainloop()

    def frames_da_tela(self):
        self.frame_4 = Frame(self.jnla, bd=1, bg="#BEBEBE", highlightbackground="#A9A9A9", highlightthickness=4)
        self.frame_4.place(relx=0.02 , rely=0.02 , relwidth=0.96 , relheight=0.95)

    def tela_4(self):
        self.jnla
        self.jnla.title("Gerenciamento Pessoal")
        self.jnla.configure(background="#757575")
        self.jnla.geometry('800x600')
        self.jnla.resizable(True,True)
        self.jnla.maxsize(width=1550, height=900)
        self.jnla.minsize(width=1200, height=700)

    def widgets_frame4(self):
        
        self.text_despesas = Label(self.frame_4, bd= 2, background="#CC3333", text = "DESPESAS", relief="flat")
        self.text_despesas.place(relx=0.015 , rely=0.13, relwidth=0.22 , relheight=0.1)
      
        self.tabela = ttk.Treeview(self.frame_4, height=5,selectmode="browse", column=("column1", "column2") , show="headings")
        self.tabela.heading("#1", text="Despesas")
        self.tabela.column("column1", width=1)
        self.tabela.heading("#2", text="Valor")
        self.tabela.column("column2", width=25)

        self.text_renda = Label(self.frame_4, bd= 2, background="#0088DE", text = "RENDAS", relief="flat")
        self.text_renda.place(relx=0.3 , rely=0.13, relwidth=0.22 , relheight=0.1)
      
        self.tabela2 = ttk.Treeview(self.frame_4, height=5,selectmode="browse", column=("column1", "column2") , show="headings")
        self.tabela2.heading("#1", text="Renda")
        self.tabela2.column("column1", width=1)
        self.tabela2.heading("#2", text="Valor")
        self.tabela2.column("column2", width=25)

        self.tabela.place(relx=0.015 , rely=0.22, relwidth=0.22, relheight=0.6)
        self.tabela2.place(relx=0.3 , rely=0.22, relwidth=0.22, relheight=0.6)


        self.bt_cadastar = Button(self.frame_4, text="Alterar",bg="#0088DE" ,fg="white", relief="flat") 
        self.bt_cadastar.place(relx=0.8, rely=0.85, relwidth=0.15, relheight=0.07)


    def grafico(self):
  
        # the figure that will contain the plot
        fig = Figure(figsize = (6.4, 4.8), dpi = 10)

        # list of squares
        y = [i**2 for i in range(101)]
    
        # adding the subplot
        plot1 = fig.add_subplot(111)
    
        # plotting the graph
        plot1.plot(y)
    
        # creating the Tkinter canvas
        # containing the Matplotlib figure

        canvas = FigureCanvasTkAgg(fig,master = self.jnla)  
        canvas.draw()
     
    
        # placing the canvas on the Tkinter jnla
        canvas.get_tk_widget().pack()
    
        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,self.jnla)
        toolbar.update()
    
        # placing the toolbar on the Tkinter jnla
        canvas.get_tk_widget().pack()

    

  






        #self.scroolLista = Scrollbar(self.frame_4, orient="vertical")
        #self.listaCli.configure(yscroll=self.scroolLista.set)
        #self.scroolLista.place(relx=0.97, rely=0.1, relwidth=0.025, relheight=0.85)


Aplicacao()

