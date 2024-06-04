# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(590, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMaximumSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        mainWindow.setFont(font)
        mainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(parent=mainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainFrame = QtWidgets.QFrame(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.mainFrame)
        self.label.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.mainForm = QtWidgets.QVBoxLayout()
        self.mainForm.setContentsMargins(-1, 5, -1, -1)
        self.mainForm.setObjectName("mainForm")
        self.credentials = QtWidgets.QHBoxLayout()
        self.credentials.setObjectName("credentials")
        self.credentialsLabel = QtWidgets.QLabel(parent=self.mainFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.credentialsLabel.setFont(font)
        self.credentialsLabel.setObjectName("credentialsLabel")
        self.credentials.addWidget(self.credentialsLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.credentials.addItem(spacerItem)
        self.credentialsBtn = QtWidgets.QPushButton(parent=self.mainFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.credentialsBtn.setFont(font)
        self.credentialsBtn.setObjectName("credentialsBtn")
        self.credentials.addWidget(self.credentialsBtn)
        self.mainForm.addLayout(self.credentials)
        self.path = QtWidgets.QHBoxLayout()
        self.path.setObjectName("path")
        self.pathLabel = QtWidgets.QLabel(parent=self.mainFrame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pathLabel.setFont(font)
        self.pathLabel.setObjectName("pathLabel")
        self.path.addWidget(self.pathLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.path.addItem(spacerItem1)
        self.pathInput = QtWidgets.QLineEdit(parent=self.mainFrame)
        self.pathInput.setObjectName("pathInput")
        self.path.addWidget(self.pathInput)
        self.browsePath = QtWidgets.QToolButton(parent=self.mainFrame)
        self.browsePath.setObjectName("browsePath")
        self.path.addWidget(self.browsePath)
        self.mainForm.addLayout(self.path)
        self.sync = QtWidgets.QVBoxLayout()
        self.sync.setContentsMargins(100, 0, 100, 10)
        self.sync.setSpacing(15)
        self.sync.setObjectName("sync")
        self.syncBtn = QtWidgets.QPushButton(parent=self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.syncBtn.sizePolicy().hasHeightForWidth())
        self.syncBtn.setSizePolicy(sizePolicy)
        self.syncBtn.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.syncBtn.setFont(font)
        self.syncBtn.setCheckable(False)
        self.syncBtn.setChecked(False)
        self.syncBtn.setAutoDefault(False)
        self.syncBtn.setDefault(False)
        self.syncBtn.setFlat(False)
        self.syncBtn.setObjectName("syncBtn")
        self.sync.addWidget(self.syncBtn, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.syncProgressBar = QtWidgets.QProgressBar(parent=self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.syncProgressBar.sizePolicy().hasHeightForWidth())
        self.syncProgressBar.setSizePolicy(sizePolicy)
        self.syncProgressBar.setMinimumSize(QtCore.QSize(350, 0))
        self.syncProgressBar.setProperty("value", 42)
        self.syncProgressBar.setObjectName("syncProgressBar")
        self.sync.addWidget(self.syncProgressBar, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.syncStatusMessage = QtWidgets.QLabel(parent=self.mainFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.syncStatusMessage.setFont(font)
        self.syncStatusMessage.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.syncStatusMessage.setObjectName("syncStatusMessage")
        self.sync.addWidget(self.syncStatusMessage)
        self.mainForm.addLayout(self.sync)
        self.verticalLayout_3.addLayout(self.mainForm)
        self.verticalLayout.addWidget(self.mainFrame, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 590, 24))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(parent=self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=mainWindow)
        self.toolBar.setObjectName("toolBar")
        mainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionCredentials = QtGui.QAction(parent=mainWindow)
        self.actionCredentials.setObjectName("actionCredentials")
        self.actionPreferences = QtGui.QAction(parent=mainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.menuSettings.addAction(self.actionCredentials)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Kindle Clippings to Notion"))
        self.label.setText(_translate("mainWindow", "Kindle Clippings to Notion"))
        self.credentialsLabel.setText(_translate("mainWindow", "Edit Credentials"))
        self.credentialsBtn.setText(_translate("mainWindow", "Credentials"))
        self.pathLabel.setText(_translate("mainWindow", "Path to \"My Clippings.txt\""))
        self.browsePath.setText(_translate("mainWindow", "..."))
        self.syncBtn.setText(_translate("mainWindow", "Sync!"))
        self.syncStatusMessage.setText(_translate("mainWindow", "Some Message"))
        self.menuSettings.setTitle(_translate("mainWindow", "Settings"))
        self.toolBar.setWindowTitle(_translate("mainWindow", "toolBar"))
        self.actionCredentials.setText(_translate("mainWindow", "Credentials"))
        self.actionPreferences.setText(_translate("mainWindow", "Preferences"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
