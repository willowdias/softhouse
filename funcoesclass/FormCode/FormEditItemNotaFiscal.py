# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormLyoute/FormEditItemNotaFiscal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormEditItemNotaFiscal(object):
    def setupUi(self, FormEditItemNotaFiscal):
        FormEditItemNotaFiscal.setObjectName("FormEditItemNotaFiscal")
        FormEditItemNotaFiscal.resize(1504, 836)
        FormEditItemNotaFiscal.setStyleSheet("QWidget{text-transform: uppercase;\n"
"    background-color: rgb(0, 0, 0,200);\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(FormEditItemNotaFiscal)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(FormEditItemNotaFiscal)
        self.widget.setStyleSheet("QWidget#widget{text-transform: uppercase;\n"
"    background-color: rgb(0, 0, 0,200);\n"
"}")
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(1200, 800))
        self.widget_2.setMaximumSize(QtCore.QSize(1200, 800))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
"border:1px solid blue;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.widget_2)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 80))
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
        self.verticalLayout_3.addWidget(self.frame_4)
        self.tabWidget = QtWidgets.QTabWidget(self.widget_2)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid #C2C7CB;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"    border: 2px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"    border-bottom-color: #C2C7CB; /* same as pane color */\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"QWidget{\n"
"text-transform: uppercase;\n"
"border:0px solid blue;\n"
"    background-color: rgb(212, 212, 212);\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"    background: #FFF;\n"
"boder:3px solid;\n"
"}\n"
"QLineEdit:focus{\n"
"    background-color: rgb(226, 226, 226);\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"\n"
"text-transform: uppercase;\n"
"font-size: 12px;\n"
"font-family: \"Arial Unicode MS\";\n"
"font-weight: bold;\n"
"color: black;\n"
"    \n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QDoubleSpinBox{\n"
"    background: #FFF;\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 0, 0);\n"
"border:none;\n"
"border-bottom-left-radius:0px;\n"
"border-bottom-right-radius:0px;\n"
"border-top-left-radius:0px;\n"
"}\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.dadosproduto = QtWidgets.QWidget()
        self.dadosproduto.setStyleSheet("")
        self.dadosproduto.setObjectName("dadosproduto")
        self.label_16 = QtWidgets.QLabel(self.dadosproduto)
        self.label_16.setGeometry(QtCore.QRect(20, 0, 51, 21))
        self.label_16.setObjectName("label_16")
        self.tx_tipoDeUnidade = QtWidgets.QLineEdit(self.dadosproduto)
        self.tx_tipoDeUnidade.setGeometry(QtCore.QRect(690, 80, 71, 31))
        self.tx_tipoDeUnidade.setMaxLength(2)
        self.tx_tipoDeUnidade.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_tipoDeUnidade.setObjectName("tx_tipoDeUnidade")
        self.label_3 = QtWidgets.QLabel(self.dadosproduto)
        self.label_3.setGeometry(QtCore.QRect(680, 50, 61, 21))
        self.label_3.setObjectName("label_3")
        self.TX_IDpRODUTO = QtWidgets.QLineEdit(self.dadosproduto)
        self.TX_IDpRODUTO.setGeometry(QtCore.QRect(20, 30, 101, 31))
        self.TX_IDpRODUTO.setFocusPolicy(QtCore.Qt.NoFocus)
        self.TX_IDpRODUTO.setAlignment(QtCore.Qt.AlignCenter)
        self.TX_IDpRODUTO.setObjectName("TX_IDpRODUTO")
        self.tx_Fornecedor = QtWidgets.QLineEdit(self.dadosproduto)
        self.tx_Fornecedor.setGeometry(QtCore.QRect(380, 120, 211, 31))
        self.tx_Fornecedor.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tx_Fornecedor.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_Fornecedor.setObjectName("tx_Fornecedor")
        self.tx_MarcaProduto = QtWidgets.QLineEdit(self.dadosproduto)
        self.tx_MarcaProduto.setGeometry(QtCore.QRect(90, 120, 201, 31))
        self.tx_MarcaProduto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tx_MarcaProduto.setText("")
        self.tx_MarcaProduto.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_MarcaProduto.setObjectName("tx_MarcaProduto")
        self.tx_DescricaoGrupo = QtWidgets.QLineEdit(self.dadosproduto)
        self.tx_DescricaoGrupo.setGeometry(QtCore.QRect(700, 120, 191, 31))
        self.tx_DescricaoGrupo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tx_DescricaoGrupo.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_DescricaoGrupo.setObjectName("tx_DescricaoGrupo")
        self.tx_codGrupo = QtWidgets.QLineEdit(self.dadosproduto)
        self.tx_codGrupo.setGeometry(QtCore.QRect(610, 120, 91, 31))
        self.tx_codGrupo.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(231, 231, 231);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 9pt \"MS Shell Dlg 2\";\n"
