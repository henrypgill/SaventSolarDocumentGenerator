
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QWidget, QPushButton, QLabel, QFormLayout, QLineEdit, QFileDialog
from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal
from . import formToPDFWidget, textAndImageLabelWidget, imageUploadButtonWidget




class maintenanceReportWidget(QWidget):
    
    backToHomeRequested = pyqtSignal()
    
  
        
    def __init__(self):
        super().__init__()
        
        
        
        # class to create the formData object that holds the information from the form once it's submitted
        class formData:
            def __init__(self):
                pass
            
            def addData(self, label, field):
                setattr(self, label, field)
                
                
        
        #create the layout for the form
        self.formWidget = QWidget()
        self.formLayout = QFormLayout()
    
        
        self.label_firstName = QLabel("Client first name")
        self.field_firstName = QLineEdit()
        
        self.label_surName = QLabel("Client surname")
        self.field_surName = QLineEdit()
        
        self.label_address1 = QLabel("Address line 1")
        self.field_address1 = QLineEdit()
        
        self.label_address2 = QLabel("Address line 2")
        self.field_address2 = QLineEdit()
        
        self.label_town = QLabel("Town")
        self.field_town = QLineEdit()
        
        self.label_county = QLabel("County")
        self.field_county = QLineEdit()
        
        self.label_postcode = QLabel("Postcode")
        self.field_postcode = QLineEdit()
        
        self.label_reportDate = QLabel("Date the report was carried out on")
        self.field_reportDate = QLineEdit()
        
        #pre-clean images
        self.label_preCleanImg1 = textAndImageLabelWidget.imageLabel("Pre-clean image 1")
        self.field_preCleanImg1 = imageUploadButtonWidget.uploadButton(self.label_preCleanImg1)
        
        self.label_preCleanImg2 = textAndImageLabelWidget.imageLabel("Pre-clean image 2")
        self.field_preCleanImg2 = QLineEdit()
        
        self.label_preCleanImg3 = textAndImageLabelWidget.imageLabel("Pre-clean image 3")
        self.field_preCleanImg3 = QLineEdit()
        
        self.label_preCleanImg4 = textAndImageLabelWidget.imageLabel("Pre-clean image 4")
        self.field_preCleanImg4 = QLineEdit()
        
        #mid-clean images
        self.label_midCleanImg1 = textAndImageLabelWidget.imageLabel("Mid-clean image 1")
        self.field_midCleanImg1 = QLineEdit()
        
        self.label_midCleanImg2 = textAndImageLabelWidget.imageLabel("Mid-clean image 2")
        self.field_midCleanImg2 = QLineEdit()
        
        self.label_midCleanImg3 = textAndImageLabelWidget.imageLabel("Mid-clean image 3")
        self.field_midCleanImg3 = QLineEdit()
        
        self.label_midCleanImg4 = textAndImageLabelWidget.imageLabel("Mid-clean image 4")
        self.field_midCleanImg4 = QLineEdit()
        
        #post-clean images
        self.label_postCleanImg1 = textAndImageLabelWidget.imageLabel("Post-clean image 1")
        self.field_postCleanImg1 = QLineEdit()
        
        self.label_postCleanImg2 = textAndImageLabelWidget.imageLabel("Post-clean image 2")
        self.field_postCleanImg2 = QLineEdit()
        
        self.label_postCleanImg3 = textAndImageLabelWidget.imageLabel("Post-clean image 3")
        self.field_postCleanImg3 = QLineEdit()
        
        self.label_postCleanImg4 = textAndImageLabelWidget.imageLabel("Post-clean image 4")
        self.field_postCleanImg4 = QLineEdit()
        
        upload_button = QPushButton("Upload Image")

        #add address fields
        self.formLayout.addRow(self.label_firstName, self.field_firstName)
        self.formLayout.addRow(self.label_surName, self.field_surName)
        self.formLayout.addRow(self.label_address1, self.field_address1)
        self.formLayout.addRow(self.label_address2, self.field_address2)
        self.formLayout.addRow(self.label_town, self.field_town)
        self.formLayout.addRow(self.label_county, self.field_county)
        self.formLayout.addRow(self.label_postcode, self.field_postcode)
        #add date fields
        self.formLayout.addRow(self.label_reportDate, self.field_reportDate)
        #add pre-clean image fields
        self.formLayout.addRow(self.label_preCleanImg1, self.field_preCleanImg1)
        self.formLayout.addRow(self.label_preCleanImg2, self.field_preCleanImg2)
        self.formLayout.addRow(self.label_preCleanImg3, self.field_preCleanImg3)
        self.formLayout.addRow(self.label_preCleanImg4, self.field_preCleanImg4)
        #add mid-clean image fields
        self.formLayout.addRow(self.label_midCleanImg1, self.field_midCleanImg1)
        self.formLayout.addRow(self.label_midCleanImg2, self.field_midCleanImg2)
        self.formLayout.addRow(self.label_midCleanImg3, self.field_midCleanImg3)
        self.formLayout.addRow(self.label_midCleanImg4, self.field_midCleanImg4)
        #add post-clean image fields
        self.formLayout.addRow(self.label_postCleanImg1, self.field_postCleanImg1)
        self.formLayout.addRow(self.label_postCleanImg2, self.field_postCleanImg2)
        self.formLayout.addRow(self.label_postCleanImg3, self.field_postCleanImg3)
        self.formLayout.addRow(self.label_postCleanImg4, self.field_postCleanImg4)
        
        
        
        self.formWidget.setLayout(self.formLayout)
        
        
        
        #create the layout for the window
        windowGridLayout = QGridLayout()
        
        #create the widgets to be added to the layout
        self.titleLabel = QLabel("This is the maintenance report generator")
        self.subTitleLabel = QLabel("Fill in the fields below with the relevant information to create a maintenance report.")
        
        self.homeButton = QPushButton("Back to Home")
        self.homeButton.clicked.connect(self.backToHome)
        
        self.submitButton = QPushButton("Create Report")
        self.submitButton.clicked.connect(self.submitFormData)
        
        windowGridLayout.addWidget(self.titleLabel)
        windowGridLayout.addWidget(self.subTitleLabel)
        windowGridLayout.addWidget(self.homeButton)
        windowGridLayout.addWidget(self.formWidget)
        windowGridLayout.setAlignment(self.homeButton, QtCore.Qt.AlignmentFlag.AlignCenter)
        windowGridLayout.addWidget(self.submitButton)
        self.setLayout(windowGridLayout)
        
        
        #form submission
        self.formAddress = formData()
        self.formPreCleanPictures = formData()
        self.formPostCleanPictures = formData()
        self.formInfo = formData()
        

        
    def submitFormData(self):
        
        self.formAddress.addData("firstName", self.field_firstName.text())
        self.formAddress.addData("surName", self.field_surName.text())
        self.formAddress.addData("address1", self.field_address1.text())
        self.formAddress.addData("address2", self.field_address2.text())
        self.formAddress.addData("town", self.field_town.text())
        self.formAddress.addData("county", self.field_county.text())
        self.formAddress.addData("postcode", self.field_postcode.text())
        
        self.formInfo.addData("date", self.field_reportDate.text())
        
        for formLabel in vars(self.formAddress):
            formField = getattr(self.formAddress, formLabel)
            print(formLabel, "=", formField)

        


    def backToHome(self):
        self.backToHomeRequested.emit()
        