# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormLyoute/FormBaixaReceber.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormBaixaReceber(object):
    def setupUi(self, FormBaixaReceber):
        FormBaixaReceber.setObjectName("FormBaixaReceber")
        FormBaixaReceber.resize(1313, 815)
        FormBaixaReceber.setStyleSheet("QWidget#FormBaixaReceber{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(0, 0, 0, 118), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none;\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 127);\n"
"font-size: 24px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:0px;\n"
"}\n"
"QLineEdit:focus{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox{\n"
"border:1px solid;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:0px;\n"
"}")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(FormBaixaReceber)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_2 = QtWidgets.QWidget(FormBaixaReceber)
        self.widget_2.setStyleSheet("\n"
"QWidget#widget_2{\n"
"    background-color: rgb(0, 0, 0,0);\n"
"text-transform: uppercase;\n"
"\n"
"}\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setMinimumSize(QtCore.QSize(1000, 0))
        self.widget.setMaximumSize(QtCore.QSize(100, 800))
        self.widget.setStyleSheet("QWidget{\n"
"text-transform: uppercase;\n"
"border:1px solid blue;\n"
"    background-color: rgb(231, 231, 231);\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setStyleSheet("QFrame{\n"
"border:none;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.frame_4.setFont(font)
        self.frame_4.setStyleSheet("QFrame#frame_4{\n"
"color:red;\n"
"border: none;\n"
"background-color:#2408D4;}\n"
"\n"
"QLabel{color: white;\n"
"background-color:transparent;\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 220))
        self.frame_3.setStyleSheet("QFrame{border:none;\n"
"\n"
"}\n"
"QGroupBox{\n"
"border:none;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.cb_tipoDocumento = QtWidgets.QComboBox(self.frame_5)
        self.cb_tipoDocumento.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.cb_tipoDocumento.setFont(font)
        self.cb_tipoDocumento.setStyleSheet("QComboBox{\n"
"padding:10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid red;\n"
"    background-color: rgb(255, 255, 127);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.cb_tipoDocumento.setObjectName("cb_tipoDocumento")
        self.verticalLayout_2.addWidget(self.cb_tipoDocumento)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.dt_datapamento = QtWidgets.QDateEdit(self.frame_6)
        self.dt_datapamento.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dt_datapamento.setStyleSheet("QDateEdit {\n"
"    border: 2px solid lightgray;\n"
"    border-radius: 5px;\n"
"    font: 20pt \"MS Shell Dlg 2\";\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.dt_datapamento.setCalendarPopup(True)
        self.dt_datapamento.setObjectName("dt_datapamento")
        self.verticalLayout_5.addWidget(self.dt_datapamento)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.db_valorTotalparcela = QtWidgets.QDoubleSpinBox(self.frame_7)
        self.db_valorTotalparcela.setMinimumSize(QtCore.QSize(300, 40))
        self.db_valorTotalparcela.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font-size: 24px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:0px;")
        self.db_valorTotalparcela.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_valorTotalparcela.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.db_valorTotalparcela.setProperty("showGroupSeparator", True)
        self.db_valorTotalparcela.setDecimals(6)
        self.db_valorTotalparcela.setMaximum(999999.0)
        self.db_valorTotalparcela.setObjectName("db_valorTotalparcela")
        self.verticalLayout.addWidget(self.db_valorTotalparcela)
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.Db_desconto = QtWidgets.QDoubleSpinBox(self.frame_7)
        self.Db_desconto.setMinimumSize(QtCore.QSize(0, 40))
        self.Db_desconto.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font-size: 24px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:0px;")
        self.Db_desconto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Db_desconto.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.Db_desconto.setProperty("showGroupSeparator", True)
        self.Db_desconto.setDecimals(3)
        self.Db_desconto.setMaximum(100.0)
        self.Db_desconto.setObjectName("Db_desconto")
        self.verticalLayout.addWidget(self.Db_desconto)
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.db_valortotal = QtWidgets.QDoubleSpinBox(self.frame_7)
        self.db_valortotal.setMinimumSize(QtCore.QSize(300, 40))
        self.db_valortotal.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font-size: 24px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:0px;")
        self.db_valortotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_valortotal.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.db_valortotal.setProperty("showGroupSeparator", True)
        self.db_valortotal.setDecimals(6)
        self.db_valortotal.setMaximum(9999999.0)
        self.db_valortotal.setObjectName("db_valortotal")
        self.verticalLayout.addWidget(self.db_valortotal)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_6.addWidget(self.frame_3)
        self.tab_BaixaReceber = QtWidgets.QTableWidget(self.frame)
        self.tab_BaixaReceber.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.tab_BaixaReceber.setStyleSheet("QTableWidget {\n"
"  background-color: white;\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"  background-color: gray;\n"
"  color: white;\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"  border: 0px solid black;\n"
"border-bottom:1px solid;\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"  background-color: blue;\n"
"  color: white;\n"
"}\n"
"")
        self.tab_BaixaReceber.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab_BaixaReceber.setTabKeyNavigation(False)
        self.tab_BaixaReceber.setProperty("showDropIndicator", True)
        self.tab_BaixaReceber.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tab_BaixaReceber.setObjectName("tab_BaixaReceber")
        self.tab_BaixaReceber.setColumnCount(9)
        self.tab_BaixaReceber.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_BaixaReceber.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_BaixaReceber.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_BaixaReceber.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.tab_BaixaReceber.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_BaixaReceber.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_BaixaReceber.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_BaixaReceber.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_BaixaReceber.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_BaixaReceber.setHorizontalHeaderItem(8, item)
        self.tab_BaixaReceber.horizontalHeader().setDefaultSectionSize(210)
        self.tab_BaixaReceber.horizontalHeader().setHighlightSections(True)
        self.tab_BaixaReceber.horizontalHeader().setSortIndicatorShown(True)
        self.tab_BaixaReceber.horizontalHeader().setStretchLastSection(False)
        self.tab_BaixaReceber.verticalHeader().setVisible(False)
        self.tab_BaixaReceber.verticalHeader().setHighlightSections(True)
        self.verticalLayout_6.addWidget(self.tab_BaixaReceber)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:20px;\n"
"    cursor: pointer;\n"
"    background-color:#538fff;\n"
"padding:15px 15px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_receber = QtWidgets.QPushButton(self.frame_2)
        self.bt_receber.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/telainicial/telainicial/receber.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_receber.setIcon(icon)
        self.bt_receber.setIconSize(QtCore.QSize(30, 30))
        self.bt_receber.setObjectName("bt_receber")
        self.horizontalLayout.addWidget(self.bt_receber)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.bt_cancelar = QtWidgets.QPushButton(self.frame_2)
        self.bt_cancelar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_cancelar.setStyleSheet("background-color: rgb(255, 0, 127);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/action_stop.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cancelar.setIcon(icon1)
        self.bt_cancelar.setIconSize(QtCore.QSize(30, 30))
        self.bt_cancelar.setAutoRepeatInterval(4)
        self.bt_cancelar.setObjectName("bt_cancelar")
        self.horizontalLayout.addWidget(self.bt_cancelar)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(self.frame)
        self.horizontalLayout_4.addWidget(self.widget)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_5.addWidget(self.widget_2)

        self.retranslateUi(FormBaixaReceber)
        self.bt_cancelar.clicked.connect(FormBaixaReceber.hide) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(FormBaixaReceber)
        FormBaixaReceber.setTabOrder(self.cb_tipoDocumento, self.db_valorTotalparcela)
        FormBaixaReceber.setTabOrder(self.db_valorTotalparcela, self.Db_desconto)
        FormBaixaReceber.setTabOrder(self.Db_desconto, self.db_valortotal)
        FormBaixaReceber.setTabOrder(self.db_valortotal, self.tab_BaixaReceber)

    def retranslateUi(self, FormBaixaReceber):
        _translate = QtCore.QCoreApplication.translate
        FormBaixaReceber.setWindowTitle(_translate("FormBaixaReceber", "RECEBIMENTO"))
        self.label.setText(_translate("FormBaixaReceber", "caixa-receber"))
        self.label_6.setText(_translate("FormBaixaReceber", "Tipo PAgamento"))
        self.label_2.setText(_translate("FormBaixaReceber", "data atual"))
        self.label_4.setText(_translate("FormBaixaReceber", "valor total "))
        self.label_3.setText(_translate("FormBaixaReceber", "valor desconto %"))
        self.Db_desconto.setPrefix(_translate("FormBaixaReceber", "DESCONTO% "))
        self.label_5.setText(_translate("FormBaixaReceber", "valor Final"))
        item = self.tab_BaixaReceber.horizontalHeaderItem(0)
        item.setText(_translate("FormBaixaReceber", "id"))
        item = self.tab_BaixaReceber.horizontalHeaderItem(1)
        item.setText(_translate("FormBaixaReceber", "NOTA"))
        item = self.tab_BaixaReceber.horizontalHeaderItem(2)
        item.setText(_translate("FormBaixaReceber", "NOME CLIENTE"))
        item = self.tab_BaixaReceber.horizontalHeaderItem(3)
        item.setText(_translate("FormBaixaReceber", "desconto"))
        item = self.tab_BaixaReceber.horizontalHeaderItem(4)
        item.setText(_translate("FormBaixaReceber", "valor nominal"))
        item = self.tab_BaixaReceber.horizontalHeaderItem(5)
        item.setText(_translate("FormBaixaReceber", "valor total"))
        item = self.tab_BaixaReceber.horizontalHeaderItem(6)
        item.setText(_translate("FormBaixaReceber", "data emissao"))
        item = self.tab_BaixaReceber.horizontalHeaderItem(7)
        item.setText(_translate("FormBaixaReceber", "data baixa"))
        item = self.tab_BaixaReceber.horizontalHeaderItem(8)
        item.setText(_translate("FormBaixaReceber", "documento"))
        self.bt_receber.setText(_translate("FormBaixaReceber", "baixar receber (F2)"))
        self.bt_receber.setShortcut(_translate("FormBaixaReceber", "F2"))
        self.bt_cancelar.setText(_translate("FormBaixaReceber", "cancelar (esc)"))
        self.bt_cancelar.setShortcut(_translate("FormBaixaReceber", "Esc"))
