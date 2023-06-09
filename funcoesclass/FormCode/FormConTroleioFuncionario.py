# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormLyoute/FormConTroleioFuncionario.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormCadasTroFuncionario(object):
    def setupUi(self, FormCadasTroFuncionario):
        FormCadasTroFuncionario.setObjectName("FormCadasTroFuncionario")
        FormCadasTroFuncionario.resize(1210, 849)
        FormCadasTroFuncionario.setStyleSheet("text-transform: uppercase;")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(FormCadasTroFuncionario)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.frameMainClientes = QtWidgets.QFrame(FormCadasTroFuncionario)
        self.frameMainClientes.setMinimumSize(QtCore.QSize(1100, 650))
        self.frameMainClientes.setMaximumSize(QtCore.QSize(1100, 800))
        self.frameMainClientes.setStyleSheet("QFrame#frameMainClientes{\n"
"color:red;\n"
"border: none;\n"
"background-color:#2408D4;}\n"
"\n"
"QLabel{color: white;\n"
"background-color:transparent;\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"\n"
"}")
        self.frameMainClientes.setObjectName("frameMainClientes")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameMainClientes)
        self.verticalLayout_2.setContentsMargins(1, 0, 1, 3)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fr_TituloClientes = QtWidgets.QFrame(self.frameMainClientes)
        self.fr_TituloClientes.setMinimumSize(QtCore.QSize(0, 30))
        self.fr_TituloClientes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fr_TituloClientes.setStyleSheet("QFrame#fr_TituloClientes{\n"
"color:red;\n"
"border: none;\n"
"background-color:#2408D4;}\n"
"QLabel{\n"
"background:none;\n"
"font-size: 25px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"    color: black;\n"
"border: none;\n"
"}\n"
"QLabel{color: white;\n"
"background-color:transparent;\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"\n"
"}")
        self.fr_TituloClientes.setObjectName("fr_TituloClientes")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.fr_TituloClientes)
        self.horizontalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lb_tituloClientes = QtWidgets.QLabel(self.fr_TituloClientes)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lb_tituloClientes.setFont(font)
        self.lb_tituloClientes.setStyleSheet("")
        self.lb_tituloClientes.setObjectName("lb_tituloClientes")
        self.horizontalLayout_3.addWidget(self.lb_tituloClientes)
        self.verticalLayout_2.addWidget(self.fr_TituloClientes)
        self.ct_containerClientes = QtWidgets.QFrame(self.frameMainClientes)
        self.ct_containerClientes.setStyleSheet("border: none")
        self.ct_containerClientes.setObjectName("ct_containerClientes")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ct_containerClientes)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_edita = QtWidgets.QFrame(self.ct_containerClientes)
        self.frame_edita.setStyleSheet("QFrame{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
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
"}\n"
"\n"
"\n"
"")
        self.frame_edita.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_edita.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_edita.setObjectName("frame_edita")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_edita)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 2)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fr_TopoMenuClientes = QtWidgets.QFrame(self.frame_edita)
        self.fr_TopoMenuClientes.setMaximumSize(QtCore.QSize(16777215, 60))
        self.fr_TopoMenuClientes.setStyleSheet("background:#E1DFE0;\n"
"border: none;")
        self.fr_TopoMenuClientes.setObjectName("fr_TopoMenuClientes")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fr_TopoMenuClientes)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2.addWidget(self.fr_TopoMenuClientes)
        self.tx_BuscaFuncionario = QtWidgets.QLineEdit(self.frame_edita)
        self.tx_BuscaFuncionario.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tx_BuscaFuncionario.setFont(font)
        self.tx_BuscaFuncionario.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tx_BuscaFuncionario.setStyleSheet("\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 127);\n"
"font-size: 16px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:0px;\n"
"padding:6px\n"
"}\n"
"QLineEdit:focus{\n"
"    background-color: rgb(226, 226, 226);\n"
"}")
        self.tx_BuscaFuncionario.setFrame(True)
        self.tx_BuscaFuncionario.setObjectName("tx_BuscaFuncionario")
        self.horizontalLayout_2.addWidget(self.tx_BuscaFuncionario)
        self.bt_novo = QtWidgets.QPushButton(self.frame_edita)
        self.bt_novo.setMinimumSize(QtCore.QSize(0, 20))
        self.bt_novo.setObjectName("bt_novo")
        self.horizontalLayout_2.addWidget(self.bt_novo)
        self.Bt_Alterar = QtWidgets.QPushButton(self.frame_edita)
        self.Bt_Alterar.setMinimumSize(QtCore.QSize(0, 20))
        self.Bt_Alterar.setStyleSheet("")
        self.Bt_Alterar.setObjectName("Bt_Alterar")
        self.horizontalLayout_2.addWidget(self.Bt_Alterar)
        self.Bt_excluir = QtWidgets.QPushButton(self.frame_edita)
        self.Bt_excluir.setMinimumSize(QtCore.QSize(0, 20))
        self.Bt_excluir.setObjectName("Bt_excluir")
        self.horizontalLayout_2.addWidget(self.Bt_excluir)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.frame_edita)
        self.Tab_funcionario = QtWidgets.QTableWidget(self.ct_containerClientes)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.Tab_funcionario.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Tab_funcionario.setFont(font)
        self.Tab_funcionario.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Tab_funcionario.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Tab_funcionario.setStyleSheet("QTableWidget {\n"
"  background-color: white;\n"
"    font: 12pt \"MS Shell Dlg 2\";\n"
"    color: rgb(0, 0, 0);\n"
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
        self.Tab_funcionario.setAutoScrollMargin(20)
        self.Tab_funcionario.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Tab_funcionario.setAlternatingRowColors(False)
        self.Tab_funcionario.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Tab_funcionario.setShowGrid(False)
        self.Tab_funcionario.setGridStyle(QtCore.Qt.NoPen)
        self.Tab_funcionario.setWordWrap(True)
        self.Tab_funcionario.setObjectName("Tab_funcionario")
        self.Tab_funcionario.setColumnCount(4)
        self.Tab_funcionario.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.Tab_funcionario.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.Tab_funcionario.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tab_funcionario.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setBackground(QtGui.QColor(255, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.Tab_funcionario.setHorizontalHeaderItem(3, item)
        self.Tab_funcionario.horizontalHeader().setDefaultSectionSize(300)
        self.Tab_funcionario.horizontalHeader().setHighlightSections(True)
        self.Tab_funcionario.horizontalHeader().setSortIndicatorShown(False)
        self.Tab_funcionario.horizontalHeader().setStretchLastSection(False)
        self.Tab_funcionario.verticalHeader().setVisible(False)
        self.Tab_funcionario.verticalHeader().setDefaultSectionSize(50)
        self.Tab_funcionario.verticalHeader().setMinimumSectionSize(20)
        self.verticalLayout_3.addWidget(self.Tab_funcionario)
        self.verticalLayout_2.addWidget(self.ct_containerClientes)
        self.ct_containerClientes.raise_()
        self.fr_TituloClientes.raise_()
        self.horizontalLayout_4.addWidget(self.frameMainClientes)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)

        self.retranslateUi(FormCadasTroFuncionario)
        QtCore.QMetaObject.connectSlotsByName(FormCadasTroFuncionario)

    def retranslateUi(self, FormCadasTroFuncionario):
        _translate = QtCore.QCoreApplication.translate
        FormCadasTroFuncionario.setWindowTitle(_translate("FormCadasTroFuncionario", "ControleioFuncionario"))
        self.lb_tituloClientes.setText(_translate("FormCadasTroFuncionario", "CONTROLEIO de funcionarios"))
        self.tx_BuscaFuncionario.setPlaceholderText(_translate("FormCadasTroFuncionario", "BUSCA funcionario"))
        self.bt_novo.setText(_translate("FormCadasTroFuncionario", "novo funcionario"))
        self.Bt_Alterar.setText(_translate("FormCadasTroFuncionario", "alterar"))
        self.Bt_excluir.setText(_translate("FormCadasTroFuncionario", "excluir"))
        self.Tab_funcionario.setSortingEnabled(False)
        item = self.Tab_funcionario.horizontalHeaderItem(0)
        item.setText(_translate("FormCadasTroFuncionario", "ID"))
        item = self.Tab_funcionario.horizontalHeaderItem(1)
        item.setText(_translate("FormCadasTroFuncionario", "NOME"))
        item = self.Tab_funcionario.horizontalHeaderItem(2)
        item.setText(_translate("FormCadasTroFuncionario", "sobrenome"))
        item = self.Tab_funcionario.horizontalHeaderItem(3)
        item.setText(_translate("FormCadasTroFuncionario", "status"))
