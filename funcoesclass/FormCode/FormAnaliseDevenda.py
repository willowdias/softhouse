# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormLyoute/FormAnaliseDevenda.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormAnaliseDevenda(object):
    def setupUi(self, FormAnaliseDevenda):
        FormAnaliseDevenda.setObjectName("FormAnaliseDevenda")
        FormAnaliseDevenda.setWindowModality(QtCore.Qt.ApplicationModal)
        FormAnaliseDevenda.resize(1824, 850)
        FormAnaliseDevenda.setStyleSheet("QWidget{text-transform: uppercase;\n"
"\n"
"\n"
"}\n"
"")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(FormAnaliseDevenda)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.widget_2 = QtWidgets.QWidget(FormAnaliseDevenda)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.wb_nomeCliente = QtWidgets.QWidget(self.widget_2)
        self.wb_nomeCliente.setGeometry(QtCore.QRect(1320, 400, 400, 150))
        self.wb_nomeCliente.setMinimumSize(QtCore.QSize(400, 150))
        self.wb_nomeCliente.setMaximumSize(QtCore.QSize(400, 150))
        self.wb_nomeCliente.setStyleSheet("\n"
"QWidget#wb_nomeCliente{\n"
"    background-color: rgb(255, 255, 255);\n"
"border:1px solid blue;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:14px;\n"
"    cursor: pointer;\n"
"background-color: rgb(0, 85, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: black;\n"
"border: none;\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 127);\n"
"font-size: 12px;\n"
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
"    background-color: rgb(255, 255, 127);\n"
"}")
        self.wb_nomeCliente.setObjectName("wb_nomeCliente")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.wb_nomeCliente)
        self.verticalLayout_7.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.wb_nomeCliente)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.tx_nomecliente = QtWidgets.QLineEdit(self.wb_nomeCliente)
        self.tx_nomecliente.setMinimumSize(QtCore.QSize(0, 40))
        self.tx_nomecliente.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.tx_nomecliente.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_nomecliente.setObjectName("tx_nomecliente")
        self.verticalLayout_7.addWidget(self.tx_nomecliente)
        self.frame_10 = QtWidgets.QFrame(self.wb_nomeCliente)
        self.frame_10.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_10.setStyleSheet("border:none")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.bt_consultaCliente = QtWidgets.QPushButton(self.frame_10)
        self.bt_consultaCliente.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.bt_consultaCliente.setFont(font)
        self.bt_consultaCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_consultaCliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_consultaCliente.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_consultaCliente.setStyleSheet("")
        self.bt_consultaCliente.setIconSize(QtCore.QSize(75, 35))
        self.bt_consultaCliente.setObjectName("bt_consultaCliente")
        self.horizontalLayout_10.addWidget(self.bt_consultaCliente)
        self.bt_sairCliente = QtWidgets.QPushButton(self.frame_10)
        self.bt_sairCliente.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.bt_sairCliente.setFont(font)
        self.bt_sairCliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_sairCliente.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.bt_sairCliente.setObjectName("bt_sairCliente")
        self.horizontalLayout_10.addWidget(self.bt_sairCliente)
        self.verticalLayout_7.addWidget(self.frame_10)
        self.frameAnalisePoritem = QtWidgets.QFrame(self.widget_2)
        self.frameAnalisePoritem.setGeometry(QtCore.QRect(1310, 220, 400, 150))
        self.frameAnalisePoritem.setMinimumSize(QtCore.QSize(400, 150))
        self.frameAnalisePoritem.setMaximumSize(QtCore.QSize(400, 150))
        self.frameAnalisePoritem.setStyleSheet("QFrame{text-transform: uppercase;\n"
"background-color: rgb(207, 207, 207);\n"
"    background-color: rgb(255, 255, 255);\n"
"border:1px solid blue;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:14px;\n"
"    cursor: pointer;\n"
"background-color: rgb(0, 85, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: black;\n"
"border: none;\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 127);\n"
"font-size: 12px;\n"
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
"    background-color: rgb(255, 255, 127);\n"
"}")
        self.frameAnalisePoritem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameAnalisePoritem.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameAnalisePoritem.setObjectName("frameAnalisePoritem")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameAnalisePoritem)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.frameAnalisePoritem)
        self.label_15.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.tx_itens = QtWidgets.QLineEdit(self.frameAnalisePoritem)
        self.tx_itens.setMinimumSize(QtCore.QSize(0, 30))
        self.tx_itens.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tx_itens.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.tx_itens.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_itens.setObjectName("tx_itens")
        self.verticalLayout_2.addWidget(self.tx_itens)
        self.frame_3 = QtWidgets.QFrame(self.frameAnalisePoritem)
        self.frame_3.setStyleSheet("border:none")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_confirmaItens = QtWidgets.QPushButton(self.frame_3)
        self.bt_confirmaItens.setMinimumSize(QtCore.QSize(0, 25))
        self.bt_confirmaItens.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bt_confirmaItens.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_confirmaItens.setStyleSheet("")
        self.bt_confirmaItens.setObjectName("bt_confirmaItens")
        self.horizontalLayout.addWidget(self.bt_confirmaItens)
        self.bt_cancelarITens = QtWidgets.QPushButton(self.frame_3)
        self.bt_cancelarITens.setMinimumSize(QtCore.QSize(0, 25))
        self.bt_cancelarITens.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_cancelarITens.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.bt_cancelarITens.setObjectName("bt_cancelarITens")
        self.horizontalLayout.addWidget(self.bt_cancelarITens)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.FrameDataemisao = QtWidgets.QFrame(self.widget_2)
        self.FrameDataemisao.setGeometry(QtCore.QRect(1310, 60, 400, 150))
        self.FrameDataemisao.setMinimumSize(QtCore.QSize(400, 150))
        self.FrameDataemisao.setMaximumSize(QtCore.QSize(400, 200))
        self.FrameDataemisao.setStyleSheet("\n"
"QWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"border:1px solid blue;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:11px;\n"
"    cursor: pointer;\n"
"background-color: rgb(0, 85, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: black;\n"
"border: none;\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 127);\n"
"font-size: 12px;\n"
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
"    background-color: rgb(255, 255, 127);\n"
"}")
        self.FrameDataemisao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameDataemisao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameDataemisao.setObjectName("FrameDataemisao")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.FrameDataemisao)
        self.verticalLayout_3.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.FrameDataemisao)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.frame_7 = QtWidgets.QFrame(self.FrameDataemisao)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_7.setStyleSheet("border:none;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.dt_inicial = QtWidgets.QDateEdit(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dt_inicial.setFont(font)
        self.dt_inicial.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dt_inicial.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.dt_inicial.setCalendarPopup(True)
        self.dt_inicial.setObjectName("dt_inicial")
        self.horizontalLayout_5.addWidget(self.dt_inicial)
        self.label_14 = QtWidgets.QLabel(self.frame_7)
        self.label_14.setMaximumSize(QtCore.QSize(45, 16777215))
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.dt_final = QtWidgets.QDateEdit(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dt_final.setFont(font)
        self.dt_final.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.dt_final.setStyleSheet("background-color: rgb(188, 188, 188);")
        self.dt_final.setCalendarPopup(True)
        self.dt_final.setObjectName("dt_final")
        self.horizontalLayout_5.addWidget(self.dt_final)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_4 = QtWidgets.QFrame(self.FrameDataemisao)
        self.frame_4.setStyleSheet("QFrame{\n"
"border:none;\n"
"}\n"
"QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"    cursor: pointer;\n"
"    background-color:#538fff;\n"
"padding:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bt_ConfirmaDatavenda = QtWidgets.QPushButton(self.frame_4)
        self.bt_ConfirmaDatavenda.setMinimumSize(QtCore.QSize(0, 50))
        self.bt_ConfirmaDatavenda.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_ConfirmaDatavenda.setStyleSheet("")
        self.bt_ConfirmaDatavenda.setObjectName("bt_ConfirmaDatavenda")
        self.horizontalLayout_6.addWidget(self.bt_ConfirmaDatavenda)
        self.bt_cancelarDatavenda = QtWidgets.QPushButton(self.frame_4)
        self.bt_cancelarDatavenda.setMinimumSize(QtCore.QSize(0, 50))
        self.bt_cancelarDatavenda.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_cancelarDatavenda.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.bt_cancelarDatavenda.setObjectName("bt_cancelarDatavenda")
        self.horizontalLayout_6.addWidget(self.bt_cancelarDatavenda)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.wb_NumeroNotas = QtWidgets.QWidget(self.widget_2)
        self.wb_NumeroNotas.setGeometry(QtCore.QRect(1320, 610, 400, 150))
        self.wb_NumeroNotas.setMinimumSize(QtCore.QSize(400, 150))
        self.wb_NumeroNotas.setMaximumSize(QtCore.QSize(400, 150))
        self.wb_NumeroNotas.setStyleSheet("\n"
"QWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"border:1px solid blue;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:14px;\n"
"    cursor: pointer;\n"
"background-color: rgb(0, 85, 255);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}\n"
"\n"
"QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: black;\n"
"border: none;\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 127);\n"
"font-size: 12px;\n"
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
"    background-color: rgb(255, 255, 127);\n"
"}")
        self.wb_NumeroNotas.setObjectName("wb_NumeroNotas")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.wb_NumeroNotas)
        self.verticalLayout_5.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.wb_NumeroNotas)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.tx_numeroNota = QtWidgets.QLineEdit(self.wb_NumeroNotas)
        self.tx_numeroNota.setMinimumSize(QtCore.QSize(0, 40))
        self.tx_numeroNota.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.tx_numeroNota.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_numeroNota.setObjectName("tx_numeroNota")
        self.verticalLayout_5.addWidget(self.tx_numeroNota)
        self.frame_5 = QtWidgets.QFrame(self.wb_NumeroNotas)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setStyleSheet("border:none")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_CosultaNumeronota = QtWidgets.QPushButton(self.frame_5)
        self.bt_CosultaNumeronota.setMinimumSize(QtCore.QSize(0, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.bt_CosultaNumeronota.setFont(font)
        self.bt_CosultaNumeronota.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bt_CosultaNumeronota.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_CosultaNumeronota.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_CosultaNumeronota.setStyleSheet("")
        self.bt_CosultaNumeronota.setIconSize(QtCore.QSize(75, 35))
        self.bt_CosultaNumeronota.setObjectName("bt_CosultaNumeronota")
        self.horizontalLayout_2.addWidget(self.bt_CosultaNumeronota)
        self.bt_notaSair = QtWidgets.QPushButton(self.frame_5)
        self.bt_notaSair.setMinimumSize(QtCore.QSize(0, 31))
        self.bt_notaSair.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_notaSair.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.bt_notaSair.setObjectName("bt_notaSair")
        self.horizontalLayout_2.addWidget(self.bt_notaSair)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.fundo = QtWidgets.QWidget(self.widget_2)
        self.fundo.setGeometry(QtCore.QRect(10, 0, 1301, 700))
        self.fundo.setMinimumSize(QtCore.QSize(0, 0))
        self.fundo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.fundo.setStyleSheet("QWidget#fundo{\n"
"text-transform: uppercase;\n"
"border:1px solid blue;\n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.fundo.setObjectName("fundo")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.fundo)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.fundo)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setStyleSheet("QFrame#frame{\n"
"color:red;\n"
"border: none;\n"
"text-transform: uppercase;\n"
"background-color:#2408D4;}\n"
"\n"
"QLabel{color: white;\n"
"background-color:transparent;\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"text-transform: uppercase;\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame)
        self.tb_analiseVenda = QtWidgets.QTableWidget(self.fundo)
        self.tb_analiseVenda.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tb_analiseVenda.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tb_analiseVenda.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tb_analiseVenda.setStyleSheet("QTableWidget {\n"
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
"}")
        self.tb_analiseVenda.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_analiseVenda.setTabKeyNavigation(False)
        self.tb_analiseVenda.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tb_analiseVenda.setShowGrid(False)
        self.tb_analiseVenda.setGridStyle(QtCore.Qt.NoPen)
        self.tb_analiseVenda.setObjectName("tb_analiseVenda")
        self.tb_analiseVenda.setColumnCount(5)
        self.tb_analiseVenda.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tb_analiseVenda.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_analiseVenda.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_analiseVenda.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_analiseVenda.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tb_analiseVenda.setHorizontalHeaderItem(4, item)
        self.tb_analiseVenda.horizontalHeader().setDefaultSectionSize(250)
        self.tb_analiseVenda.horizontalHeader().setHighlightSections(False)
        self.tb_analiseVenda.horizontalHeader().setStretchLastSection(False)
        self.tb_analiseVenda.verticalHeader().setVisible(False)
        self.tb_analiseVenda.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.tb_analiseVenda)
        self.frame_2 = QtWidgets.QFrame(self.fundo)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 120))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
