import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Calculator')
        grid = QGridLayout()
        self.result = QLabel('0')  # 초기 결과값을 0으로 설정
        result_font = self.result.font()
        result_font.setPointSize(15)
        self.result.setFont(result_font)
        self.result.setStyleSheet("background-color:white")
        self.result.setFixedWidth(380)
        self.result.setAlignment(Qt.AlignRight)
        grid.addWidget(self.result, 0, 0, 1, 4)

        item_list = ['AC', '+/-', '%', '/', '7', '8', '9', 'X', '4', '5', '6', '-', '1', '2', '3', '+', '0', '.', '='] 
        positions = [(i+1, j) for i in range(5) for j in range(4)]
        k = 0
        for position, name in zip(positions, item_list):
            button = QPushButton(name)
            button.clicked.connect(self.button_click)
            if name == '0':
                grid.addWidget(button, position[0], position[1], 1, 2)  # '0' 버튼이 두 칸을 차지함
                k = 1
            else:
                grid.addWidget(button, position[0], position[1]+k)

        self.setLayout(grid)
        self.show()

    def button_click(self):
        sender = self.sender()
        current_text = self.result.text()
        button_text = sender.text()

        if button_text == 'AC':
            self.result.setText('0')
        elif button_text in {'+', '-', 'X', '/', '%', '+/-'}:
            if not current_text.endswith(button_text):
                self.result.setText(current_text + ' ' + button_text + ' ')
        elif button_text == '=':
            self.calculate_result()
        else:
            if current_text == '0':
                self.result.setText(button_text)
            else:
                self.result.setText(current_text + button_text)

    def calculate_result(self):
        try:
            expression = self.result.text().replace('X', '*')
            result = eval(expression)
            self.result.setText(str(result))
        except Exception as e:
            self.result.setText('Error')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
