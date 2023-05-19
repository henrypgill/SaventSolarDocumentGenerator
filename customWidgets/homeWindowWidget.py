
import sys
#import getStyleSheet
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QWidget, QPushButton, QLabel, QFormLayout, QLineEdit, QFileDialog
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal
from . import formToPDFWidget, textAndImageLabelWidget, imageUploadButtonWidget




class homeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Application")
        self.resize(800, 800)
        
        #self.setStyleSheet(getStyleSheet.mainStyleSheet())
        
        
        # Set up the home layout 
        self.homeWidget = QWidget()
        self.homeLayout = QGridLayout()
        self.homeWidget.setLayout(self.homeLayout)
        
        # Set up the home components
        self.titleLabel = QLabel("Welcome to the Savent Solar Document Generator")
        self.subTitleLabel = QLabel("Select the form you would like to create using the buttons below.")
        
        # Create a button that links to the maintenance report generator
        self.button = QPushButton("Create Maintenance Report", self)
        self.button.clicked.connect(self.openMaintenanceReportGenerator)
        
        
        #add the widgets of the home view
        self.homeLayout.addWidget(self.titleLabel, 0, 0, 1, 2)
        self.homeLayout.addWidget(self.subTitleLabel, 1, 0, 1, 2)
        self.homeLayout.addWidget(self.button, 2, 0)
        
        
        
        # Set up the stacked layout
        
        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.homeWidget)
        
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.stackedLayout)
    
        
        # Set the layout as the main window's central widget
        
        # Add other views as widgets
        self.maintenanceReportWidget = formToPDFWidget.maintenanceReportWidget()
        self.maintenanceReportWidget.backToHomeRequested.connect(self.show_home_widget)
        self.stackedLayout.addWidget(self.maintenanceReportWidget)
    
    
    
    #method for returning to the home view
    def show_home_widget(self):
        self.stackedLayout.setCurrentWidget(self.homeWidget)
        
        
    #methods for switching to other views
    def openMaintenanceReportGenerator(self):
        self.stackedLayout.setCurrentWidget(self.maintenanceReportWidget)