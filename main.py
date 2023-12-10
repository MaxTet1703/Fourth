import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QTextBrowser


class VirtualKeyboard(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.textEdit = QLineEdit()
        self.textBrowser = QTextBrowser()
        self.textBrowser.setFixedHeight(100)

        keyboardLayout = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M'],
            ['Готово']
        ]

        for row in keyboardLayout:
            rowLayout = QHBoxLayout()
            for key in row:
                keyButton = QPushButton(key)
                keyButton.clicked.connect(lambda checked, key=key: self.on_key_click(key))
                rowLayout.addWidget(keyButton)
            self.layout.addLayout(rowLayout)

        self.layout.addWidget(self.textBrowser)
        self.layout.addWidget(self.textEdit)

        self.setLayout(self.layout)

    def on_key_click(self, key):
        if key == 'Готово':
            clipboard = QApplication.clipboard()
            clipboard.setText(self.textEdit.text())
            self.textBrowser.setText("Текст успешно скопирован в буфер обмена")
        else:
            self.textEdit.setText(self.textEdit.text() + key)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VirtualKeyboard()
    window.setWindowTitle('Виртуальная клавиатура')
    window.show()
    sys.exit(app.exec_())