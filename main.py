from model import Model
from view import View
from controller import Controller

if __name__ == "__main__":
    model = Model()
    view = View()
    controller = Controller(View, Model)

    while True:
        controller.calcular()