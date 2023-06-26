# Modelo (Model)
class Calculadora:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operacao = ""

    def calcular(self):
        if self.operacao == "+":
            return self.num1 + self.num2
        elif self.operacao == "-":
            return self.num1 - self.num2
        elif self.operacao == "*":
            return self.num1 * self.num2
        elif self.operacao == "/":
            return self.num1 / self.num2
        else:
            return 0

    def set_num1(self, num1):
        self.num1 = num1

    def set_num2(self, num2):
        self.num2 = num2

    def set_operacao(self, operacao):
        self.operacao = operacao


# Controlador (Controller)
class CalculadoraController:
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def calcular(self):
        num1 = self.view.get_num1()
        num2 = self.view.get_num2()
        operacao = self.view.get_operacao()
        self.model.set_num1(num1)
        self.model.set_num2(num2)
        self.model.set_operacao(operacao)
        resultado = self.model.calcular()
        self.view.mostrar_resultado(resultado)


# Visualização (View)
class CalculadoraView:
    def get_num1(self):
        return float(input("Digite o primeiro valor: "))

    def get_num2(self):
        return float(input("Digite o segundo valor: "))

    def get_operacao(self):
        return input("Digite a operação (+, -, *, /): ")

    def mostrar_resultado(self, resultado):
        print("Resultado: ", resultado)


# Programa principal
if __name__ == "__main__":
    model = Calculadora()
    view = CalculadoraView()
    controller = CalculadoraController(view, model)

    while True:
        controller.calcular()
