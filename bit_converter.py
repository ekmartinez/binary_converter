from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BitConverter(object):

    def setupUi(self, BitConverter):

        BitConverter.setObjectName("BitConverter")
        BitConverter.resize(571, 281)
        BitConverter.setMaximumSize(QtCore.QSize(571, 281))
        self.centralwidget = QtWidgets.QWidget(BitConverter)
        self.centralwidget.setObjectName("centralwidget")
        
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(20, 10, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Bengali Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 70, 111, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        
        self.decimal_option = QtWidgets.QRadioButton(self.groupBox)
        self.decimal_option.setGeometry(QtCore.QRect(10, 50, 101, 22))
        self.decimal_option.setObjectName("decimal_option")
        
        self.binary_option = QtWidgets.QRadioButton(self.groupBox)
        self.binary_option.setGeometry(QtCore.QRect(10, 90, 101, 22))
        self.binary_option.setObjectName("binary_option")
        self.input_label = QtWidgets.QLabel(self.centralwidget)
        self.input_label.setGeometry(QtCore.QRect(150, 80, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        
        self.input_label.setFont(font)
        self.input_label.setObjectName("input_label")
        self.input_box = QtWidgets.QLineEdit(self.centralwidget)
        self.input_box.setGeometry(QtCore.QRect(220, 80, 331, 32))
        self.input_box.setObjectName("input_box")
        
        self.results_label = QtWidgets.QLabel(self.centralwidget)
        self.results_label.setGeometry(QtCore.QRect(150, 120, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.results_label.setFont(font)
        self.results_label.setObjectName("results_label")
        self.results_box = QtWidgets.QLineEdit(self.centralwidget)
        self.results_box.setGeometry(QtCore.QRect(220, 120, 331, 32))
        self.results_box.setText("")
        self.results_box.setObjectName("results_box")
        
        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(370, 170, 84, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.convert_button.setFont(font)
        self.convert_button.setObjectName("convert_button")
        self.convert_button.clicked.connect(self.convert)
        
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(460, 170, 91, 34))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exit_button.setFont(font)
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(sys.exit)


        BitConverter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BitConverter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 30))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        BitConverter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BitConverter)
        self.statusbar.setObjectName("statusbar")
        BitConverter.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(BitConverter)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(BitConverter)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(BitConverter)
        QtCore.QMetaObject.connectSlotsByName(BitConverter)

    def retranslateUi(self, BitConverter):
        _translate = QtCore.QCoreApplication.translate
        BitConverter.setWindowTitle(_translate("BitConverter", "Bit-Converter"))
        self.title_label.setText(_translate("BitConverter", "Bit-Converter"))
        self.groupBox.setTitle(_translate("BitConverter", "Convert to:"))
        self.decimal_option.setText(_translate("BitConverter", "Decimal"))
        self.binary_option.setText(_translate("BitConverter", "Binary"))
        self.input_label.setText(_translate("BitConverter", "Input"))
        self.results_label.setText(_translate("BitConverter", "Results"))
        self.convert_button.setText(_translate("BitConverter", "Convert"))
        self.exit_button.setText(_translate("BitConverter", "Exit"))
        self.menuFile.setTitle(_translate("BitConverter", "File"))
        self.actionAbout.setText(_translate("BitConverter", "About"))
        self.actionExit.setText(_translate("BitConverter", "Exit"))

    def convert(self):
        num = self.input_box.text()

        if self.decimal_option.isChecked():
            self.results_box.setText(str(int(num, 2)))

        if self.binary_option.isChecked():
            self.results_box.setText(bin(int(num))[2:])



'''
    def convert(self):
        
        initialized = converter(self.input_box.text())

        if self.decimal_option.isChecked():
            self.results_box.setText(str(initialized.to_decimal()))

        if self.binary_option.isChecked():
            self.results_box.setText(str(initialized.to_binary()))
    
    '''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BitConverter = QtWidgets.QMainWindow()
    ui = Ui_BitConverter()
    ui.setupUi(BitConverter)
    BitConverter.show()
    sys.exit(app.exec_())
