
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QWidget, QPushButton, QLabel, QFormLayout, QLineEdit, QFileDialog
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal
from . import formToPDFWidget, textAndImageLabelWidget, imageUploadButtonWidget
from PyQt6.QtGui import QPixmap




# class for an image label that holds the label and a preview of the image      
class imageLabel(QWidget):
    def __init__(self, labelText):
        super().__init__()
        
        imageLabelLayout = QHBoxLayout()
        self.textLabel = QLabel(labelText)
        self.imageLabel = QLabel()
        imageLabelLayout.addWidget(self.textLabel)
        imageLabelLayout.addWidget(self.imageLabel)
        self.setLayout(imageLabelLayout)
    
    def setImage(self, imagePath):
        pixmap = QPixmap(imagePath)
        self.imageLabel.setPixmap(pixmap.scaled(200, 200, QtCore.Qt.AspectRatioMode.KeepAspectRatio))
        
        

