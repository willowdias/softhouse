# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormLyoute/FormLembrete.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormLembrete(object):
    def setupUi(self, FormLembrete):
        FormLembrete.setObjectName("FormLembrete")
        FormLembrete.resize(1014, 580)
        FormLembrete.setStyleSheet("background-color: rgb(0, 0, 0,200);")
        self.verticalLayout = QtWidgets.QVBoxLayout(FormLembrete)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(FormLembrete)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(500, 500))
        self.widget_2.setMaximumSize(QtCore.QSize(500, 500))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
"border:1px solid blue;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.widget_2)
        self.frame_6.setStyleSheet("QFrame#frame_6{\n"
"color:red;\n"
"border: none;\n"
"background-color:#2408D4;}\n"
"\n"
"QLabel{color: white;\n"
"background-color:transparent;\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"border:none\n"
"}\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_2 = QtWidgets.QFrame(self.widget_2)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_2.setStyleSheet("background-color: rgb(220, 220, 220);\n"
"border:none;\n"
"color:black")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.amarela = QtWidgets.QToolButton(self.frame_2)
        self.amarela.setMinimumSize(QtCore.QSize(80, 80))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pagina/telainicial/paginaamarela.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.amarela.setIcon(icon)
        self.amarela.setIconSize(QtCore.QSize(60, 60))
        self.amarela.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.amarela.setObjectName("amarela")
        self.horizontalLayout_3.addWidget(self.amarela)
        self.azul = QtWidgets.QToolButton(self.frame_2)
        self.azul.setMinimumSize(QtCore.QSize(80, 80))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pagina/telainicial/paginaazul.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.azul.setIcon(icon1)
        self.azul.setIconSize(QtCore.QSize(60, 60))
        self.azul.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.azul.setObjectName("azul")
        self.horizontalLayout_3.addWidget(self.azul)
        self.laranja = QtWidgets.QToolButton(self.frame_2)
        self.laranja.setMinimumSize(QtCore.QSize(80, 80))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/pagina/telainicial/paginalaranja.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.laranja.setIcon(icon2)
        self.laranja.setIconSize(QtCore.QSize(60, 60))
        self.laranja.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.laranja.setObjectName("laranja")
        self.horizontalLayout_3.addWidget(self.laranja)
        self.preto = QtWidgets.QToolButton(self.frame_2)
        self.preto.setMinimumSize(QtCore.QSize(80, 80))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/pagina/telainicial/paginapreta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.preto.setIcon(icon3)
        self.preto.setIconSize(QtCore.QSize(60, 60))
        self.preto.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.preto.setObjectName("preto")
        self.horizontalLayout_3.addWidget(self.preto)
        self.verde = QtWidgets.QToolButton(self.frame_2)
        self.verde.setMinimumSize(QtCore.QSize(80, 80))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/pagina/telainicial/paginaverde.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.verde.setIcon(icon4)
        self.verde.setIconSize(QtCore.QSize(60, 60))
        self.verde.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.verde.setObjectName("verde")
        self.horizontalLayout_3.addWidget(self.verde)
        self.vermelho = QtWidgets.QToolButton(self.frame_2)
        self.vermelho.setMinimumSize(QtCore.QSize(80, 80))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/pagina/telainicial/paginavermelha.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.vermelho.setIcon(icon5)
        self.vermelho.setIconSize(QtCore.QSize(60, 60))
        self.vermelho.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.vermelho.setObjectName("vermelho")
        self.horizontalLayout_3.addWidget(self.vermelho)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.lb_corest = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lb_corest.setFont(font)
        self.lb_corest.setStyleSheet("background-color: rgb(207, 207, 207);\n"
"color: rgb(0, 0, 0);")
        self.lb_corest.setText("")
        self.lb_corest.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_corest.setObjectName("lb_corest")
        self.verticalLayout_2.addWidget(self.lb_corest)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget_2)
        self.plainTextEdit.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.frame = QtWidgets.QFrame(self.widget_2)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(223, 223, 223);\n"
"}\n"
"QPushButton{\n"
"background-color:rgba(2, 65, 118, 255);\n"
"color:rgba(255, 255, 255, 200);\n"
"border-radius:5px;\n"
"padding:15px;\n"
"    font: 14pt \"Segoe UI\";\n"
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
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.salva = QtWidgets.QPushButton(self.frame)
        self.salva.setObjectName("salva")
        self.horizontalLayout_2.addWidget(self.salva)
        self.bt_altera = QtWidgets.QPushButton(self.frame)
        self.bt_altera.setObjectName("bt_altera")
        self.horizontalLayout_2.addWidget(self.bt_altera)
        self.cancelar = QtWidgets.QPushButton(self.frame)
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayout_2.addWidget(self.cancelar)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.widget_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(FormLembrete)
        QtCore.QMetaObject.connectSlotsByName(FormLembrete)

    def retranslateUi(self, FormLembrete):
        _translate = QtCore.QCoreApplication.translate
        FormLembrete.setWindowTitle(_translate("FormLembrete", "lembrete"))
        self.label.setText(_translate("FormLembrete", "INCLUIR LEMBRETE"))
        self.amarela.setText(_translate("FormLembrete", "amarelo"))
        self.azul.setText(_translate("FormLembrete", "azul"))
        self.laranja.setText(_translate("FormLembrete", "laranja"))
        self.preto.setText(_translate("FormLembrete", "preto"))
        self.verde.setText(_translate("FormLembrete", "verde"))
        self.vermelho.setText(_translate("FormLembrete", "vermelho"))
        self.salva.setText(_translate("FormLembrete", "SALVAR (F2)"))
        self.salva.setShortcut(_translate("FormLembrete", "F2"))
        self.bt_altera.setText(_translate("FormLembrete", "ALTERAR (F2)"))
        self.bt_altera.setShortcut(_translate("FormLembrete", "F2"))
        self.cancelar.setText(_translate("FormLembrete", "CANCELAR (ESC)"))
        self.cancelar.setShortcut(_translate("FormLembrete", "Esc"))