"background-color: rgb(85, 170, 255,150);\n"
"}\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setStyleSheet("QPushButton{\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:14px;\n"
"    cursor: pointer;\n"
"background-color: rgb(0, 85, 255);\n"
"padding:15px\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bt_clientes = QtWidgets.QPushButton(self.widget)
        self.bt_clientes.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_clientes.setObjectName("bt_clientes")
        self.horizontalLayout_4.addWidget(self.bt_clientes)
        self.bt_notas = QtWidgets.QPushButton(self.widget)
        self.bt_notas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_notas.setObjectName("bt_notas")
        self.horizontalLayout_4.addWidget(self.bt_notas)
        self.bt_emissao = QtWidgets.QPushButton(self.widget)
        self.bt_emissao.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_emissao.setObjectName("bt_emissao")
        self.horizontalLayout_4.addWidget(self.bt_emissao)
        self.bt_itens = QtWidgets.QPushButton(self.widget)
        self.bt_itens.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_itens.setObjectName("bt_itens")
        self.horizontalLayout_4.addWidget(self.bt_itens)
        self.bt_Geral = QtWidgets.QPushButton(self.widget)
        self.bt_Geral.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_Geral.setObjectName("bt_Geral")
        self.horizontalLayout_4.addWidget(self.bt_Geral)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.frame_6 = QtWidgets.QFrame(self.widget)
        self.frame_6.setMinimumSize(QtCore.QSize(300, 82))
        self.frame_6.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_6.setStyleSheet("QLabel{\n"
"font-size: 10px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: black;\n"
"border: none;\n"
"}\n"
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
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.db_total = QtWidgets.QDoubleSpinBox(self.frame_6)
        self.db_total.setMinimumSize(QtCore.QSize(250, 35))
        self.db_total.setSizeIncrement(QtCore.QSize(250, 0))
        self.db_total.setFocusPolicy(QtCore.Qt.NoFocus)
        self.db_total.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.db_total.setFrame(False)
        self.db_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_total.setReadOnly(True)
        self.db_total.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.db_total.setProperty("showGroupSeparator", True)
        self.db_total.setMaximum(999999999999.0)
        self.db_total.setObjectName("db_total")
        self.verticalLayout_4.addWidget(self.db_total)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.horizontalLayout_7.addWidget(self.widget)
        self.verticalLayout.addWidget(self.frame_2)
        self.fundo.raise_()
        self.wb_nomeCliente.raise_()
        self.frameAnalisePoritem.raise_()
        self.FrameDataemisao.raise_()
        self.wb_NumeroNotas.raise_()
        self.horizontalLayout_8.addWidget(self.widget_2)

        self.retranslateUi(FormAnaliseDevenda)
        QtCore.QMetaObject.connectSlotsByName(FormAnaliseDevenda)

    def retranslateUi(self, FormAnaliseDevenda):
        _translate = QtCore.QCoreApplication.translate
        FormAnaliseDevenda.setWindowTitle(_translate("FormAnaliseDevenda", "Form"))
        self.label_9.setText(_translate("FormAnaliseDevenda", "busca por nome cliente"))
        self.tx_nomecliente.setPlaceholderText(_translate("FormAnaliseDevenda", "digite nome"))
        self.bt_consultaCliente.setText(_translate("FormAnaliseDevenda", "consulta (F2)"))
        self.bt_consultaCliente.setShortcut(_translate("FormAnaliseDevenda", "F2"))
        self.bt_sairCliente.setText(_translate("FormAnaliseDevenda", "sair"))
        self.bt_sairCliente.setShortcut(_translate("FormAnaliseDevenda", "Esc"))
        self.label_15.setText(_translate("FormAnaliseDevenda", "buscar por item"))
        self.tx_itens.setPlaceholderText(_translate("FormAnaliseDevenda", "itens"))
        self.bt_confirmaItens.setText(_translate("FormAnaliseDevenda", "confirma (F2)"))
        self.bt_confirmaItens.setShortcut(_translate("FormAnaliseDevenda", "F2"))
        self.bt_cancelarITens.setText(_translate("FormAnaliseDevenda", "cancelar"))
        self.label_3.setText(_translate("FormAnaliseDevenda", "analise venda data"))
        self.label_5.setText(_translate("FormAnaliseDevenda", "entre:"))
        self.label_14.setText(_translate("FormAnaliseDevenda", "ate:"))
        self.bt_ConfirmaDatavenda.setText(_translate("FormAnaliseDevenda", "confirma (F2)"))
        self.bt_ConfirmaDatavenda.setShortcut(_translate("FormAnaliseDevenda", "F2"))
        self.bt_cancelarDatavenda.setText(_translate("FormAnaliseDevenda", "cancelar"))
        self.label_6.setText(_translate("FormAnaliseDevenda", "busca por numero nota"))
        self.tx_numeroNota.setPlaceholderText(_translate("FormAnaliseDevenda", "digite numero notas"))
        self.bt_CosultaNumeronota.setText(_translate("FormAnaliseDevenda", "consulta"))
        self.bt_notaSair.setText(_translate("FormAnaliseDevenda", "sair"))
        self.bt_notaSair.setShortcut(_translate("FormAnaliseDevenda", "Esc"))
        self.label_2.setText(_translate("FormAnaliseDevenda", "analises de vendas"))
        item = self.tb_analiseVenda.horizontalHeaderItem(0)
        item.setText(_translate("FormAnaliseDevenda", "nota"))
        item = self.tb_analiseVenda.horizontalHeaderItem(1)
        item.setText(_translate("FormAnaliseDevenda", "descriçao"))
        item = self.tb_analiseVenda.horizontalHeaderItem(2)
        item.setText(_translate("FormAnaliseDevenda", "valor"))
        item = self.tb_analiseVenda.horizontalHeaderItem(3)
        item.setText(_translate("FormAnaliseDevenda", "data emissao"))
        self.bt_clientes.setText(_translate("FormAnaliseDevenda", "clientes"))
        self.bt_notas.setText(_translate("FormAnaliseDevenda", "notas"))
        self.bt_emissao.setText(_translate("FormAnaliseDevenda", "emissao"))
        self.bt_itens.setText(_translate("FormAnaliseDevenda", "item"))
        self.bt_Geral.setText(_translate("FormAnaliseDevenda", "GERAL"))
        self.label_4.setText(_translate("FormAnaliseDevenda", "valor total"))
        self.db_total.setPrefix(_translate("FormAnaliseDevenda", "R$ "))
