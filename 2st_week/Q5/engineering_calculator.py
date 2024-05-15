import sys
import math
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Engineering Calculator')
        grid = QGridLayout()
        self.result = QLabel("0")
        self.result.setAlignment(Qt.AlignRight)
        self.result.setFixedWidth(1000)
        grid.addWidget(self.result, 0, 0, 1, 10)

        button_order = [
            '(', ')', 'mc', 'm+', 'm-', 'mr', 'C', '+/-', '%', '/',
            '2nd', 'x^2', 'x^3', 'x^y', 'e^x', '10^x', '7', '8', '9', '*',
            '1/x', 'sqrt(x)', 'cbrt(x)', 'yroot', 'ln', 'log10', '4', '5', '6', '-',
            'x!', 'sin', 'cos', 'tan', 'e', 'EE', '1', '2', '3', '+',
            'Rad', 'sinh', 'cosh', 'tanh', 'pi', 'Rand', '0', '.', '='
        ]

        buttons = {
            '(', ')', 'mc', 'm+', 'm-', 'mr', 'C', '+/-', '%', '/',
            '2nd', 'x^2', 'x^3', 'x^y', 'e^x', '10^x', '7', '8', '9', '*',
            '1/x', 'sqrt(x)', 'cbrt(x)', 'yroot', 'ln', 'log10', '4', '5', '6', '-',
            'x!', 'sin', 'cos', 'tan', 'e', 'EE', '1', '2', '3', '+',
            'Rad', 'sinh', 'cosh', 'tanh', 'pi', 'Rand', '0', '.', '=' }
        k = 0
        positions = [(i // 10 + 1, i % 10) for i in range(len(button_order))]
        for pos, name in zip(positions, button_order):
            button = QPushButton(name)
            if name == '0':
                grid.addWidget(button, pos[0], pos[1],1,2)
                k = 1
            else:
                grid.addWidget(button, pos[0], pos[1] + k)
        
        self.setLayout(grid)
        self.show()

    def make_connection(self, command):
        def command_func():
            command()
            self.update_display()
        return command_func



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
