from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QListWidgetItem, QHBoxLayout, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lista con Botones")
        self.setGeometry(100, 100, 400, 400)

        # Crear lista (QListWidget)
        self.list_widget = QListWidget()

        # Botón para agregar elementos
        self.add_button = QPushButton("Agregar Elemento con Botón")
        self.add_button.clicked.connect(self.add_item)

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_item(self):
        """ Agrega un nuevo elemento con un botón dentro de la lista """
        item_widget = QWidget()  # Widget contenedor del elemento

        # Layout para el elemento
        item_layout = QHBoxLayout()
        item_layout.setContentsMargins(5, 5, 5, 5)

        # Crear botón dentro del elemento
        button = QPushButton("Acción")
        button.clicked.connect(lambda: self.button_action(button))  # Conectar a función

        # Agregar el botón al layout del item
        item_layout.addWidget(button)
        item_widget.setLayout(item_layout)

        # Crear el item de la lista
        list_item = QListWidgetItem(self.list_widget)
        list_item.setSizeHint(item_widget.sizeHint())  # Ajustar tamaño del item

        # Agregar el widget personalizado al item de la lista
        self.list_widget.addItem(list_item)
        self.list_widget.setItemWidget(list_item, item_widget)

    def button_action(self, button):
        """ Acción del botón dentro de la lista """
        print("¡Botón dentro de la lista presionado!")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
