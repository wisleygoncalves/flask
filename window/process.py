from PyQt5.QtCore import QThread, pyqtSignal
import tombamento

class Worker(QThread):
    message_signal = pyqtSignal(str)

    def __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        messages = tombamento.tombamento_safra(self.path)
        if messages:
            for message in messages:
                self.message_signal.emit(message)