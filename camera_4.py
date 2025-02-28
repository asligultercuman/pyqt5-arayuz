import sys
import cv2
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

class CameraWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kamera Görüntüsü")
        self.setGeometry(100, 100, 640, 480)
        
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        # OpenCV Video Capture
        self.cap = cv2.VideoCapture(0)  # 0, varsayılan kamera
         
        # Timer to update the frame
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # 30 ms için her frame yenilenecek

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # BGR formatından RGB'ye dönüştürme
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # QImage oluşturma
            height, width, _ = frame.shape
            qimg = QImage(frame.data, width, height, 3 * width, QImage.Format_RGB888)
            
            # QLabel üzerinde görüntü gösterme
            self.image_label.setPixmap(QPixmap.fromImage(qimg))
            
    def closeEvent(self, event):
        self.cap.release()  # Kamera kaynağını serbest bırak
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CameraWindow()
    window.show()
    sys.exit(app.exec_())
