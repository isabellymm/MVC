from tkinter import *
from tkinter import ttk

jnla = Tk()

class Aplicacao():

    def __init__(self) :
        self.jnla = jnla
        self.frames_da_tela()
        self.tela_3()
        self.widgets_frame3()

        jnla.mainloop()

    def frames_da_tela(self):
        self.frame_3 = Frame(self.jnla, bd=1, bg="#BEBEBE", highlightbackground="#A9A9A9", highlightthickness=4)
        self.frame_3.place(relx=0.02 , rely=0.02 , relwidth=0.96 , relheight=0.95)

    def tela_3(self):
        self.jnla
        self.jnla.title("Meses")
        self.jnla.configure(background="#757575")
        self.jnla.geometry('800x600')
        self.jnla.resizable(True,True)
        self.jnla.maxsize(width=900, height=600)
        self.jnla.minsize(width=700, height=600)
   
    def widgets_frame3(self):

        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho","Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

        y = 0.05
        i=0
        aux_1 = 0
 

        while i < 6:
            self.bt_meses = Button(self.frame_3, text=(meses[0+aux_1]), bg="#0088DE" ,fg="white", relief="flat") 
            self.bt_meses.place(relx=0.15, rely=y, relwidth=0.2, relheight=0.09)

            self.bt_meses = Button(self.frame_3, text=(meses[6+aux_1]),bg="#0088DE" ,fg="white", relief="flat") 
            self.bt_meses.place(relx=0.65, rely=y, relwidth=0.2, relheight=0.09)

            y += 0.15
            i += 1
            aux_1 += 1
   
      


    
Aplicacao()