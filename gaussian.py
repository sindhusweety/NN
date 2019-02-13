# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gaussian.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_gaussian(object):
    def setupUi(self, gaussian):
        gaussian.setObjectName("gaussian")
        gaussian.resize(989, 721)
        self.centralwidget = QtWidgets.QWidget(gaussian)
        self.centralwidget.setObjectName("centralwidget")
        self.A_label = QtWidgets.QLabel(self.centralwidget)
        self.A_label.setGeometry(QtCore.QRect(230, 300, 81, 31))
        self.A_label.setObjectName("A_label")
        self.sigmaX = QtWidgets.QLabel(self.centralwidget)
        self.sigmaX.setGeometry(QtCore.QRect(230, 350, 81, 17))
        self.sigmaX.setObjectName("sigmaX")
        self.sigmaY = QtWidgets.QLabel(self.centralwidget)
        self.sigmaY.setGeometry(QtCore.QRect(230, 400, 68, 17))
        self.sigmaY.setObjectName("sigmaY")
        self.A_value = QtWidgets.QLineEdit(self.centralwidget)
        self.A_value.setGeometry(QtCore.QRect(410, 300, 113, 27))
        self.A_value.setObjectName("A_value")
        self.x_value = QtWidgets.QLineEdit(self.centralwidget)
        self.x_value.setGeometry(QtCore.QRect(410, 350, 113, 27))
        self.x_value.setObjectName("x_value")
        self.y_value = QtWidgets.QLineEdit(self.centralwidget)
        self.y_value.setGeometry(QtCore.QRect(410, 400, 113, 27))
        self.y_value.setObjectName("y_value")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 480, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.gaussianwidget = gaussianWidget(self.centralwidget)
        self.gaussianwidget.setGeometry(QtCore.QRect(240, 40, 301, 241))
        self.gaussianwidget.setObjectName("gaussianwidget")
        gaussian.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(gaussian)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 25))
        self.menubar.setObjectName("menubar")
        gaussian.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(gaussian)
        self.statusbar.setObjectName("statusbar")
        gaussian.setStatusBar(self.statusbar)

        self.retranslateUi(gaussian)
        self.pushButton.clicked.connect(self.gaussianwidget.update_graph)
        QtCore.QMetaObject.connectSlotsByName(gaussian)
        self.pushButton.clicked.connect(self.update_graph_value)


    def retranslateUi(self, gaussian):
        _translate = QtCore.QCoreApplication.translate
        gaussian.setWindowTitle(_translate("gaussian", "MainWindow"))
        self.A_label.setText(_translate("gaussian", "A"))
        self.sigmaX.setText(_translate("gaussian", "sigmaX"))
        self.sigmaY.setText(_translate("gaussian", "sigmaY"))
        self.pushButton.setText(_translate("gaussian", "formula"))

    def update_graph_value(self):
        A = self.A_value.text()
        sigma_x = self.x_value.text()
        sigma_y = self.y_value.text()
        list = [float(A), float(sigma_x), float(sigma_y)]
        import json
        with open('list_gaussian_value.json', 'w') as outfile:
            json.dump(list, outfile)

from gaussianwidget import gaussianWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gaussian = QtWidgets.QMainWindow()
    ui = Ui_gaussian()
    ui.setupUi(gaussian)
    gaussian.show()
    sys.exit(app.exec_())

