from model import Model
from view import View

class Controller():
    def __init__(self,view,model):
        self.model = Model()
        self.view = View()

    def calcular(self, view, model):
        num1 = self.view.get_num1()
        num2 = self.view.get_num2()
        operacao = self.view.get_opracao()


        self.model.set_num1(num1)
        self.model.set_num2(num2)
        self.model.set_operacao(operacao)

        result = self.model.calcular()
        self.view.mostrar_resultado(result)

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(view, model)

    while True:
        controller.calcular()