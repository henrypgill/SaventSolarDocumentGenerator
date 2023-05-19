
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QWidget, QPushButton, QLabel, QFormLayout, QLineEdit, QFileDialog
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal
from . import formToPDFWidget, textAndImageLabelWidget, imageUploadButtonWidget
from PyQt6.QtGui import QPixmap


class uploadButton(QPushButton):
    def __init__(self, targetLabel):
        super().__init__()
        self.clicked.connect(self.openImageDialog)
        self.targetLabel = targetLabel
        
    def openImageDialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")
        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            imageFilePath = file_dialog.selectedFiles()[0]
            self.targetLabel.setImage(imageFilePath)  # Update the image label in the grandparent widget
