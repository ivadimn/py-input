from PyQt6.QtWidgets import QApplication
import sys
from widget import Widget


if __name__ == '__main__':

    app = QApplication(sys.argv)
    main_window = Widget()
    main_window.show()
    result = app.exec()
    sys.exit(result)
