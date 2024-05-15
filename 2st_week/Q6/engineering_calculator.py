import sys
import math
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import Qt

class Calculator:
    def __init__(self):
        self.reset()

    def reset(self):
        self.current = '0'
        self.operator = None
        self.operand = None
        self.waiting_for_operand = True

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return 'Error'
        return a / b

    def negative_positive(self):
        if self.current.startswith('-'):
            self.current = self.current[1:]
        else:
            self.current = '-' + self.current

    def percent(self):
        self.current = str(float(self.current) / 100)

    def append_digit(self, digit):
        if self.waiting_for_operand:
            self.current = digit
            self.waiting_for_operand = False
        elif digit == '.' and '.' in self.current:
            pass
        else:
            self.current += digit

    def set_operator(self, op):
        if not self.waiting_for_operand:
            self.equal()
        self.operator = op
        self.operand = float(self.current)
        self.waiting_for_operand = True

    def equal(self):
        if self.operator and not self.waiting_for_operand:
            operand2 = float(self.current)
            if self.operator == '+':
                result = self.add(self.operand, operand2)
            elif self.operator == '-':
                result = self.subtract(self.operand, operand2)
            elif self.operator == '*':
                result = self.multiply(self.operand, operand2)
            elif self.operator == '/':
                result = self.divide(self.operand, operand2)
            self.current = str(result)
            self.operand = None
            self.operator = None
            self.waiting_for_operand = True

class EngineeringCalculator(Calculator):
    def __init__(self):
        super().__init__()
        self.memory = 0
        self.in_degrees = True

    def memory_clear(self):
        self.memory = 0

    def memory_recall(self):
        self.current = str(self.memory)

    def memory_add(self):
        self.memory += float(self.current)

    def memory_subtract(self):
        self.memory -= float(self.current)

    def toggle_deg_rad(self):
        self.in_degrees = not self.in_degrees

    def factorial(self):
        n = int(float(self.current))
        if n < 0:
            self.current = 'Error'
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            self.current = str(result)

    def exp(self):
        self.current = str(math.exp(float(self.current)))

    def exp10(self):
        self.current = str(math.pow(10, float(self.current)))

    def ln(self):
        value = float(self.current)
        if value <= 0:
            self.current = 'Error'
        else:
            self.current = str(math.log(value))

    def log10(self):
        value = float(self.current)
        if value <= 0:
            self.current = 'Error'
        else:
            self.current = str(math.log10(value))

    def random_number(self):
        self.current = str(random.random())

    def reciprocal(self):
        value = float(self.current)
        if value == 0:
            self.current = 'Error'
        else:
            self.current = str(1 / value)

    def sqrt(self):
        value = float(self.current)
        if value < 0:
            self.current = 'Error'
        else:
            self.current = str(math.sqrt(value))

    def cbrt(self):
        self.current = str(math.pow(float(self.current), 1/3))

    def nth_root(self, n):
        base = float(self.current)
        if base < 0 and n % 2 == 0:
            self.current = 'Error'
        else:
            self.current = str(base ** (1/n))

    def power_y(self, y):
        base = float(self.current)
        self.current = str(math.pow(base, y))

    def sin(self):
        value = float(self.current)
        if self.in_degrees:
            value = math.radians(value)
        self.current = str(math.sin(value))

    def cos(self):
        value = float(self.current)
        if self.in_degrees:
            value = math.radians(value)
        self.current = str(math.cos(value))

    def tan(self):
        value = float(self.current)
        if self.in_degrees:
            value = math.radians(value)
        self.current = str(math.tan(value))

    def sinh(self):
        self.current = str(math.sinh(float(self.current)))

    def cosh(self):
        self.current = str(math.cosh(float(self.current)))

    def tanh(self):
        self.current = str(math.tanh(float(self.current)))

    def pi(self):
        self.current = str(math.pi)
    
    
    def no_op(self):
        pass  # Placeholder for buttons without defined functions yet

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.calculator = EngineeringCalculator()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Engineering Calculator')
        grid = QGridLayout()
        self.result = QLabel(self.calculator.current)
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
            '(': self.calculator.no_op, ')': self.calculator.no_op,
            'mc': self.calculator.memory_clear, 'm+': self.calculator.memory_add,
            'm-': self.calculator.memory_subtract, 'mr': self.calculator.memory_recall,
            'C': self.calculator.reset, '+/-': self.calculator.negative_positive, '%': self.calculator.percent, '/': lambda: self.calculator.set_operator('/'),
            '2nd': self.calculator.no_op, 'x^2': lambda: self.calculator.power_y(2), 'x^3': lambda: self.calculator.power_y(3), 'x^y': lambda: self.calculator.power_y(y), 'e^x': self.calculator.exp, '10^x': self.calculator.exp10,
            '7': lambda: self.calculator.append_digit('7'), '8': lambda: self.calculator.append_digit('8'), '9': lambda: self.calculator.append_digit('9'), '*': lambda: self.calculator.set_operator('*'),
            '1/x': self.calculator.reciprocal, 'sqrt(x)': self.calculator.sqrt, 'cbrt(x)': self.calculator.cbrt, 'yroot': lambda: self.calculator.nth_root(y), 'ln': self.calculator.ln, 'log10': self.calculator.log10,
            '4': lambda: self.calculator.append_digit('4'), '5': lambda: self.calculator.append_digit('5'), '6': lambda: self.calculator.append_digit('6'), '-': lambda: self.calculator.set_operator('-'),
            'x!': self.calculator.factorial, 'sin': self.calculator.sin, 'cos': self.calculator.cos, 'tan': self.calculator.tan, 'e': lambda: self.calculator.append_digit(math.e), 'EE': self.calculator.no_op,
            '1': lambda: self.calculator.append_digit('1'), '2': lambda: self.calculator.append_digit('2'), '3': lambda: self.calculator.append_digit('3'), '+': lambda: self.calculator.set_operator('+'),
            'Rad': self.calculator.toggle_deg_rad, 'sinh': self.calculator.sinh, 'cosh': self.calculator.cosh, 'tanh': self.calculator.tanh, 'pi': self.calculator.pi, 'Rand': self.calculator.random_number,
            '0': lambda: self.calculator.append_digit('0'), '.': lambda: self.calculator.append_digit('.'), '=': self.calculator.equal
        }
        k = 0
        positions = [(i // 10 + 1, i % 10) for i in range(len(button_order))]
        for pos, name in zip(positions, button_order):
            button = QPushButton(name)
            button.clicked.connect(self.make_connection(buttons.get(name, self.calculator.no_op)))
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

    def update_display(self):
        self.result.setText(self.calculator.current)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
