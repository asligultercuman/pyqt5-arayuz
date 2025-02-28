import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QPushButton, QVBoxLayout, QGridLayout,QHBoxLayout, QFrame
from PyQt5.QtCore import QTimer, Qt, QDateTime
from PyQt5.QtGui import QPixmap, QFont

class mainGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MakinaFleo-HSS")
        self.setGeometry(100, 100, 800, 450)
        self.setStyleSheet("background-color: lightblue; border-radius: 20px;")

        # Main Layout
        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)
        
        # Upper Layout (Title and Logo)
        self.top_layout = QHBoxLayout()
        self.main_layout.addLayout(self.top_layout)

        # Title (Upper Left)
        self.title_label = QLabel("MakinaFleo-HSS")
        self.title_label.setStyleSheet("color: red; font-size: 14px;")
        self.top_layout.addWidget(self.title_label, alignment=Qt.AlignLeft | Qt.AlignTop)

        # Upper right logo
        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap("logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setFixedSize(80,80)
        self.top_layout.addWidget(self.logo_label, alignment=Qt.AlignRight | Qt.AlignTop)

        # Ortadaki Video Alanı (Gri Arkaplan)
        self.video_frame = QLabel()
        self.video_frame.setStyleSheet("background-color: lightgray; border: 1px solid black;")
        self.main_layout.addWidget(self.video_frame, stretch=1)

# Subclass QMainWindow to customize your application's main window
#class MainWindow(QMainWindow):
#    def __init__(self):
#        super().__init__()
#
#        self.setWindowTitle("MakinaFleo-HSS")
#        button = QPushButton("Press Me!")
#
#        # Set the central widget of the Window.
#        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = mainGUI()
window.show()

app.exec()
