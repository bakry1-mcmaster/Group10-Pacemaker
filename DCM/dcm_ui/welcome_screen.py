# dcm_ui/welcome_screen.py
# - UI for login and registration.
# - Checks if max 10 users are already registered.
# - Passes user info to user_manager.py.

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTabWidget
)
from dcm_core.user_manager import UserManager

class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Device Controller Monitor - Welcome")
        self.user_manager = UserManager()

        layout = QVBoxLayout()

        # Title
        title = QLabel("Welcome to the DCM")
        layout.addWidget(title)

        # Tabs for Login / Register
        tabs = QTabWidget()
        tabs.addTab(self.login_tab(), "Login")
        tabs.addTab(self.register_tab(), "Register")

        layout.addWidget(tabs)
        self.setLayout(layout)

    def login_tab(self):
        """Creates the Login form"""
        widget = QWidget()
        layout = QVBoxLayout()

        self.login_user = QLineEdit()
        self.login_user.setPlaceholderText("Username")
        layout.addWidget(self.login_user)

        self.login_pass = QLineEdit()
        self.login_pass.setPlaceholderText("Password")
        self.login_pass.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.login_pass)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        widget.setLayout(layout)
        return widget

    def register_tab(self):
        """Creates the Register form"""
        widget = QWidget()
        layout = QVBoxLayout()

        self.register_user = QLineEdit()
        self.register_user.setPlaceholderText("New Username")
        layout.addWidget(self.register_user)

        self.register_pass = QLineEdit()
        self.register_pass.setPlaceholderText("New Password")
        self.register_pass.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.register_pass)

        register_button = QPushButton("Register")
        register_button.clicked.connect(self.handle_register)
        layout.addWidget(register_button)

        widget.setLayout(layout)
        return widget

    def handle_login(self):
        user = self.login_user.text()
        password = self.login_pass.text()
        if self.user_manager.login(user, password):
            QMessageBox.information(self, "Login", "Login successful!")
            # TODO: transition to dashboard
        else:
            QMessageBox.warning(self, "Login", "Invalid username or password.")

    def handle_register(self):
        user = self.register_user.text()
        password = self.register_pass.text()
        success, msg = self.user_manager.register(user, password)
        if success:
            QMessageBox.information(self, "Register", msg)
        else:
            QMessageBox.warning(self, "Register", msg)
