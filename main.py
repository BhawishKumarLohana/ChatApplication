import socket
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QInputDialog
import sys


class ChatClient(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("C++ Server Chat")
        self.resize(400, 500)

        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)

        self.message_input = QLineEdit()
        self.send_button = QPushButton("Send")

        layout = QVBoxLayout()
        layout.addWidget(self.chat_display)
        layout.addWidget(self.message_input)
        layout.addWidget(self.send_button)
        self.setLayout(layout)

        self.send_button.clicked.connect(self.send_message)
        self.message_input.returnPressed.connect(self.send_message)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connect_to_server()

    def connect_to_server(self):
        try:
            self.client_socket.connect(('127.0.0.1', 50000))
        except Exception as e:
            self.chat_display.append(f"Connection error: {e}")
            return

        username, ok = QInputDialog.getText(self, "Username", "Enter your username:")
        if ok and username:
            self.client_socket.send(username.encode())
            threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_message(self):
        msg = self.message_input.text()
        if msg:
            self.client_socket.send(msg.encode())
            self.message_input.clear()

    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode()
                if msg:
                    self.chat_display.append(msg)
            except:
                self.chat_display.append("Disconnected from server.")
                break


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatClient()
    window.show()
    sys.exit(app.exec_())
