"""Criar um aplicativo de lista de tarefas que permite adicionar, 
editar e excluir tarefas. A visão deve exibir a lista de tarefas e 
permitir a entrada do usuário, enquanto o modelo deve armazenar a 
lista de tarefas e permitir a edição dos itens. O controlador deve coordenar 
a comunicação entre a visão e o modelo.
"""


class Model():
    def __init__(self):
        self.excluir = ""
        self.alterar = ""
        self.texto =""


    def alteracao(self):
        if self.alterar == "S" or self.alterar =="s":
            self.texto = input("")

        if self.excluir == "S"  or self.excluir =="s":
            self.texto = ""
            print("Texto excluido")

        else:
            print("Escolha uma opção válida")


    def set_excluir(self,excluir):
            self.set_excluir = excluir

            
    def set_alterar(self,alterar):
        self.set_alterar= alterar

            
    def set_texto(self,texto):
        self.set_texto = texto



class Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model

    
    def alterar_texto(self):

        excluir = self.view.get_excluir()
        altera = self.view.get_alterar()
        texto = self.view.get_texto()

        self.model.set_excluir(excluir)
        self.model.set_alterar(altera)
        self.model.set_texto(texto)

        resultado = self.model.alterar_texto()
        self.view.mostrar_resultado(resultado)



class View():
    def get_texto(self):

        return input("Digite uma palavra")
    
    def get_alterar(self):
        return input("Deseja alterar ?")
    
    def get_excluir(self):
        return input("Deseja excluir ?")
    

# Programa principal
if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(view, model)

    while True:
        controller.alterar_texto()
