
import sys
import getStyleSheet
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QWidget, QPushButton, QLabel, QFormLayout, QLineEdit, QFileDialog
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal

from customWidgets import homeWindowWidget, textAndImageLabelWidget, formToPDFWidget, imageUploadButtonWidget





# Create the application instance
app = QApplication(sys.argv)



homeWindow = homeWindowWidget.homeWindow()

# Create the main window
window = homeWindowWidget.homeWindow()

# Show the main window
window.show()

# Start the event loop
sys.exit(app.exec())
