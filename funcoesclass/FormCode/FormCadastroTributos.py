# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormLyoute/FormCadastroTributos.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormCadastroTributos(object):
    def setupUi(self, FormCadastroTributos):
        FormCadastroTributos.setObjectName("FormCadastroTributos")
        FormCadastroTributos.setWindowModality(QtCore.Qt.ApplicationModal)
        FormCadastroTributos.resize(994, 676)
        FormCadastroTributos.setStyleSheet("QWidget{\n"
"\n"
"text-transform: uppercase;\n"
"}\n"
"QLineEdit{\n"
"border:0px;\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
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
"}\n"
"\n"
"QDoubleSpinBox{\n"
"border:0px;\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase;\n"
"}\n"
"QDoubleSpinBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
"\n"
"QComboBox{\n"
"border:none;\n"
"background: #CFCFCF;\n"
"border-radius: 2px;\n"
"color: #000;\n"
"font: 13px \"Arial\" ;\n"
"text-transform: uppercase\n"
"}\n"
"QComboBox:Focus {\n"
"border: 1px solid red;\n"
"}\n"
"\n"
"")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(FormCadastroTributos)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_2 = QtWidgets.QWidget(FormCadastroTributos)
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
"    background-color: rgb(0, 0, 0,200);\n"
"text-transform: uppercase;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setGeometry(QtCore.QRect(180, 40, 691, 531))
        self.widget.setStyleSheet("QWidget{\n"
"text-transform: uppercase;\n"
"border:1px solid blue;\n"
"    background-color: rgb(248, 248, 248);\n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setStyleSheet("QFrame{\n"
"border:none;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fr_TituloEsotuque = QtWidgets.QFrame(self.frame_2)
        self.fr_TituloEsotuque.setMinimumSize(QtCore.QSize(0, 80))
        self.fr_TituloEsotuque.setMaximumSize(QtCore.QSize(16777215, 80))
        self.fr_TituloEsotuque.setStyleSheet("QFrame{\n"
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
        self.fr_TituloEsotuque.setObjectName("fr_TituloEsotuque")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fr_TituloEsotuque)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lb_TituloEstoque = QtWidgets.QLabel(self.fr_TituloEsotuque)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        self.lb_TituloEstoque.setFont(font)
        self.lb_TituloEstoque.setStyleSheet("QFrame#frame_4{\n"
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
        self.lb_TituloEstoque.setObjectName("lb_TituloEstoque")
        self.horizontalLayout.addWidget(self.lb_TituloEstoque)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.fr_TituloEsotuque)
        self.tx_buscarTributo = QtWidgets.QLineEdit(self.frame_2)
        self.tx_buscarTributo.setStyleSheet("QLineEdit{\n"
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
"    background-color: rgb(255, 255, 127,150);\n"
"}\n"
"")
        self.tx_buscarTributo.setObjectName("tx_buscarTributo")
        self.verticalLayout_2.addWidget(self.tx_buscarTributo)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setStyleSheet("QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:12px;\n"
"    cursor: pointer;\n"
"    background-color:#538fff;\n"
"padding:15px 15px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_incluir = QtWidgets.QPushButton(self.frame)
        self.bt_incluir.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_incluir.setObjectName("bt_incluir")
        self.horizontalLayout_2.addWidget(self.bt_incluir)
        self.bt_selecionaAltera = QtWidgets.QPushButton(self.frame)
        self.bt_selecionaAltera.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_selecionaAltera.setObjectName("bt_selecionaAltera")
        self.horizontalLayout_2.addWidget(self.bt_selecionaAltera)
        self.bt_apagar = QtWidgets.QPushButton(self.frame)
        self.bt_apagar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_apagar.setObjectName("bt_apagar")
        self.horizontalLayout_2.addWidget(self.bt_apagar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame)
        self.tab_tributos = QtWidgets.QTableWidget(self.frame_2)
        self.tab_tributos.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tab_tributos.setStyleSheet("QTableWidget {\n"
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
        self.tab_tributos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tab_tributos.setTabKeyNavigation(False)
        self.tab_tributos.setProperty("showDropIndicator", True)
        self.tab_tributos.setDragDropOverwriteMode(False)
        self.tab_tributos.setAlternatingRowColors(True)
        self.tab_tributos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tab_tributos.setObjectName("tab_tributos")
        self.tab_tributos.setColumnCount(4)
        self.tab_tributos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tab_tributos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_tributos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_tributos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tab_tributos.setHorizontalHeaderItem(3, item)
        self.tab_tributos.horizontalHeader().setDefaultSectionSize(150)
        self.tab_tributos.horizontalHeader().setHighlightSections(False)
        self.tab_tributos.horizontalHeader().setStretchLastSection(False)
        self.tab_tributos.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tab_tributos)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.bt_close = QtWidgets.QPushButton(self.frame_3)
        self.bt_close.setMinimumSize(QtCore.QSize(0, 30))
        self.bt_close.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_close.setStyleSheet("\n"
"QFrame{\n"
"border:none\n"
"}\n"
"QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:15px;\n"
"    cursor: pointer;\n"
"    background-color:red;\n"
"padding:15px 15px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}")
        self.bt_close.setObjectName("bt_close")
        self.horizontalLayout_3.addWidget(self.bt_close)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame_2)
        self.wb_Incluirtributos = QtWidgets.QWidget(self.widget_2)
        self.wb_Incluirtributos.setGeometry(QtCore.QRect(240, 180, 491, 271))
        self.wb_Incluirtributos.setMinimumSize(QtCore.QSize(0, 0))
        self.wb_Incluirtributos.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.wb_Incluirtributos.setStyleSheet("QWidget{\n"
"text-transform: uppercase;\n"
"border:1px solid blue;\n"
"    background-color: rgb(248, 248, 248);\n"
"}\n"
"")
        self.wb_Incluirtributos.setObjectName("wb_Incluirtributos")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.wb_Incluirtributos)
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_10 = QtWidgets.QFrame(self.wb_Incluirtributos)
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 45))
        self.frame_10.setStyleSheet("QFrame{\n"
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
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.frame_10)
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.verticalLayout_5.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.wb_Incluirtributos)
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
        self.tx_codst = QtWidgets.QLineEdit(self.frame_11)
        self.tx_codst.setGeometry(QtCore.QRect(10, 30, 51, 31))
        self.tx_codst.setMaxLength(1)
        self.tx_codst.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_codst.setObjectName("tx_codst")
        self.tx_descricaotributo = QtWidgets.QLineEdit(self.frame_11)
        self.tx_descricaotributo.setGeometry(QtCore.QRect(70, 30, 291, 31))
        self.tx_descricaotributo.setObjectName("tx_descricaotributo")
        self.label_6 = QtWidgets.QLabel(self.frame_11)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_11)
        self.label_7.setGeometry(QtCore.QRect(70, 10, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_11)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.label_8.setObjectName("label_8")
        self.tx_aliquota = QtWidgets.QDoubleSpinBox(self.frame_11)
        self.tx_aliquota.setGeometry(QtCore.QRect(10, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.tx_aliquota.setFont(font)
        self.tx_aliquota.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.tx_aliquota.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_aliquota.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.tx_aliquota.setProperty("showGroupSeparator", False)
        self.tx_aliquota.setMaximum(99999.0)
        self.tx_aliquota.setProperty("value", 0.0)
        self.tx_aliquota.setObjectName("tx_aliquota")
        self.tx_id = QtWidgets.QLineEdit(self.frame_11)
        self.tx_id.setGeometry(QtCore.QRect(330, 0, 61, 20))
        self.tx_id.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_id.setObjectName("tx_id")
        self.verticalLayout_5.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.wb_Incluirtributos)
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
"    font-size:15px;\n"
"    cursor: pointer;\n"
"    background-color:red;\n"
"padding:15px 15px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.bt_SalvarPagamento = QtWidgets.QPushButton(self.frame_12)
        self.bt_SalvarPagamento.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.bt_SalvarPagamento.setFont(font)
        self.bt_SalvarPagamento.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_SalvarPagamento.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_SalvarPagamento.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_SalvarPagamento.setStyleSheet("QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:15px;\n"
"    cursor: pointer;\n"
"    background-color:#538fff;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}")
        self.bt_SalvarPagamento.setIconSize(QtCore.QSize(75, 35))
        self.bt_SalvarPagamento.setObjectName("bt_SalvarPagamento")
        self.horizontalLayout_10.addWidget(self.bt_SalvarPagamento)
        self.bt_Altera = QtWidgets.QPushButton(self.frame_12)
        self.bt_Altera.setMinimumSize(QtCore.QSize(0, 30))
        self.bt_Altera.setStyleSheet("QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:15px;\n"
"    cursor: pointer;\n"
"    background-color:#538fff;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}")
        self.bt_Altera.setObjectName("bt_Altera")
        self.horizontalLayout_10.addWidget(self.bt_Altera)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.bt_sairlancamento = QtWidgets.QPushButton(self.frame_12)
        self.bt_sairlancamento.setMinimumSize(QtCore.QSize(0, 30))
        self.bt_sairlancamento.setStyleSheet("")
        self.bt_sairlancamento.setObjectName("bt_sairlancamento")
        self.horizontalLayout_10.addWidget(self.bt_sairlancamento)
        self.verticalLayout_5.addWidget(self.frame_12)
        self.verticalLayout_3.addWidget(self.widget_2)

        self.retranslateUi(FormCadastroTributos)
        self.bt_close.clicked.connect(FormCadastroTributos.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(FormCadastroTributos)

    def retranslateUi(self, FormCadastroTributos):
        _translate = QtCore.QCoreApplication.translate
        FormCadastroTributos.setWindowTitle(_translate("FormCadastroTributos", "Form"))
        self.lb_TituloEstoque.setText(_translate("FormCadastroTributos", "cadastro tributos"))
        self.tx_buscarTributo.setPlaceholderText(_translate("FormCadastroTributos", "pesquisar"))
        self.bt_incluir.setText(_translate("FormCadastroTributos", "incluir"))
        self.bt_selecionaAltera.setText(_translate("FormCadastroTributos", "alterar"))
        self.bt_apagar.setText(_translate("FormCadastroTributos", "apagar"))
        item = self.tab_tributos.horizontalHeaderItem(0)
        item.setText(_translate("FormCadastroTributos", "codst"))
        item = self.tab_tributos.horizontalHeaderItem(1)
        item.setText(_translate("FormCadastroTributos", "descricaçao"))
        item = self.tab_tributos.horizontalHeaderItem(2)
        item.setText(_translate("FormCadastroTributos", "icms"))
        item = self.tab_tributos.horizontalHeaderItem(3)
        item.setText(_translate("FormCadastroTributos", "reg"))
        self.bt_close.setText(_translate("FormCadastroTributos", "sair"))
        self.bt_close.setShortcut(_translate("FormCadastroTributos", "Esc"))
        self.label_5.setText(_translate("FormCadastroTributos", "incluir tributos"))
        self.label_6.setText(_translate("FormCadastroTributos", "codst"))
        self.label_7.setText(_translate("FormCadastroTributos", "descriçao"))
        self.label_8.setText(_translate("FormCadastroTributos", "aliquota"))
        self.bt_SalvarPagamento.setText(_translate("FormCadastroTributos", "SALVAR"))
        self.bt_Altera.setText(_translate("FormCadastroTributos", "alterar"))
        self.bt_sairlancamento.setText(_translate("FormCadastroTributos", "sair"))
        self.bt_sairlancamento.setShortcut(_translate("FormCadastroTributos", "Esc"))
