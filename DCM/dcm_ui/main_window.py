# dcm_ui/main_window.py
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QGroupBox
)
from dcm_core.user_manager import UserManager

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Device Controller Monitor")

        # --- Set default window size and minimum size ---
        self.resize(800, 600)           # default size
        self.setMinimumSize(600, 400)   # cannot shrink below this

        self.user_manager = UserManager()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # --- Login Widgets ---
        self.login_group = QGroupBox()
        login_layout = QVBoxLayout()

        self.login_user = QLineEdit()
        self.login_user.setPlaceholderText("Username")
        login_layout.addWidget(self.login_user)

        self.login_pass = QLineEdit()
        self.login_pass.setPlaceholderText("Password")
        self.login_pass.setEchoMode(QLineEdit.Password)
        login_layout.addWidget(self.login_pass)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_login)
        login_layout.addWidget(login_button)

        self.login_group.setLayout(login_layout)
        self.main_layout.addWidget(self.login_group)

        # --- Dashboard Widgets (hidden initially) ---
        self.dashboard_group = QGroupBox("Dashboard")
        dashboard_layout = QVBoxLayout()

        self.welcome_label = QLabel("")
        dashboard_layout.addWidget(self.welcome_label)

        # Example dashboard buttons
        self.btn_pacing = QPushButton("Pacing Modes")
        dashboard_layout.addWidget(self.btn_pacing)

        self.btn_parameters = QPushButton("Parameters")
        dashboard_layout.addWidget(self.btn_parameters)

        self.dashboard_group.setLayout(dashboard_layout)
        self.dashboard_group.hide()  # hidden until login
        self.main_layout.addWidget(self.dashboard_group)

    def handle_login(self):
        user = self.login_user.text()
        password = self.login_pass.text()
        if self.user_manager.login(user, password):
            # Switch to dashboard
            self.login_group.hide()
            self.dashboard_group.show()
            self.welcome_label.setText(f"Welcome, {user}!")
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
