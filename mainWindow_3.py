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

        # Right Buttons
        self.button_layout = QVBoxLayout()
        self.main_layout.addLayout(self.button_layout)

        self.button1 = QPushButton("Görev 1")
        self.button1.setStyleSheet("background-color: yellow; font-size: 18px;")
        self.button_layout.addWidget(self.button1)

        self.button2 = QPushButton("Görev 2")
        self.button2.setStyleSheet("background-color: pink; font-size: 18px;")
        self.button_layout.addWidget(self.button2)

        self.button3 = QPushButton("Görev 3")
        self.button3.setStyleSheet("background-color: red; font-size: 18px;")
        self.button_layout.addWidget(self.button3)

        # Saat (Sağ Alt Köşe)
        self.datetime_label = QLabel()
        self.datetime_label.setStyleSheet("color: red; font-size: 15px;")
        self.main_layout.addWidget(self.datetime_label, alignment=Qt.AlignRight | Qt.AlignBottom)

        # Zamanlayıcı ile Saat Güncelleme
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        """ Dinamik olarak saat ve tarihi günceller """
        current_time = QDateTime.currentDateTime().toString("dd/MM/yyyy  HH:mm:ss")
        self.datetime_label.setText(current_time)

    def resizeEvent(self, event):
        """ Pencere boyutu değiştiğinde bileşenleri yeniden ölçeklendirir """
        width = self.width()
        height = self.height()

        # Gri ekranı güncelle
        self.video_frame.setFixedSize(int(width * 0.75), int(height * 0.6))

        # Logo boyutunu güncelle
        self.logo_label.setFixedSize(int(width * 0.1), int(height * 0.15))

        # Saatin konumunu sağ alt köşeye ayarla
        self.datetime_label.move(width - 150, height - 30)

        super().resizeEvent(event)

app = QApplication(sys.argv)

window = mainGUI()
window.show()

app.exec()
