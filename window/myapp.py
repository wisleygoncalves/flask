import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton
from process import Worker

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.list_widget = QListWidget()
        self.layout.addWidget(self.list_widget)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.startProcess)
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)
        self.setWindowTitle('Real-time Output')
        self.show()

    def appendToList(self, message):
        self.list_widget.addItem(message)
        self.list_widget.scrollToBottom() 

    def startProcess(self):
        # Aqui você pode abrir uma janela de diálogo para selecionar o arquivo e obter o path
        path = "/caminho/para/seu/arquivo"

        self.worker = Worker(path)
        self.worker.message_signal.connect(self.appendToList)
        self.worker.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())