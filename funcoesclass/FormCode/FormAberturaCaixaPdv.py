# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormLyoute/FormAberturaCaixaPdv.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormAberturaCaixaPdv(object):
    def setupUi(self, FormAberturaCaixaPdv):
        FormAberturaCaixaPdv.setObjectName("FormAberturaCaixaPdv")
        FormAberturaCaixaPdv.setWindowModality(QtCore.Qt.ApplicationModal)
        FormAberturaCaixaPdv.resize(986, 631)
        FormAberturaCaixaPdv.setStyleSheet("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(FormAberturaCaixaPdv)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_2 = QtWidgets.QWidget(FormAberturaCaixaPdv)
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
"\n"
"    background-color: rgb(0, 0, 0,200);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setMinimumSize(QtCore.QSize(500, 0))
        self.widget.setMaximumSize(QtCore.QSize(500, 600))
        self.widget.setStyleSheet("QWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"text-transform: uppercase;\n"
"border:4px solid blue;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setStyleSheet("\n"
"QFrame#frame{\n"
"color:red;\n"
"border: none;\n"
"background-color:#2408D4;}\n"
"QLabel{\n"
"color:white;\n"
"border: none;\n"
"background:none;\n"
"    font: 20pt \"Arial\";\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LB_abertura = QtWidgets.QLabel(self.frame)
        self.LB_abertura.setStyleSheet("")
        self.LB_abertura.setAlignment(QtCore.Qt.AlignCenter)
        self.LB_abertura.setObjectName("LB_abertura")
        self.horizontalLayout_2.addWidget(self.LB_abertura)
        self.verticalLayout.addWidget(self.frame)
        self.frame_11 = QtWidgets.QFrame(self.widget)
        self.frame_11.setStyleSheet("QFrame\n"
"{background: #eaeaea;\n"
"border: none\n"
"}\n"
"QLineEdit{\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"border:none\n"
"}\n"
"QLineEdit:Focus {\n"
"border: 1px solid red;\n"
"}\n"
"\n"
"QLabel{\n"
"text-transform: uppercase;\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: #797979\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.tx_Descricaixa = QtWidgets.QLineEdit(self.frame_11)
        self.tx_Descricaixa.setGeometry(QtCore.QRect(10, 30, 251, 31))
        self.tx_Descricaixa.setObjectName("tx_Descricaixa")
        self.label_7 = QtWidgets.QLabel(self.frame_11)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_11)
        self.label_8.setGeometry(QtCore.QRect(210, 70, 47, 13))
        self.label_8.setObjectName("label_8")
        self.db_valorCaixa = QtWidgets.QDoubleSpinBox(self.frame_11)
        self.db_valorCaixa.setGeometry(QtCore.QRect(210, 100, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.db_valorCaixa.setFont(font)
        self.db_valorCaixa.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.db_valorCaixa.setAlignment(QtCore.Qt.AlignCenter)
        self.db_valorCaixa.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.db_valorCaixa.setProperty("showGroupSeparator", True)
        self.db_valorCaixa.setMaximum(99999.0)
        self.db_valorCaixa.setProperty("value", 0.0)
        self.db_valorCaixa.setObjectName("db_valorCaixa")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setGeometry(QtCore.QRect(10, 490, 471, 51))
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_12.setStyleSheet("\n"
"QFrame{\n"
"border:none\n"
"}\n"
"QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:20px;\n"
"    cursor: pointer;\n"
"    background-color:red;\n"
"padding:5px 15px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}\n"
"\n"
"QPushButton#bt_confirma{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:20px;\n"
"    cursor: pointer;\n"
"    background-color:#538fff;\n"
"padding:5px 15px;\n"
"}\n"
"QPushButton#bt_confirma:hover{\n"
"background-color:#3668ff;\n"
"}")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.bt_confirma = QtWidgets.QPushButton(self.frame_12)
        self.bt_confirma.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.bt_confirma.setFont(font)
        self.bt_confirma.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_confirma.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_confirma.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_confirma.setStyleSheet("")
        self.bt_confirma.setIconSize(QtCore.QSize(75, 35))
        self.bt_confirma.setObjectName("bt_confirma")
        self.horizontalLayout_10.addWidget(self.bt_confirma)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem1)
        self.bt_sairlancamento = QtWidgets.QPushButton(self.frame_12)
        self.bt_sairlancamento.setMinimumSize(QtCore.QSize(0, 30))
        self.bt_sairlancamento.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_sairlancamento.setObjectName("bt_sairlancamento")
        self.horizontalLayout_10.addWidget(self.bt_sairlancamento)
        self.dt_incluirdata = QtWidgets.QDateEdit(self.frame_11)
        self.dt_incluirdata.setGeometry(QtCore.QRect(290, 30, 151, 31))
        self.dt_incluirdata.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dt_incluirdata.setStyleSheet("QDateEdit {\n"
"    border: 2px solid lightgray;\n"
"    border-radius: 5px;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
" \n"
"")
        self.dt_incluirdata.setCalendarPopup(True)
        self.dt_incluirdata.setObjectName("dt_incluirdata")
        self.label_9 = QtWidgets.QLabel(self.frame_11)
        self.label_9.setGeometry(QtCore.QRect(290, 10, 91, 16))
        self.label_9.setObjectName("label_9")
        self.cb_incluirTipodocumento = QtWidgets.QComboBox(self.frame_11)
        self.cb_incluirTipodocumento.setGeometry(QtCore.QRect(10, 100, 151, 31))
        self.cb_incluirTipodocumento.setStyleSheet("border:1px solid;")
        self.cb_incluirTipodocumento.setObjectName("cb_incluirTipodocumento")
        self.label_10 = QtWidgets.QLabel(self.frame_11)
        self.label_10.setGeometry(QtCore.QRect(10, 70, 121, 16))
        self.label_10.setObjectName("label_10")
        self.tab_caixa = QtWidgets.QTableWidget(self.frame_11)
        self.tab_caixa.setGeometry(QtCore.QRect(10, 150, 481, 341))
        self.tab_caixa.setStyleSheet("QTableView{\n"
"background: #F1F1F1;\n"
"color: black;\n"
"font-weight: bold;\n"
"font-size: 16px;\n"
"border:1px solid blakc;\n"
"    \n"
"    selection-color: rgb(255, 0, 0);\n"
"    selection-background-color: rgb(85, 170, 255);\n"
"}\n"
"QHeaderView:section{\n"
"background: #FFF;\n"
"\n"
"font-size: 13px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #797979;\n"
"border:none;\n"
"border-bottom: 2px solid black;\n"
"border-top:2px solid black;\n"
"padding:5px 0px;\n"
"text-transform: uppercase\n"
"}\n"
"\n"
"\n"
"")
        self.tab_caixa.setObjectName("tab_caixa")
        self.tab_caixa.setColumnCount(3)
        self.tab_caixa.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_caixa.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_caixa.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_caixa.setHorizontalHeaderItem(2, item)
        self.tab_caixa.horizontalHeader().setStretchLastSection(True)
        self.tab_caixa.verticalHeader().setVisible(False)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.frame_11)
        self.commandLinkButton.setGeometry(QtCore.QRect(390, 100, 41, 41))
        self.commandLinkButton.setStyleSheet("border:none;\n"
"background:none;")
        self.commandLinkButton.setText("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout.addWidget(self.frame_11)
        self.horizontalLayout.addWidget(self.widget)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.widget_2)

        self.retranslateUi(FormAberturaCaixaPdv)
        self.bt_sairlancamento.clicked.connect(FormAberturaCaixaPdv.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(FormAberturaCaixaPdv)
        FormAberturaCaixaPdv.setTabOrder(self.tx_Descricaixa, self.cb_incluirTipodocumento)
        FormAberturaCaixaPdv.setTabOrder(self.cb_incluirTipodocumento, self.db_valorCaixa)
        FormAberturaCaixaPdv.setTabOrder(self.db_valorCaixa, self.bt_sairlancamento)

    def retranslateUi(self, FormAberturaCaixaPdv):
        _translate = QtCore.QCoreApplication.translate
        FormAberturaCaixaPdv.setWindowTitle(_translate("FormAberturaCaixaPdv", "Form"))
        self.LB_abertura.setText(_translate("FormAberturaCaixaPdv", "abertura caixa"))
        self.label_7.setText(_translate("FormAberturaCaixaPdv", "descriçao"))
        self.label_8.setText(_translate("FormAberturaCaixaPdv", "valor"))
        self.bt_confirma.setText(_translate("FormAberturaCaixaPdv", "salvar"))
        self.bt_sairlancamento.setText(_translate("FormAberturaCaixaPdv", "sair"))
        self.bt_sairlancamento.setShortcut(_translate("FormAberturaCaixaPdv", "Esc"))
        self.label_9.setText(_translate("FormAberturaCaixaPdv", "data"))
        self.label_10.setText(_translate("FormAberturaCaixaPdv", "tipo PAgamento"))
        item = self.tab_caixa.horizontalHeaderItem(0)
        item.setText(_translate("FormAberturaCaixaPdv", "tipo doc"))
        item = self.tab_caixa.horizontalHeaderItem(1)
        item.setText(_translate("FormAberturaCaixaPdv", "entrada"))
        item = self.tab_caixa.horizontalHeaderItem(2)
        item.setText(_translate("FormAberturaCaixaPdv", "saida"))
