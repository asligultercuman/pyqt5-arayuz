import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QPushButton, 
                            QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy)
from PyQt5.QtCore import QTimer, Qt, QDateTime
from PyQt5.QtGui import QPixmap

class MainGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("MakinaFleo-HSS")
        self.setGeometry(100, 100, 800, 450)
        self.setStyleSheet("background-color: lightblue;")

        # Ana dikey layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)
        
        # Üst kısım (Başlık)
        header_layout = QHBoxLayout()
        self.title = QLabel("MakinaFleo-HSS")
        self.title.setStyleSheet("color: red; font-size: 14px;")
        header_layout.addWidget(self.title, alignment=Qt.AlignLeft)
        
        # Esnek boşluk ekle
        header_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        main_layout.addLayout(header_layout)

        # Orta kısım (Video + Sağ Panel)
        middle_layout = QHBoxLayout()
        main_layout.addLayout(middle_layout, stretch=1)

        # Video Alanı (Sol)
        self.video_frame = QLabel()
        self.video_frame.setStyleSheet("""
            background-color: lightgray;
            border: 2px solid darkgray;
            border-radius: 10px;
        """)
        middle_layout.addWidget(self.video_frame, stretch=3)

        # Sağ Panel (Logo ve Butonlar)
        right_panel = QVBoxLayout()
        right_panel.setSpacing(15)
        middle_layout.addLayout(right_panel, stretch=1)

        # Logo
        self.logo = QLabel()
        self.logo.setPixmap(QPixmap("logo.png").scaled(100, 100, Qt.KeepAspectRatio))
        self.logo.setAlignment(Qt.AlignCenter)
        right_panel.addWidget(self.logo)

        # Butonlar
        self.btn1 = self.create_button("Görev 1", "yellow")
        self.btn2 = self.create_button("Görev 2", "pink")
        self.btn3 = self.create_button("Görev 3", "#FF6666")
        
        right_panel.addWidget(self.btn1)
        right_panel.addWidget(self.btn2)
        right_panel.addWidget(self.btn3)
        
        # Alt kısım (Saat)
        self.time_label = QLabel()
        self.time_label.setStyleSheet("color: red; font-size: 14px;")
        main_layout.addWidget(self.time_label, alignment=Qt.AlignRight | Qt.AlignBottom)

        # Zaman güncelleme
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def create_button(self, text, color):
        btn = QPushButton(text)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                font-size: 16px;
                min-width: 120px;
                min-height: 40px;
                border-radius: 8px;
                border: 1px solid gray;
            }}
            QPushButton:hover {{
                background-color: {color};
                opacity: 0.8;
            }}
        """)
        return btn

    def update_time(self):
        current_time = QDateTime.currentDateTime().toString("dd/MM/yyyy  HH:mm:ss")
        self.time_label.setText(current_time)

    def resizeEvent(self, event):
        # Logo boyutunu dinamik ayarla
        new_size = min(self.width()//8, self.height()//5)
        self.logo.setPixmap(QPixmap("logo.png").scaled(
            new_size, new_size, 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        ))
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainGUI()
    window.show()
    sys.exit(app.exec_())
