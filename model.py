class Model():
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operacao = 0
        


    def calcular(self):
        if self.operacao == 1:
            return self.num1 + self.num2
        if self.operacao == 2:
            return self.num1 - self.num2
        if self.operacao == 3:
            return self.num1 * self.num2
        if self.operacao == 4:
            return self.num1 / self.num2
        else:
            return 0
    
    def set_num1(self,num1):
        self.num1 = num1
    
    def set_num2(self,num2):
        self.num2 = num2
    
    def set_operacao(self, operacao):
        self.operacao = operacao
        
        
        