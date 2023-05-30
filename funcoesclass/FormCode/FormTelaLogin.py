# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormLyoute/FormTelaLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormTelalogin(object):
    def setupUi(self, FormTelalogin):
        FormTelalogin.setObjectName("FormTelalogin")
        FormTelalogin.resize(682, 640)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/telainicial/telainicial/pdv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormTelalogin.setWindowIcon(icon)
        FormTelalogin.setStyleSheet("QWiget#FormTelalogin{\n"
"    background-color: rgb(0, 0, 0,200);\n"
"}")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(FormTelalogin)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(FormTelalogin)
        self.widget_2.setStyleSheet("QWiget#widget_2{\n"
"    background-color: rgb(0, 0, 0,200);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setGeometry(QtCore.QRect(0, 60, 651, 531))
        self.widget.setMinimumSize(QtCore.QSize(400, 400))
        self.widget.setStyleSheet("QWidget#widget{\n"
"    \n"
"    border-image: url(:/telainicial/telainicial/tec.png);\n"
"border-radius:10px;\n"
"\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit{\n"
"border-radius:0px;\n"
"background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:white;\n"
"padding-bottom:7px;\n"
"text-transform: uppercase;\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"text-transform: uppercase;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"text-transform: uppercase;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.lb_log = QtWidgets.QLabel(self.widget)
        self.lb_log.setSizeIncrement(QtCore.QSize(0, 40))
        self.lb_log.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color:none;\n"
"color: rgb(244, 244, 244);")
        self.lb_log.setText("")
        self.lb_log.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_log.setObjectName("lb_log")
        self.verticalLayout_2.addWidget(self.lb_log)
        self.tx_login = QtWidgets.QLineEdit(self.widget)
        self.tx_login.setMinimumSize(QtCore.QSize(0, 40))
        self.tx_login.setSizeIncrement(QtCore.QSize(0, 40))
        self.tx_login.setBaseSize(QtCore.QSize(0, 40))
        self.tx_login.setStyleSheet("")
        self.tx_login.setObjectName("tx_login")
        self.verticalLayout_2.addWidget(self.tx_login)
        self.tx_senha = QtWidgets.QLineEdit(self.widget)
        self.tx_senha.setMinimumSize(QtCore.QSize(0, 40))
        self.tx_senha.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tx_senha.setStyleSheet("")
        self.tx_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.tx_senha.setObjectName("tx_senha")
        self.verticalLayout_2.addWidget(self.tx_senha)
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setStyleSheet("QFrame{border:none;\n"
"    background-color:none;\n"
"    background-image: none;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_logar = QtWidgets.QPushButton(self.frame)
        self.bt_logar.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bt_logar.setFont(font)
        self.bt_logar.setStyleSheet("QPushButton#pushButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2, 65, 118, 100);\n"
"background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.bt_logar.setObjectName("bt_logar")
        self.horizontalLayout.addWidget(self.bt_logar)
        self.bt_canelar = QtWidgets.QPushButton(self.frame)
        self.bt_canelar.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bt_canelar.setFont(font)
        self.bt_canelar.setStyleSheet("")
        self.bt_canelar.setObjectName("bt_canelar")
        self.horizontalLayout.addWidget(self.bt_canelar)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget_2)
        self.frame_2.setGeometry(QtCore.QRect(280, 10, 101, 101))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setStyleSheet("background-color: rgb(55, 111, 167);\n"
"border-radius:50%;\n"
"background-image: url(:/telainicial/telainicial/cadastro clientes.png);\n"
" height: 200px;\n"
"  background-position: center; /* Center the image */\n"
"  background-repeat: no-repeat; /* Do not repeat the image */\n"
" ")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.actionsenha = QtWidgets.QAction(FormTelalogin)
        self.actionsenha.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/telainicial/telainicial/olho.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionsenha.setIcon(icon1)
        self.actionsenha.setObjectName("actionsenha")

        self.retranslateUi(FormTelalogin)
        QtCore.QMetaObject.connectSlotsByName(FormTelalogin)

    def retranslateUi(self, FormTelalogin):
        _translate = QtCore.QCoreApplication.translate
        FormTelalogin.setWindowTitle(_translate("FormTelalogin", "Login"))
        self.label.setText(_translate("FormTelalogin", "seja bem vindo"))
        self.tx_login.setPlaceholderText(_translate("FormTelalogin", "login"))
        self.tx_senha.setPlaceholderText(_translate("FormTelalogin", "senha"))
        self.bt_logar.setText(_translate("FormTelalogin", "login"))
        self.bt_canelar.setText(_translate("FormTelalogin", "cancelar"))
        self.actionsenha.setText(_translate("FormTelalogin", "senha"))
        self.actionsenha.setToolTip(_translate("FormTelalogin", "VER SENHA"))
