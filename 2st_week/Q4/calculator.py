import sys
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

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.calculator = Calculator()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Calculator')
        grid = QGridLayout()
        self.result = QLabel(self.calculator.current)
        self.result.setAlignment(Qt.AlignRight)
        self.result.setFixedWidth(380)
        grid.addWidget(self.result, 0, 0, 1, 4) # 결과 창

        buttons = { # 버튼
            'AC': self.calculator.reset, '+/-': self.calculator.negative_positive, 
            '%': self.calculator.percent, '/': lambda: self.calculator.set_operator('/'), 
            '7': lambda: self.calculator.append_digit('7'), '8': lambda: self.calculator.append_digit('8'), 
            '9': lambda: self.calculator.append_digit('9'), 'X': lambda: self.calculator.set_operator('*'), 
            '4': lambda: self.calculator.append_digit('4'), '5': lambda: self.calculator.append_digit('5'), 
            '6': lambda: self.calculator.append_digit('6'), '-': lambda: self.calculator.set_operator('-'), 
            '1': lambda: self.calculator.append_digit('1'), '2': lambda: self.calculator.append_digit('2'), 
            '3': lambda: self.calculator.append_digit('3'), '+': lambda: self.calculator.set_operator('+'), 
            '0': lambda: self.calculator.append_digit('0'), '.': lambda: self.calculator.append_digit('.'), 
            '=': self.calculator.equal
        }
        k = 0
        positions = [(i+1, j) for i in range(5) for j in range(4)] #버튼이 위치할 위치 값
        for pos, name in zip(positions, buttons.keys()):
            button = QPushButton(name)
            button.clicked.connect(self.make_connection(buttons[name]))
            if name == '0': # 0이라면 2칸을 차지해야함
                grid.addWidget(button, pos[0], pos[1], 1, 2)
                k = 1
            else:
                grid.addWidget(button, pos[0], pos[1] + k)
        
        self.setLayout(grid)
        self.show()

    def make_connection(self, command): # 버튼 클릭 이멘트 연결 함수
        def command_func():
            command()
            self.update_display()
        return command_func

    def update_display(self):
        self.result.setText(self.calculator.current) # 현재 값을 보여줌

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
