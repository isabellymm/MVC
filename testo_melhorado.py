

class Model():
    def __init__(self):
        self.texto = ""

    def alterar_texto(self, novo_texto):
        self.texto = novo_texto

    def  excluir_texto(self):
        self.texto = ""
        print("Texto excluido")

    def obter_texto(self):
        return self.texto
    

class Controller:
    def __init__(self,view,model):
        self.view = view
        self.model = model
    

    def alterar_texto(self):
        novo_texto = self.view.get_texto()
        self.model.alterar_texto(novo_texto)
        self.view.mostrar_resultado("Texto alterado : " + novo_texto + "\n")

    def excluir_texto(self):
        self.model.excluir_texto()
        self.view.mostrar_resultado("Texto excluído \n")

    def executar(self):
        while True:
            opcao = self.view.get_opcao()
            if opcao == "1":
                self.alterar_texto()
            if opcao == "2":
                self.excluir_texto()
            if opcao == "3":
                break



class View():
    def get_texto(self):
        return input("Digite um texto: ")
    
    def get_opcao(self):
        return input("Escolha uma opção:\n1 - Alterar texto\n2 - Excluir texto\n3 - Sair\n")
    
    def mostrar_resultado(self,resultado):
        print(resultado)


if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(view, model)
    controller.executar()
