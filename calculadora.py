# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico con botón para cambiar texto

"""
#importamos las librerías necesarias
import sys
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz
from pathlib import Path

#Carga la interfaz gráfica y conecta los botones
class Ventana(QMainWindow):
    '''Esta es la clase principal'''
    #Inicializamos la ventana y conectamos los botones
    def __init__(self):
        ruta = Path.cwd()
        #Inicializa la ventana
        super(Ventana, self).__init__() # Reservamos un espacio en memoria para la clase
        
        uic.loadUi(f"{ruta}/Calculadora.ui",self) #Lee el archivo de Qtdesigner
        self.setWindowTitle("Calculadora") #Título de la ventana

        self.Cero.clicked.connect(self.cero)
        self.One.clicked.connect(self.one)
        self.Two.clicked.connect(self.two)
        self.Three.clicked.connect(self.three)
        self.Four.clicked.connect(self.four)
        self.Five.clicked.connect(self.five)
        self.Six.clicked.connect(self.six)
        self.Seven.clicked.connect(self.seven)
        self.Eight.clicked.connect(self.eight)
        self.Nine.clicked.connect(self.nine)
        self.Sum.clicked.connect(self.sum)
        self.Substract.clicked.connect(self.substract)
        self.Multiply.clicked.connect(self.multiply)
        self.Divide.clicked.connect(self.divide)
        self.Delete.clicked.connect(self.delete)
        self.Clear.clicked.connect(self.clear)
        self.Equal.clicked.connect(self.equal)
        self.Exp.clicked.connect(self.exp)
        self.Sqrt.clicked.connect(self.sqrt)
        self.P_left.clicked.connect(self.p_left)
        self.P_right.clicked.connect(self.p_right)
        self.Percent.clicked.connect(self.percent)
        self.Coma.clicked.connect(self.coma)
        self.Result.setText("0")

    def cero(self):
        self.Result.setText(self.Result.text() + "0")
    def one(self):  
        if self.Result.text() == "0" and len(self.Result.text()) == 1:
            self.Result.setText("1")
        else: 
            self.Result.setText() + "1"
    def two(self):
        if self.Result.text() == "0" and len(self.Result.text()) == 1:
            self.Result.setText("2")
        else:
            self.Result.setText(self.Result.text() + "2")
    def three(self):
        if self.Result.text() == "0" and len(self.Result.text()) == 1:
            self.Result.setText("3")
        else:
            self.Result.setText(self.Result.text() + "3")
    def four(self):
        if self.Result.text() == "0" and len(self.Result.text()) == 1:
            self.Result.setText("4")
        else:
            self.Result.setText(self.Result.text() + "4")
    def five(self):
        if self.Result.text() == "0" and len(self.Result.text()) == 1:
            self.Result.setText("5")
        else:
            self.Result.setText(self.Result.text() + "5")
    def six(self):
        if self.Result.text() == "0" and len(self.Result.text()) == 1:
            self.Result.setText("6")
        else:
            self.Result.setText(self.Result.text() + "6")
    def seven(self):    
        if self.Result.text() == "0" and len(self.Result.text()) == 1:
            self.Result.setText("7")
        else:
            self.Result.setText(self.Result.text() + "7")
    def eight(self):
        if self.Result.text() == "0" and len(self.Result.text()) == 1:
            self.Result.setText("8")
        else:
            self.Result.setText(self.Result.text() + "8")
    def nine(self):
        if self.Result.text() == "0" and len(self.Result.text()) == 1:
            self.Result.setText("9")
        else:
            self.Result.setText(self.Result.text() + "9")
    def sum(self):  
        if self.Result.text() != "0":
            self.Result.setText(self.Result.text() + "+")
    def substract(self):
        if self.Result.text() != "0":
            self.Result.setText(self.Result.text() + "-")
    def multiply(self):
        if self.Result.text() != "0":
            self.Result.setText(self.Result.text() + "*")
    def divide(self):
        if self.Result.text() != "0":
            self.Result.setText(self.Result.text() + "/")
    def delete(self):
        if len(self.Result.text()) == 1:
            self.Result.setText("0")
        else:
            self.Result.setText(self.Result.text()[:-1])
    def clear(self):
        self.Result.setText("0")
    def equal(self):
        try:
            self.Result.setText(str(eval(self.Result.text())))
        except:
            self.Result.setText("Error")    
    def exp(self):
        if self.Result.text() != "0":
            self.Result.setText(self.Result.text() + "^")
    def sqrt(self):
        if self.Result.text() != "0":
            self.Result.setText(self.Result.text() + "√")
    def p_left(self):
        self.Result.setText(self.Result.text() + "(")
    def p_right(self):
        self.Result.setText(self.Result.text() + ")")
    def percent(self):
        self.Result.setText(self.Result.text() + "%")
    def coma(self):
        self.Result.setText(self.Result.text() + ",")
     




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show()
    app.exec() 