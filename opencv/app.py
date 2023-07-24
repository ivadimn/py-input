import sys
from PyQt6.QtWidgets import QApplication
from qt_image import Image


if __name__ == '__main__':
    app = QApplication(sys.argv)
    image_window = Image()
    image_window.show()
    sys.exit(app.exec())