"border:0px solid\n"
"\n"
" }\n"
"QLineEdit:hover{\n"
"background-color: #40a286\n"
"}")
        self.tx_codGrupo.setText("")
        self.tx_codGrupo.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_codGrupo.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.tx_codGrupo.setObjectName("tx_codGrupo")
        self.label_8 = QtWidgets.QLabel(self.dadosproduto)
        self.label_8.setGeometry(QtCore.QRect(610, 250, 111, 21))
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.tx_valorVenda = QtWidgets.QDoubleSpinBox(self.dadosproduto)
        self.tx_valorVenda.setGeometry(QtCore.QRect(740, 250, 131, 31))
        self.tx_valorVenda.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tx_valorVenda.setStyleSheet("")
        self.tx_valorVenda.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_valorVenda.setReadOnly(False)
        self.tx_valorVenda.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.tx_valorVenda.setProperty("showGroupSeparator", True)
        self.tx_valorVenda.setDecimals(3)
        self.tx_valorVenda.setMaximum(999999.0)
        self.tx_valorVenda.setSingleStep(1.0)
        self.tx_valorVenda.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.tx_valorVenda.setObjectName("tx_valorVenda")
        self.label_2 = QtWidgets.QLabel(self.dadosproduto)
        self.label_2.setGeometry(QtCore.QRect(150, 0, 121, 21))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.dadosproduto)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 111, 21))
        self.label_4.setObjectName("label_4")
        self.tx_DescricaoProduto = QtWidgets.QLineEdit(self.dadosproduto)
        self.tx_DescricaoProduto.setGeometry(QtCore.QRect(20, 80, 661, 31))
        self.tx_DescricaoProduto.setStyleSheet("")
        self.tx_DescricaoProduto.setObjectName("tx_DescricaoProduto")
        self.tx_codigoBarra = QtWidgets.QLineEdit(self.dadosproduto)
        self.tx_codigoBarra.setGeometry(QtCore.QRect(140, 30, 131, 31))
        self.tx_codigoBarra.setMaxLength(15)
        self.tx_codigoBarra.setObjectName("tx_codigoBarra")
        self.label_9 = QtWidgets.QLabel(self.dadosproduto)
        self.label_9.setGeometry(QtCore.QRect(330, 210, 133, 18))
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.db_compra = QtWidgets.QDoubleSpinBox(self.dadosproduto)
        self.db_compra.setGeometry(QtCore.QRect(470, 200, 133, 29))
        self.db_compra.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.db_compra.setWrapping(False)
        self.db_compra.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_compra.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.db_compra.setProperty("showGroupSeparator", True)
        self.db_compra.setMaximum(99999.0)
        self.db_compra.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.db_compra.setObjectName("db_compra")
        self.label_10 = QtWidgets.QLabel(self.dadosproduto)
        self.label_10.setGeometry(QtCore.QRect(330, 240, 133, 18))
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.db_custo = QtWidgets.QDoubleSpinBox(self.dadosproduto)
        self.db_custo.setGeometry(QtCore.QRect(470, 240, 133, 29))
        self.db_custo.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.db_custo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_custo.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.db_custo.setProperty("showGroupSeparator", True)
        self.db_custo.setMaximum(99999.0)
        self.db_custo.setObjectName("db_custo")
        self.label_11 = QtWidgets.QLabel(self.dadosproduto)
        self.label_11.setGeometry(QtCore.QRect(330, 280, 121, 18))
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.db_lucro = QtWidgets.QDoubleSpinBox(self.dadosproduto)
        self.db_lucro.setGeometry(QtCore.QRect(470, 280, 133, 29))
        self.db_lucro.setFocusPolicy(QtCore.Qt.NoFocus)
        self.db_lucro.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_lucro.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.db_lucro.setProperty("showGroupSeparator", True)
        self.db_lucro.setMaximum(99999.0)
        self.db_lucro.setObjectName("db_lucro")
        self.label_6 = QtWidgets.QLabel(self.dadosproduto)
        self.label_6.setGeometry(QtCore.QRect(20, 210, 143, 14))
        self.label_6.setObjectName("label_6")
        self.tx_QuantidadeProduto = QtWidgets.QDoubleSpinBox(self.dadosproduto)
        self.tx_QuantidadeProduto.setGeometry(QtCore.QRect(150, 200, 143, 29))
        self.tx_QuantidadeProduto.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tx_QuantidadeProduto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_QuantidadeProduto.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.tx_QuantidadeProduto.setProperty("showGroupSeparator", True)
        self.tx_QuantidadeProduto.setMaximum(99999.0)
        self.tx_QuantidadeProduto.setObjectName("tx_QuantidadeProduto")
        self.label_13 = QtWidgets.QLabel(self.dadosproduto)
        self.label_13.setGeometry(QtCore.QRect(20, 250, 121, 16))
        self.label_13.setObjectName("label_13")
        self.tx_maximoproduto = QtWidgets.QLineEdit(self.dadosproduto)
        self.tx_maximoproduto.setGeometry(QtCore.QRect(150, 240, 143, 24))
        self.tx_maximoproduto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_maximoproduto.setObjectName("tx_maximoproduto")
        self.label_14 = QtWidgets.QLabel(self.dadosproduto)
        self.label_14.setGeometry(QtCore.QRect(20, 290, 143, 14))
        self.label_14.setObjectName("label_14")
        self.tx_minimoProduto = QtWidgets.QLineEdit(self.dadosproduto)
        self.tx_minimoProduto.setGeometry(QtCore.QRect(150, 280, 143, 24))
        self.tx_minimoProduto.setMaxLength(10)
        self.tx_minimoProduto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_minimoProduto.setObjectName("tx_minimoProduto")
        self.tx_codfornecedo = QtWidgets.QLineEdit(self.dadosproduto)
        self.tx_codfornecedo.setGeometry(QtCore.QRect(310, 120, 71, 31))
        self.tx_codfornecedo.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(231, 231, 231);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 9pt \"MS Shell Dlg 2\";\n"
