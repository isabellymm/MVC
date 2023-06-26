class View():

    def get_num1(self):
        return float(input("Digite o 1 numero"))
    
    def get_num2(self):
        return float(input("Digite o 2 numero"))
    
    def get_operacao(self):
        return input("Digite a operacao 1- soma \*  2- sub /* 3-div /* 4- mult ")
    
    def mostrar_resultado(self, resultado):
        print("Resultado: ", resultado)