from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import QByteArray
import numpy as np


def generate_image():
    array = np.zeros([100, 200, 4], dtype=np.uint8)
    array[:, :100] = [255, 128, 0, 255]  # оранжевый цвет для левого края
    array[:, 100:] = [0, 0, 255, 255]  # голубой цвет для правого

    # установление прозрачности в зависимости от положения x
    for x in range(200):
        for y in range(100):
            array[y, x, 3] = x
    return array


class Image(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Test image from numpy array")
        self.setGeometry(200, 200, 1000, 700)

        vbox = QVBoxLayout(self)
        data = generate_image()
        print(type(data))
        image = rgb2qimage(data)
        label = QLabel(self)
        label.setGeometry(0, 0, 500, 500)
        label.setPixmap(QPixmap.fromImage(image))
        vbox.addWidget(label)
        self.setLayout(vbox)


def rgb2qimage(rgb):
    """Convert the 3D numpy array `rgb` into a 32-bit QImage.  `rgb` must
    have three dimensions with the vertical, horizontal and RGB image axes.

    ATTENTION: This QImage carries an attribute `ndimage` with a
    reference to the underlying numpy array that holds the data. On
    Windows, the conversion into a QPixmap does not copy the data, so
    that you have to take care that the QImage does not get garbage
    collected (otherwise PyQt will throw away the wrapper, effectively
    freeing the underlying memory - boom!)."""
    if len(rgb.shape) != 3:
        raise ValueError("rgb2QImage can only convert 3D arrays")
    if rgb.shape[2] not in (3, 4):
        raise ValueError("rgb2QImage can expects the last dimension to contain exactly three (R,G,B) or four (R,G,B,A) channels")

    h, w, channels = rgb.shape

    # Qt expects 32bit BGRA data for color images:
    bgra = np.empty((h, w, 4), np.uint8, 'C')
    bgra[...,0] = rgb[...,2]
    bgra[...,1] = rgb[...,1]
    bgra[...,2] = rgb[...,0]
    if rgb.shape[2] == 3:
        bgra[...,3].fill(255)
        fmt = QImage.Format.Format_RGB32
    else:
        bgra[...,3] = rgb[...,3]
        fmt = QImage.Format.Format_ARGB32

    result = QImage(bgra.data, w, h, fmt)
    result.ndarray = bgra
    return result
