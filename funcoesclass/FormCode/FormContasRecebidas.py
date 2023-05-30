# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormLyoute/FormContasRecebidas.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormContasRecebidas(object):
    def setupUi(self, FormContasRecebidas):
        FormContasRecebidas.setObjectName("FormContasRecebidas")
        FormContasRecebidas.resize(1381, 802)
        FormContasRecebidas.setMinimumSize(QtCore.QSize(0, 50))
        FormContasRecebidas.setStyleSheet("text-transform: uppercase;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:1 rgba(0, 0, 0, 80));")
        self.horizontalLayout = QtWidgets.QHBoxLayout(FormContasRecebidas)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(FormContasRecebidas)
        self.widget.setStyleSheet("text-transform: uppercase;\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:1 rgba(0, 0, 0, 80));")
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.wb_incluirParcelas = QtWidgets.QWidget(self.widget)
        self.wb_incluirParcelas.setMinimumSize(QtCore.QSize(1200, 700))
        self.wb_incluirParcelas.setMaximumSize(QtCore.QSize(900, 700))
        self.wb_incluirParcelas.setStyleSheet("QWidget{\n"
"background-color: rgb(231, 231, 231);\n"
"border:1px solid blue;\n"
"text-transform: uppercase;\n"
"}\n"
"QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:20px;\n"
"    cursor: pointer;\n"
"    background-color: rgb(0, 85, 255);\n"
"padding:15px 15px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}\n"
"")
        self.wb_incluirParcelas.setObjectName("wb_incluirParcelas")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.wb_incluirParcelas)
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_10 = QtWidgets.QFrame(self.wb_incluirParcelas)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_10.setStyleSheet("\n"
"QFrame#frame_10{\n"
"color:red;\n"
"border: none;\n"
"background-color:#2408D4;}\n"
"\n"
"QLabel{color: white;\n"
"background-color:transparent;\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"\n"
"}")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        self.label_5.setMinimumSize(QtCore.QSize(150, 0))
        self.label_5.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_5.setStyleSheet("border:none")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.lb_nome = QtWidgets.QLabel(self.frame_10)
        self.lb_nome.setMinimumSize(QtCore.QSize(0, 20))
        self.lb_nome.setStyleSheet("border:none;")
        self.lb_nome.setText("")
        self.lb_nome.setObjectName("lb_nome")
        self.horizontalLayout_8.addWidget(self.lb_nome)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.wb_incluirParcelas)
        self.frame_11.setStyleSheet("QFrame\n"
"{background: #eaeaea;\n"
"border: none\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color:black;\n"
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
"background-color: rgb(255, 255, 127);\n"
"border:1px solid;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:0px;\n"
"}\n"
"QDoubleSpinBox{\n"
"background-color: rgb(255, 255, 127);\n"
"font-size: 24px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:0px;\n"
"\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_recebidos = QtWidgets.QTableWidget(self.frame_11)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.tab_recebidos.setPalette(palette)
        self.tab_recebidos.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tab_recebidos.setStyleSheet("QTableWidget {\n"
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
        self.tab_recebidos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab_recebidos.setTabKeyNavigation(False)
        self.tab_recebidos.setProperty("showDropIndicator", True)
        self.tab_recebidos.setDragDropOverwriteMode(False)
        self.tab_recebidos.setAlternatingRowColors(False)
        self.tab_recebidos.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tab_recebidos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tab_recebidos.setShowGrid(False)
        self.tab_recebidos.setGridStyle(QtCore.Qt.SolidLine)
        self.tab_recebidos.setObjectName("tab_recebidos")
        self.tab_recebidos.setColumnCount(10)
        self.tab_recebidos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_recebidos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_recebidos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tab_recebidos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_recebidos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_recebidos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_recebidos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_recebidos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_recebidos.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_recebidos.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_recebidos.setHorizontalHeaderItem(9, item)
        self.tab_recebidos.horizontalHeader().setDefaultSectionSize(150)
        self.tab_recebidos.horizontalHeader().setHighlightSections(False)
        self.tab_recebidos.horizontalHeader().setStretchLastSection(False)
        self.tab_recebidos.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tab_recebidos)
        self.frame = QtWidgets.QFrame(self.frame_11)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.db_Nominmal = QtWidgets.QDoubleSpinBox(self.frame)
        self.db_Nominmal.setMinimumSize(QtCore.QSize(500, 50))
        self.db_Nominmal.setFocusPolicy(QtCore.Qt.NoFocus)
        self.db_Nominmal.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 20pt \"Segoe UI\";")
        self.db_Nominmal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_Nominmal.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.db_Nominmal.setProperty("showGroupSeparator", True)
        self.db_Nominmal.setDecimals(4)
        self.db_Nominmal.setMinimum(0.0)
        self.db_Nominmal.setMaximum(1e+19)
        self.db_Nominmal.setProperty("value", 0.0)
        self.db_Nominmal.setObjectName("db_Nominmal")
        self.horizontalLayout_2.addWidget(self.db_Nominmal)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.tx_valorTotalparcela = QtWidgets.QDoubleSpinBox(self.frame)
        self.tx_valorTotalparcela.setMinimumSize(QtCore.QSize(400, 50))
        self.tx_valorTotalparcela.setMaximumSize(QtCore.QSize(380, 16777215))
        self.tx_valorTotalparcela.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tx_valorTotalparcela.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 20pt \"Segoe UI\";")
        self.tx_valorTotalparcela.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_valorTotalparcela.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.tx_valorTotalparcela.setProperty("showGroupSeparator", True)
        self.tx_valorTotalparcela.setDecimals(4)
        self.tx_valorTotalparcela.setMaximum(1e+18)
        self.tx_valorTotalparcela.setObjectName("tx_valorTotalparcela")
        self.horizontalLayout_2.addWidget(self.tx_valorTotalparcela)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_5.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.wb_incluirParcelas)
        self.frame_12.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_12.setStyleSheet("\n"
"QFrame{\n"
"border:none\n"
"}\n"
"")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.bt_SalvarPagamento = QtWidgets.QPushButton(self.frame_12)
        self.bt_SalvarPagamento.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.bt_SalvarPagamento.setFont(font)
        self.bt_SalvarPagamento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_SalvarPagamento.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_SalvarPagamento.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_SalvarPagamento.setStyleSheet("")
        self.bt_SalvarPagamento.setIconSize(QtCore.QSize(75, 35))
        self.bt_SalvarPagamento.setObjectName("bt_SalvarPagamento")
        self.horizontalLayout_10.addWidget(self.bt_SalvarPagamento)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.bt_sairlancamento = QtWidgets.QPushButton(self.frame_12)
        self.bt_sairlancamento.setMinimumSize(QtCore.QSize(0, 50))
        self.bt_sairlancamento.setStyleSheet("QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:20px;\n"
"    cursor: pointer;\n"
"    background-color:red;\n"
"padding:15px 15px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}")
        self.bt_sairlancamento.setObjectName("bt_sairlancamento")
        self.horizontalLayout_10.addWidget(self.bt_sairlancamento)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.horizontalLayout_3.addWidget(self.wb_incluirParcelas)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(FormContasRecebidas)
        QtCore.QMetaObject.connectSlotsByName(FormContasRecebidas)

    def retranslateUi(self, FormContasRecebidas):
        _translate = QtCore.QCoreApplication.translate
        FormContasRecebidas.setWindowTitle(_translate("FormContasRecebidas", "Form"))
        self.label_5.setText(_translate("FormContasRecebidas", "RECEBIBOS"))
        item = self.tab_recebidos.horizontalHeaderItem(0)
        item.setText(_translate("FormContasRecebidas", "NOTAS"))
        item = self.tab_recebidos.horizontalHeaderItem(1)
        item.setText(_translate("FormContasRecebidas", "DOCUMENTO"))
        item = self.tab_recebidos.horizontalHeaderItem(2)
        item.setText(_translate("FormContasRecebidas", "nome"))
        item = self.tab_recebidos.horizontalHeaderItem(3)
        item.setText(_translate("FormContasRecebidas", "VALOR nominal"))
        item = self.tab_recebidos.horizontalHeaderItem(4)
        item.setText(_translate("FormContasRecebidas", "DESCONTO"))
        item = self.tab_recebidos.horizontalHeaderItem(5)
        item.setText(_translate("FormContasRecebidas", "VALOR TOTAL"))
        item = self.tab_recebidos.horizontalHeaderItem(6)
        item.setText(_translate("FormContasRecebidas", "parcela"))
        item = self.tab_recebidos.horizontalHeaderItem(7)
        item.setText(_translate("FormContasRecebidas", "data emissao"))
        item = self.tab_recebidos.horizontalHeaderItem(8)
        item.setText(_translate("FormContasRecebidas", "data vencimento"))
        item = self.tab_recebidos.horizontalHeaderItem(9)
        item.setText(_translate("FormContasRecebidas", "data baixa"))
        self.db_Nominmal.setPrefix(_translate("FormContasRecebidas", "Nominal R$ "))
        self.tx_valorTotalparcela.setPrefix(_translate("FormContasRecebidas", "TOTAL R$ "))
        self.bt_SalvarPagamento.setText(_translate("FormContasRecebidas", "estorna"))
        self.bt_SalvarPagamento.setShortcut(_translate("FormContasRecebidas", "F2"))
        self.bt_sairlancamento.setText(_translate("FormContasRecebidas", "sair"))
        self.bt_sairlancamento.setShortcut(_translate("FormContasRecebidas", "Esc"))
