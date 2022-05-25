import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import numpy as np
import sys
import time
from ui.ui import  *

class MainWindow(QMainWindow):
    
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.disply_width = 640
        self.display_height = 480
        self.current_datetime()
        #self.update_label(label, value)
    
    def current_datetime(self):
        """
        It sets the date and time of the dateTimeEdit widget to the current date and time, sets the maximum
        date to 12/28/7999, sets the maximum time to 23:59:59, and sets the calendar popup to true
        """
        self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ui.dateTimeEdit.setMaximumDate(QtCore.QDate(7999, 12, 28))
        self.ui.dateTimeEdit.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.ui.dateTimeEdit.setCalendarPopup(True)


    def update_table(self):
        """
        The function takes the text from the line edits and appends them to the table
        """
        #self.ui.textBrowser.append(....)
        pass

    def update_label(self,label,value):
        """
        It takes a label and a value, and updates the label with the value
        
        :param label: the label to update
        :param value: The value of the slider
        """
        #label.setText(value)
        pass
if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())