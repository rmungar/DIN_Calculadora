# -*- coding: utf-8 -*-
"""
Ejemplo de ventana básico con botón para cambiar texto

"""
#importamos las librerías necesarias
import sys
from PyQt6.QtWidgets import * # Librerías de los componentes
from PyQt6 import uic  # Librería para trabajar con el archivo de la interfaz
from PyQt6.QtCore import Qt
from pathlib import Path
import re
import math as Math

#Carga la interfaz gráfica y conecta los botones
class Ventana(QMainWindow):
    '''Esta es la clase principal'''
    operation_id = 1 
    #Inicializamos la ventana y conectamos los botones
    def __init__(self):
        ruta = Path.cwd()
        #Inicializa la ventana
        super(Ventana, self).__init__() # Reservamos un espacio en memoria para la clase
        
        self.isResult = False

        uic.loadUi(f"{ruta}/Calculadora.ui",self) #Lee el archivo de Qtdesigner
        self.setWindowTitle("Calculadora") #Título de la ventana

        self.history = dict()

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
        self.ClearH.clicked.connect(self.clearHistory)
        self.Equal.clicked.connect(self.equal)
        self.Exp.clicked.connect(self.exp)
        self.Sqrt.clicked.connect(self.sqrt)
        self.P_left.clicked.connect(self.p_left)
        self.P_right.clicked.connect(self.p_right)
        self.Percent.clicked.connect(self.percent)
        self.Coma.clicked.connect(self.coma)
        self.Factorial.clicked.connect(self.factorial)
        self.Log.clicked.connect(self.log)
        self.Ln.clicked.connect(self.ln)
        self.Pi.clicked.connect(self.pi)
        self.Result.setText("0")
        


    def comprobarErr(self) -> bool:
        if self.Result.text() == "Err":
            return True
        else:
            return False

    def comprobarResult(self) -> bool:
        if self.isResult:
            return True
        else:
            return False

    def cero(self):
        if self.comprobarErr() or self.Result.text() == "0" or self.comprobarResult():
            self.Result.setText("0")
            self.isResult = False
        else:
            self.Result.setText(self.Result.text() + "0")

    def one(self): 
        if  self.Result.text() == "0" or self.comprobarErr() or self.comprobarResult():
            self.Result.setText("1")
            self.isResult = False
        else: 
            self.Result.setText(self.Result.text() + "1")

    def two(self):
        if  self.Result.text() == "0" or self.comprobarErr() or self.comprobarResult():
            self.Result.setText("2")
            self.isResult = False
        else:
            self.Result.setText(self.Result.text() + "2")

    def three(self):
        if  self.Result.text() == "0" or self.comprobarErr() or self.comprobarResult():
            self.Result.setText("3")
            self.isResult = False
        else:
            self.Result.setText(self.Result.text() + "3")

    def four(self):
        if  self.Result.text() == "0" or self.comprobarErr() or self.comprobarResult():
            self.Result.setText("4")
            self.isResult = False
        else:
            self.Result.setText(self.Result.text() + "4")

    def five(self):
        if  self.Result.text() == "0" or self.comprobarErr() or self.comprobarResult():
            self.Result.setText("5")
            self.isResult = False
        else:
            self.Result.setText(self.Result.text() + "5")

    def six(self):
        if  self.Result.text() == "0" or self.comprobarErr() or self.comprobarResult():
            self.Result.setText("6")
            self.isResult = False
        else:
            self.Result.setText(self.Result.text() + "6")

    def seven(self):    
        if  self.Result.text() == "0" or self.comprobarErr() or self.comprobarResult():
            self.Result.setText("7")
            self.isResult = False
        else:
            self.Result.setText(self.Result.text() + "7")

    def eight(self):
        if  self.Result.text() == "0" or self.comprobarErr() or self.comprobarResult():
            self.Result.setText("8")
            self.isResult = False
        else:
            self.Result.setText(self.Result.text() + "8")

    def nine(self):
        if  self.Result.text() == "0" or self.comprobarErr() or self.comprobarResult():
            self.Result.setText("9")
            self.isResult = False
        else:
            self.Result.setText(self.Result.text() + "9")

    def sum(self):  
        if self.Result.text() != "0" and not self.comprobarErr() and not self.comprobarResult():
            self.Result.setText(self.Result.text() + "+")
            self.isResult = False

    def substract(self):
        if self.Result.text() != "0" and not self.comprobarErr() and not self.comprobarResult():
            self.Result.setText(self.Result.text() + "-")
            self.isResult = False

    def multiply(self):
        if self.Result.text() != "0" and not self.comprobarErr() and not self.comprobarResult():
            self.Result.setText(self.Result.text() + "x")
            self.isResult = False

    def divide(self):
        if self.Result.text() != "0" and  not self.comprobarErr() and not self.comprobarResult():
            self.Result.setText(self.Result.text() + "/")
            self.isResult = False

    def delete(self):
        if  self.Result.text() == "0" or self.comprobarErr() or len(self.Result.text()) == 1 or self.comprobarResult(): 
            self.Result.setText("0")
            self.isResult = False
        else:
            self.Result.setText(self.Result.text()[:-1])
        
    def clear(self):
        self.Result.setText("0")

    def clearHistory(self):
        self.History.setRowCount(0)
        self.History.setColumnCount(0)
        self.history.clear()
        self.operation_id = 1

    def equal(self):

        current_text = self.Result.text()
        if current_text == "":
            self.Result.setText("")
        else:
            try:
                expr = current_text.replace("x", "*").replace("÷", "/").replace(",", ".").replace("π", f"{Math.pi}").replace("^", "**")
                while "√" in expr:
                    expr = re.sub(r"√(\d+)", r"(\1**0.5)", expr)  

                while "!" in expr:
                    expr = re.sub(r"(\d+)!", r"Math.factorial(\1)", expr)

                while "log" in expr:
                    expr = re.sub(r"log\((\d+(\.\d+)?)\)", lambda m: str(Math.log10(float(m.group(1)))), expr)
                while "ln" in expr:
                    expr = re.sub(r"ln\((\d+(\.\d+)?)\)", lambda m: str(Math.log(float(m.group(1)))), expr)

                result = eval(expr)

                
                if abs(result) > 1e6 or (0 < abs(result) < 1e-3):  # Números grandes o pequeños
                    formatted_result = "{:.2e}".format(result)  # Notación científica
                else:
                    formatted_result = "{:.2f}".format(result)  # Máximo 2 decimales
                
                self.Result.setText(formatted_result)

                # 🔹 Guardar en historial con formato correcto
                self.history[current_text] = formatted_result.replace(".", ",")
                self.saveOnTable(current_text, formatted_result.replace(".", ","))
                self.operation_id += 1

            except Exception as e:
                self.Result.setText("Err")
                print(e)
    
    def exp(self):
        if self.Result.text() != "0" and not self.comprobarErr() and not self.comprobarResult():
            self.Result.setText(self.Result.text() + "^")

    def sqrt(self):
        if self.Result.text() != "0" and not self.comprobarErr() and not self.comprobarResult():
            self.Result.setText(self.Result.text() + "√")
        elif self.Result.text() == "0" or self.comprobarErr() or self.comprobarResult():
            self.Result.setText("√")
            self.isResult = False

    def p_left(self):
        if not self.comprobarErr() and self.Result.text() != "0" and not self.comprobarResult():
            self.Result.setText(self.Result.text() + "(")
        else:
            self.Result.setText("(")
            self.isResult = False

    def p_right(self):
        if not self.comprobarErr() and self.Result.text() != "0" and not self.comprobarResult():
            self.Result.setText(self.Result.text() + ")")
        else:
            self.Result.setText(")")
            self.isResult = False

    def percent(self):
        if self.Result.text() != "0" and not self.comprobarErr() and not self.comprobarResult():
            self.Result.setText(self.Result.text() + "%")

    def coma(self):
        current_text = self.Result.text()

        signos = ["+", "-", "x", "÷"]
        # Verificar si el texto contiene algún operador
        if any(signo in current_text for signo in signos):
            operandos = [op.strip() for op in re.split(r"[+\-×÷]", current_text)]
            if operandos and "," not in operandos[-1]:  # Evitar más de un punto decimal en un número
                self.Result.setText(current_text + ",")
        elif current_text == "" or self.comprobarErr() or self.comprobarResult():
            self.Result.setText("0,")
        elif "," in current_text.split(signos[-1])[-1]:  # Último número ya tiene coma
            self.Result.setText(current_text)
        else:
            self.Result.setText(current_text + ",")
     


    def factorial(self):
        if self.Result.text() != "0" and not self.comprobarErr() and not self.comprobarResult():
            self.Result.setText(self.Result.text() + "!")

    def log(self):
        if self.Result.text() != "0" and not self.comprobarErr() and not self.comprobarResult():
            self.Result.setText(self.Result.text() + "log(")
        else:
            self.Result.setText("log(")
            self.isResult = False

    def ln(self):
        if self.Result.text() != "0" and not self.comprobarErr() and not self.comprobarResult():
            self.Result.setText(self.Result.text() + "ln(")
        else:
            self.Result.setText("ln(")
            self.isResult = False
    
    def pi(self):
        if self.Result.text() != "0" and not self.comprobarErr() and not self.comprobarResult():
            self.Result.setText(self.Result.text() + "π")
        else:
            self.Result.setText("π")
            self.isResult = False


    def saveOnTable(self, operacion, resultado):
        row_position = self.History.rowCount()
        self.History.insertRow(row_position)

        # Asegurar que solo se configuren las columnas una vez (evita duplicados)
        if self.History.columnCount() == 0:
            self.History.setColumnCount(2)
            self.History.setHorizontalHeaderLabels(["Operación", "Resultado"])  # Encabezados de columna
            self.History.resizeRowsToContents()
            self.History.resizeColumnsToContents()

        # Crear los elementos de celda con alineación centrada
        item_operacion = QTableWidgetItem(operacion)
        item_operacion.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        item_resultado = QTableWidgetItem(resultado)
        item_resultado.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        # Agregar los items a la tabla
        self.History.setItem(row_position, 0, item_operacion)  # Operación
        self.History.setItem(row_position, 1, item_resultado) 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ventana()
    window.show()
    app.exec() 