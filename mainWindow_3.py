import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
from PyQt5.QtCore import QTimer, Qt, QDateTime
from PyQt5.QtGui import QPixmap, QFont

class mainGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MakinaFleo-HSS")
        self.setGeometry(100, 100, 800, 450)
        self.setStyleSheet("background-color: lightblue")

        self.title_label = QLabel("MakinaFleo-HSS", self)
        self.title_label.setStyleSheet("color: red; font-size: 14px;")
        self.title_label.move(10, 10)

        # Upper right logo
        #self.logo_label = QLabel(self)
        #self.logo_label.setPixmap(QPixmap("logo.png"))  # Resmi ekle
        #self.logo_label.setScaledContents(True)
        #self.logo_label.setGeometry(670, 20, 100, 100)

        # Ortadaki Video Alanı (Gri Arkaplan)
        self.video_frame = QLabel(self)
        self.video_frame.setGeometry(100, 50, 600, 300)
        self.video_frame.setStyleSheet("background-color: lightgray; border: 1px solid black;")

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