"border:0px solid\n"
" }\n"
"QLineEdit:hover{\n"
"background-color: #40a286\n"
"}")
        self.tx_codfornecedo.setText("")
        self.tx_codfornecedo.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_codfornecedo.setObjectName("tx_codfornecedo")
        self.tx_codmarca = QtWidgets.QLineEdit(self.dadosproduto)
        self.tx_codmarca.setGeometry(QtCore.QRect(20, 120, 71, 31))
        self.tx_codmarca.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(231, 231, 231);\n"
"    color: rgb(0, 0, 0);\n"
"    font: 9pt \"MS Shell Dlg 2\";\n"
"\n"
"border:0px solid\n"
" }\n"
"QLineEdit:hover{\n"
"background-color: #40a286\n"
"}")
        self.tx_codmarca.setText("")
        self.tx_codmarca.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_codmarca.setObjectName("tx_codmarca")
        self.label_20 = QtWidgets.QLabel(self.dadosproduto)
        self.label_20.setGeometry(QtCore.QRect(330, 320, 121, 18))
        self.label_20.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_20.setObjectName("label_20")
        self.db_lucroreal = QtWidgets.QDoubleSpinBox(self.dadosproduto)
        self.db_lucroreal.setGeometry(QtCore.QRect(470, 320, 133, 29))
        self.db_lucroreal.setFocusPolicy(QtCore.Qt.NoFocus)
        self.db_lucroreal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_lucroreal.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.db_lucroreal.setProperty("showGroupSeparator", True)
        self.db_lucroreal.setMaximum(99999.0)
        self.db_lucroreal.setObjectName("db_lucroreal")
        self.label_21 = QtWidgets.QLabel(self.dadosproduto)
        self.label_21.setGeometry(QtCore.QRect(610, 200, 111, 21))
        self.label_21.setStyleSheet("")
        self.label_21.setObjectName("label_21")
        self.tx_porcentagemvenda = QtWidgets.QDoubleSpinBox(self.dadosproduto)
        self.tx_porcentagemvenda.setGeometry(QtCore.QRect(740, 200, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.tx_porcentagemvenda.setFont(font)
        self.tx_porcentagemvenda.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tx_porcentagemvenda.setStyleSheet("")
        self.tx_porcentagemvenda.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_porcentagemvenda.setReadOnly(False)
        self.tx_porcentagemvenda.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.tx_porcentagemvenda.setProperty("showGroupSeparator", True)
        self.tx_porcentagemvenda.setDecimals(3)
        self.tx_porcentagemvenda.setMaximum(999999.0)
        self.tx_porcentagemvenda.setSingleStep(1.0)
        self.tx_porcentagemvenda.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.tx_porcentagemvenda.setObjectName("tx_porcentagemvenda")
        self.label_15 = QtWidgets.QLabel(self.dadosproduto)
        self.label_15.setGeometry(QtCore.QRect(20, 340, 81, 16))
        self.label_15.setObjectName("label_15")
        self.tx_ncm = QtWidgets.QLineEdit(self.dadosproduto)
        self.tx_ncm.setGeometry(QtCore.QRect(130, 340, 143, 24))
        self.tx_ncm.setMaxLength(8)
        self.tx_ncm.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_ncm.setObjectName("tx_ncm")
        self.tx_fracaoPRoduto = QtWidgets.QLineEdit(self.dadosproduto)
        self.tx_fracaoPRoduto.setGeometry(QtCore.QRect(130, 380, 143, 24))
        self.tx_fracaoPRoduto.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tx_fracaoPRoduto.setMaxLength(2)
        self.tx_fracaoPRoduto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tx_fracaoPRoduto.setPlaceholderText("")
        self.tx_fracaoPRoduto.setObjectName("tx_fracaoPRoduto")
        self.label_7 = QtWidgets.QLabel(self.dadosproduto)
        self.label_7.setGeometry(QtCore.QRect(20, 380, 81, 16))
        self.label_7.setObjectName("label_7")
        self.db_pisCusto = QtWidgets.QDoubleSpinBox(self.dadosproduto)
        self.db_pisCusto.setGeometry(QtCore.QRect(130, 420, 141, 31))
        self.db_pisCusto.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.db_pisCusto.setWrapping(False)
        self.db_pisCusto.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.db_pisCusto.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.db_pisCusto.setProperty("showGroupSeparator", True)
        self.db_pisCusto.setPrefix("")
        self.db_pisCusto.setMaximum(99999.0)
        self.db_pisCusto.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.db_pisCusto.setObjectName("db_pisCusto")
        self.label_12 = QtWidgets.QLabel(self.dadosproduto)
        self.label_12.setGeometry(QtCore.QRect(20, 430, 101, 16))
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_4.raise_()
        self.label_16.raise_()
        self.tx_tipoDeUnidade.raise_()
        self.label_3.raise_()
        self.TX_IDpRODUTO.raise_()
        self.tx_Fornecedor.raise_()
        self.tx_MarcaProduto.raise_()
        self.tx_DescricaoGrupo.raise_()
        self.tx_codGrupo.raise_()
        self.label_8.raise_()
        self.tx_valorVenda.raise_()
        self.label_2.raise_()
        self.tx_DescricaoProduto.raise_()
        self.tx_codigoBarra.raise_()
        self.label_9.raise_()
        self.db_compra.raise_()
        self.label_10.raise_()
        self.db_custo.raise_()
        self.label_11.raise_()
        self.db_lucro.raise_()
        self.label_6.raise_()
        self.tx_QuantidadeProduto.raise_()
        self.label_13.raise_()
        self.tx_maximoproduto.raise_()
        self.label_14.raise_()
        self.tx_minimoProduto.raise_()
        self.tx_codfornecedo.raise_()
        self.tx_codmarca.raise_()
        self.label_20.raise_()
        self.db_lucroreal.raise_()
        self.label_21.raise_()
        self.tx_porcentagemvenda.raise_()
        self.label_15.raise_()
        self.tx_ncm.raise_()
        self.tx_fracaoPRoduto.raise_()
        self.label_7.raise_()
        self.db_pisCusto.raise_()
        self.label_12.raise_()
        self.tabWidget.addTab(self.dadosproduto, "")
        self.tributos = QtWidgets.QWidget()
        self.tributos.setObjectName("tributos")
        self.label_17 = QtWidgets.QLabel(self.tributos)
        self.label_17.setGeometry(QtCore.QRect(10, 90, 111, 16))
        self.label_17.setObjectName("label_17")
        self.tx_cfopSaida = QtWidgets.QLineEdit(self.tributos)
        self.tx_cfopSaida.setGeometry(QtCore.QRect(110, 90, 101, 21))
        self.tx_cfopSaida.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tx_cfopSaida.setMaxLength(4)
        self.tx_cfopSaida.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_cfopSaida.setObjectName("tx_cfopSaida")
        self.tx_CstSaida = QtWidgets.QLineEdit(self.tributos)
        self.tx_CstSaida.setGeometry(QtCore.QRect(110, 120, 101, 21))
        self.tx_CstSaida.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tx_CstSaida.setText("")
        self.tx_CstSaida.setMaxLength(4)
        self.tx_CstSaida.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_CstSaida.setObjectName("tx_CstSaida")
        self.cb_classificacao = QtWidgets.QComboBox(self.tributos)
        self.cb_classificacao.setGeometry(QtCore.QRect(40, 30, 231, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        self.cb_classificacao.setFont(font)
        self.cb_classificacao.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.cb_classificacao.setObjectName("cb_classificacao")
        self.cb_classificacao.addItem("")
        self.cb_classificacao.setItemText(0, "")
        self.label_18 = QtWidgets.QLabel(self.tributos)
        self.label_18.setGeometry(QtCore.QRect(40, 10, 211, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tributos)
        self.label_19.setGeometry(QtCore.QRect(10, 120, 101, 20))
        self.label_19.setObjectName("label_19")
        self.tx_codst = QtWidgets.QLineEdit(self.tributos)
        self.tx_codst.setGeometry(QtCore.QRect(10, 30, 31, 31))
        self.tx_codst.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tx_codst.setMaxLength(1)
        self.tx_codst.setObjectName("tx_codst")
        self.tabWidget.addTab(self.tributos, "")
        self.fotos = QtWidgets.QWidget()
        self.fotos.setObjectName("fotos")
        self.lb_fotos_estoque = QtWidgets.QLabel(self.fotos)
        self.lb_fotos_estoque.setGeometry(QtCore.QRect(20, 10, 551, 411))
        self.lb_fotos_estoque.setStyleSheet("background-color:#538fff;")
        self.lb_fotos_estoque.setText("")
        self.lb_fotos_estoque.setPixmap(QtGui.QPixmap(":/newPrefix/img/profile.png"))
        self.lb_fotos_estoque.setScaledContents(True)
        self.lb_fotos_estoque.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_fotos_estoque.setObjectName("lb_fotos_estoque")
        self.bt_selecionar_foto = QtWidgets.QPushButton(self.fotos)
        self.bt_selecionar_foto.setGeometry(QtCore.QRect(40, 360, 41, 41))
        self.bt_selecionar_foto.setMinimumSize(QtCore.QSize(35, 35))
        self.bt_selecionar_foto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_selecionar_foto.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.bt_selecionar_foto.setStyleSheet("QPushButton{\n"
"\n"
"    color:#fff;\n"
"    border:0px;\n"
"    border-radius:20px;\n"
"    font-size:20px;\n"
"    cursor: pointer;\n"
"background-color: #7AB32E;\n"
"    margin:0px\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"}\n"
"\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/mais.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_selecionar_foto.setIcon(icon)
        self.bt_selecionar_foto.setIconSize(QtCore.QSize(30, 30))
        self.bt_selecionar_foto.setObjectName("bt_selecionar_foto")
        self.tabWidget.addTab(self.fotos, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.frame_2 = QtWidgets.QFrame(self.widget_2)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 80))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.frame_2.setStyleSheet("QFrame{\n"
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
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_salva = QtWidgets.QPushButton(self.frame_2)
        self.bt_salva.setMinimumSize(QtCore.QSize(150, 0))
        self.bt_salva.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_salva.setObjectName("bt_salva")
        self.horizontalLayout.addWidget(self.bt_salva)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bt_sair = QtWidgets.QPushButton(self.frame_2)
        self.bt_sair.setMinimumSize(QtCore.QSize(150, 0))
        self.bt_sair.setFocusPolicy(QtCore.Qt.NoFocus)
        self.bt_sair.setObjectName("bt_sair")
        self.horizontalLayout.addWidget(self.bt_sair)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.horizontalLayout_2.addWidget(self.widget_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(FormEditItemNotaFiscal)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FormEditItemNotaFiscal)
        FormEditItemNotaFiscal.setTabOrder(self.bt_sair, self.bt_salva)

    def retranslateUi(self, FormEditItemNotaFiscal):
        _translate = QtCore.QCoreApplication.translate
        FormEditItemNotaFiscal.setWindowTitle(_translate("FormEditItemNotaFiscal", "editaITem"))
        self.label.setText(_translate("FormEditItemNotaFiscal", "entrada de nota"))
        self.label_16.setText(_translate("FormEditItemNotaFiscal", "ID"))
        self.tx_tipoDeUnidade.setText(_translate("FormEditItemNotaFiscal", "un"))
        self.tx_tipoDeUnidade.setPlaceholderText(_translate("FormEditItemNotaFiscal", "unidade"))
        self.label_3.setText(_translate("FormEditItemNotaFiscal", "unidade"))
        self.TX_IDpRODUTO.setPlaceholderText(_translate("FormEditItemNotaFiscal", "id"))
        self.tx_Fornecedor.setPlaceholderText(_translate("FormEditItemNotaFiscal", "fornecedor"))
        self.tx_MarcaProduto.setPlaceholderText(_translate("FormEditItemNotaFiscal", "marca"))
        self.tx_DescricaoGrupo.setPlaceholderText(_translate("FormEditItemNotaFiscal", "grupo"))
        self.tx_codGrupo.setPlaceholderText(_translate("FormEditItemNotaFiscal", "codproduto"))
        self.label_8.setText(_translate("FormEditItemNotaFiscal", "valor de venda"))
        self.tx_valorVenda.setPrefix(_translate("FormEditItemNotaFiscal", "R$ "))
        self.label_2.setText(_translate("FormEditItemNotaFiscal", "CODIGO BARRA"))
        self.label_4.setText(_translate("FormEditItemNotaFiscal", "Descriçao*"))
        self.tx_DescricaoProduto.setPlaceholderText(_translate("FormEditItemNotaFiscal", "descriçao produto"))
        self.tx_codigoBarra.setPlaceholderText(_translate("FormEditItemNotaFiscal", "codigo barra"))
        self.label_9.setText(_translate("FormEditItemNotaFiscal", "preço compra"))
        self.db_compra.setPrefix(_translate("FormEditItemNotaFiscal", "R$ "))
        self.label_10.setText(_translate("FormEditItemNotaFiscal", "preço custo"))
        self.db_custo.setPrefix(_translate("FormEditItemNotaFiscal", "R$ "))
        self.label_11.setText(_translate("FormEditItemNotaFiscal", "lucro(%)"))
        self.db_lucro.setPrefix(_translate("FormEditItemNotaFiscal", "% "))
        self.label_6.setText(_translate("FormEditItemNotaFiscal", "quant produto"))
        self.label_13.setText(_translate("FormEditItemNotaFiscal", "max produto"))
        self.label_14.setText(_translate("FormEditItemNotaFiscal", "min produto"))
        self.tx_codfornecedo.setPlaceholderText(_translate("FormEditItemNotaFiscal", "codfor"))
        self.tx_codmarca.setPlaceholderText(_translate("FormEditItemNotaFiscal", "codmarc"))
        self.label_20.setText(_translate("FormEditItemNotaFiscal", "lucro real"))
        self.db_lucroreal.setPrefix(_translate("FormEditItemNotaFiscal", "R$ "))
        self.label_21.setText(_translate("FormEditItemNotaFiscal", "porc% venda"))
        self.tx_porcentagemvenda.setPrefix(_translate("FormEditItemNotaFiscal", "R$ "))
        self.label_15.setText(_translate("FormEditItemNotaFiscal", "NCM*"))
        self.tx_fracaoPRoduto.setText(_translate("FormEditItemNotaFiscal", "1"))
        self.label_7.setText(_translate("FormEditItemNotaFiscal", "Fraçao"))
        self.label_12.setText(_translate("FormEditItemNotaFiscal", "calculo pis"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dadosproduto), _translate("FormEditItemNotaFiscal", "dados produto"))
        self.label_17.setText(_translate("FormEditItemNotaFiscal", "cfop saida"))
        self.label_18.setText(_translate("FormEditItemNotaFiscal", "*classificaçao fiscal"))
        self.label_19.setText(_translate("FormEditItemNotaFiscal", "cst saida"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tributos), _translate("FormEditItemNotaFiscal", "TRIBUTOS"))
        self.bt_selecionar_foto.setToolTip(_translate("FormEditItemNotaFiscal", "Selecionar Foto"))
        self.bt_selecionar_foto.setText(_translate("FormEditItemNotaFiscal", "+"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fotos), _translate("FormEditItemNotaFiscal", "fotos"))
        self.bt_salva.setText(_translate("FormEditItemNotaFiscal", "salvar   (f2)"))
        self.bt_salva.setShortcut(_translate("FormEditItemNotaFiscal", "F2"))
        self.bt_sair.setText(_translate("FormEditItemNotaFiscal", "sair"))
        self.bt_sair.setShortcut(_translate("FormEditItemNotaFiscal", "Esc"))