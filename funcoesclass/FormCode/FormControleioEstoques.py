# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FormLyoute/FormControleioEstoque.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormEstoque(object):
    def setupUi(self, FormEstoque):
        FormEstoque.setObjectName("FormEstoque")
        FormEstoque.setWindowModality(QtCore.Qt.NonModal)
        FormEstoque.resize(1261, 827)
        FormEstoque.setStyleSheet("text-transform: uppercase;")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(FormEstoque)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_2 = QtWidgets.QWidget(FormEstoque)
        self.widget_2.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setStyleSheet("QWidget#widget_3{\n"
"border:3px solid blue;\n"
"}")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setContentsMargins(3, 0, 3, 9)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.fr_TituloEsotuque = QtWidgets.QFrame(self.widget_3)
        self.fr_TituloEsotuque.setMinimumSize(QtCore.QSize(0, 80))
        self.fr_TituloEsotuque.setMaximumSize(QtCore.QSize(16777215, 80))
        self.fr_TituloEsotuque.setStyleSheet("QWidget{color:red;\n"
"border: none;\n"
"background-color:#2408D4;}\n"
"QLabel{color: white;\n"
"background-color:transparent;\n"
"font: 75 15pt \"MS Shell Dlg 2\";\n"
"\n"
"text-transform: uppercase;\n"
"}")
        self.fr_TituloEsotuque.setObjectName("fr_TituloEsotuque")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fr_TituloEsotuque)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lb_TituloEstoque = QtWidgets.QLabel(self.fr_TituloEsotuque)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lb_TituloEstoque.setFont(font)
        self.lb_TituloEstoque.setStyleSheet("")
        self.lb_TituloEstoque.setObjectName("lb_TituloEstoque")
        self.verticalLayout_2.addWidget(self.lb_TituloEstoque)
        self.verticalLayout_4.addWidget(self.fr_TituloEsotuque)
        self.framecabecario = QtWidgets.QFrame(self.widget_3)
        self.framecabecario.setMinimumSize(QtCore.QSize(0, 150))
        self.framecabecario.setMaximumSize(QtCore.QSize(16777215, 150))
        self.framecabecario.setStyleSheet("background-color: rgb(249, 249, 249);\n"
"text-transform: uppercase;")
        self.framecabecario.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framecabecario.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framecabecario.setObjectName("framecabecario")
        self.labe = QtWidgets.QLabel(self.framecabecario)
        self.labe.setGeometry(QtCore.QRect(800, 10, 111, 16))
        self.labe.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.labe.setAlignment(QtCore.Qt.AlignCenter)
        self.labe.setObjectName("labe")
        self.tx_QuantidaDeProduto = QtWidgets.QLineEdit(self.framecabecario)
        self.tx_QuantidaDeProduto.setEnabled(False)
        self.tx_QuantidaDeProduto.setGeometry(QtCore.QRect(810, 30, 101, 31))
        self.tx_QuantidaDeProduto.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tx_QuantidaDeProduto.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tx_QuantidaDeProduto.setStyleSheet("font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom:1px solid black;\n"
"")
        self.tx_QuantidaDeProduto.setText("")
        self.tx_QuantidaDeProduto.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_QuantidaDeProduto.setReadOnly(True)
        self.tx_QuantidaDeProduto.setObjectName("tx_QuantidaDeProduto")
        self.labe_2 = QtWidgets.QLabel(self.framecabecario)
        self.labe_2.setGeometry(QtCore.QRect(340, 10, 141, 16))
        self.labe_2.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.labe_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labe_2.setObjectName("labe_2")
        self.tx_descricao = QtWidgets.QLineEdit(self.framecabecario)
        self.tx_descricao.setEnabled(False)
        self.tx_descricao.setGeometry(QtCore.QRect(340, 30, 461, 31))
        self.tx_descricao.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tx_descricao.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tx_descricao.setStyleSheet("font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom:1px solid black;\n"
"")
        self.tx_descricao.setText("")
        self.tx_descricao.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.tx_descricao.setReadOnly(True)
        self.tx_descricao.setPlaceholderText("")
        self.tx_descricao.setObjectName("tx_descricao")
        self.tx_codigoBarra = QtWidgets.QLineEdit(self.framecabecario)
        self.tx_codigoBarra.setEnabled(False)
        self.tx_codigoBarra.setGeometry(QtCore.QRect(130, 30, 191, 31))
        self.tx_codigoBarra.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tx_codigoBarra.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tx_codigoBarra.setStyleSheet("\n"
"font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom:1px solid black;\n"
"\n"
"")
        self.tx_codigoBarra.setText("")
        self.tx_codigoBarra.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_codigoBarra.setReadOnly(True)
        self.tx_codigoBarra.setPlaceholderText("")
        self.tx_codigoBarra.setObjectName("tx_codigoBarra")
        self.labe_3 = QtWidgets.QLabel(self.framecabecario)
        self.labe_3.setGeometry(QtCore.QRect(130, 10, 141, 16))
        self.labe_3.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.labe_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labe_3.setObjectName("labe_3")
        self.lb_fotoitem = QtWidgets.QLabel(self.framecabecario)
        self.lb_fotoitem.setGeometry(QtCore.QRect(20, 9, 100, 100))
        self.lb_fotoitem.setMinimumSize(QtCore.QSize(100, 100))
        self.lb_fotoitem.setMaximumSize(QtCore.QSize(100, 100))
        self.lb_fotoitem.setStyleSheet("")
        self.lb_fotoitem.setText("")
        self.lb_fotoitem.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_fotoitem.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.lb_fotoitem.setObjectName("lb_fotoitem")
        self.tx_BuscarEstoque = QtWidgets.QLineEdit(self.framecabecario)
        self.tx_BuscarEstoque.setGeometry(QtCore.QRect(270, 90, 481, 30))
        self.tx_BuscarEstoque.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tx_BuscarEstoque.setFont(font)
        self.tx_BuscarEstoque.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tx_BuscarEstoque.setStyleSheet("QLineEdit {\n"
"color: #000;\n"
"    font: 14pt \"MS Shell Dlg 2\";\n"
"text-transform: uppercase;\n"
"    background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QLineEdit:focus{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:1 rgba(255, 255, 255, 111));\n"
"}\n"
"")
        self.tx_BuscarEstoque.setClearButtonEnabled(True)
        self.tx_BuscarEstoque.setObjectName("tx_BuscarEstoque")
        self.combox_localizaestoque = QtWidgets.QComboBox(self.framecabecario)
        self.combox_localizaestoque.setGeometry(QtCore.QRect(120, 90, 141, 31))
        self.combox_localizaestoque.setStyleSheet("border:1px solid")
        self.combox_localizaestoque.setEditable(True)
        self.combox_localizaestoque.setObjectName("combox_localizaestoque")
        self.labe_4 = QtWidgets.QLabel(self.framecabecario)
        self.labe_4.setGeometry(QtCore.QRect(120, 70, 141, 16))
        self.labe_4.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.labe_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labe_4.setObjectName("labe_4")
        self.verticalLayout_4.addWidget(self.framecabecario)
        self.frame_edita = QtWidgets.QFrame(self.widget_3)
        self.frame_edita.setStyleSheet("\n"
"QFrame{\n"
"text-transform: uppercase;\n"
"border:none;\n"
"    background-color: none;\n"
"}\n"
"")
        self.frame_edita.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_edita.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_edita.setObjectName("frame_edita")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_edita)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4.addWidget(self.frame_edita)
        self.tabWidget = QtWidgets.QTabWidget(self.widget_3)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"  border: 1px solid lightgray;\n"
"  top:-1px; \n"
"  background: rgb(245, 245, 245);; \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"  background: rgb(230, 230, 230); \n"
"  border: 1px solid lightgray; \n"
"  padding: 5px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    border:1px solid;\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.ativos = QtWidgets.QWidget()
        self.ativos.setObjectName("ativos")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ativos)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.ativos)
        self.widget.setMinimumSize(QtCore.QSize(1150, 0))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ch_ativo = QtWidgets.QCheckBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ch_ativo.setFont(font)
        self.ch_ativo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch_ativo.setChecked(True)
        self.ch_ativo.setTristate(True)
        self.ch_ativo.setObjectName("ch_ativo")
        self.horizontalLayout_6.addWidget(self.ch_ativo)
        self.ch_inativo = QtWidgets.QCheckBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ch_inativo.setFont(font)
        self.ch_inativo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ch_inativo.setChecked(False)
        self.ch_inativo.setAutoRepeat(False)
        self.ch_inativo.setAutoExclusive(False)
        self.ch_inativo.setTristate(True)
        self.ch_inativo.setObjectName("ch_inativo")
        self.horizontalLayout_6.addWidget(self.ch_inativo)
        self.horizontalLayout.addWidget(self.frame_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labe_5 = QtWidgets.QLabel(self.frame_3)
        self.labe_5.setStyleSheet("QLabel{\n"
"font-size: 12px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: #277298;\n"
"border: none\n"
"}")
        self.labe_5.setAlignment(QtCore.Qt.AlignCenter)
        self.labe_5.setObjectName("labe_5")
        self.verticalLayout_5.addWidget(self.labe_5)
        self.tx_quantidadeprodutoestoque = QtWidgets.QLineEdit(self.frame_3)
        self.tx_quantidadeprodutoestoque.setEnabled(False)
        self.tx_quantidadeprodutoestoque.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tx_quantidadeprodutoestoque.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tx_quantidadeprodutoestoque.setStyleSheet("font-size: 14px;\n"
"font-family: \"Arial\";\n"
"font-weight: bold;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom:1px solid black;\n"
"")
        self.tx_quantidadeprodutoestoque.setText("")
        self.tx_quantidadeprodutoestoque.setAlignment(QtCore.Qt.AlignCenter)
        self.tx_quantidadeprodutoestoque.setReadOnly(True)
        self.tx_quantidadeprodutoestoque.setObjectName("tx_quantidadeprodutoestoque")
        self.verticalLayout_5.addWidget(self.tx_quantidadeprodutoestoque)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.Tab_Estoque = QtWidgets.QTableWidget(self.widget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
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
        self.Tab_Estoque.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Tab_Estoque.setFont(font)
        self.Tab_Estoque.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Tab_Estoque.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Tab_Estoque.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.Tab_Estoque.setStyleSheet("QTableWidget {\n"
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
        self.Tab_Estoque.setAutoScrollMargin(20)
        self.Tab_Estoque.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.Tab_Estoque.setTabKeyNavigation(False)
        self.Tab_Estoque.setProperty("showDropIndicator", False)
        self.Tab_Estoque.setAlternatingRowColors(False)
        self.Tab_Estoque.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.Tab_Estoque.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Tab_Estoque.setShowGrid(False)
        self.Tab_Estoque.setGridStyle(QtCore.Qt.SolidLine)
        self.Tab_Estoque.setWordWrap(True)
        self.Tab_Estoque.setObjectName("Tab_Estoque")
        self.Tab_Estoque.setColumnCount(8)
        self.Tab_Estoque.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.Tab_Estoque.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.Tab_Estoque.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.Tab_Estoque.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.Tab_Estoque.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tab_Estoque.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tab_Estoque.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tab_Estoque.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tab_Estoque.setHorizontalHeaderItem(7, item)
        self.Tab_Estoque.horizontalHeader().setDefaultSectionSize(120)
        self.Tab_Estoque.horizontalHeader().setSortIndicatorShown(False)
        self.Tab_Estoque.horizontalHeader().setStretchLastSection(True)
        self.Tab_Estoque.verticalHeader().setVisible(False)
        self.Tab_Estoque.verticalHeader().setDefaultSectionSize(50)
        self.Tab_Estoque.verticalHeader().setMinimumSectionSize(23)
        self.verticalLayout_3.addWidget(self.Tab_Estoque)
        self.verticalLayout.addWidget(self.widget)
        self.tabWidget.addTab(self.ativos, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.frame = QtWidgets.QFrame(self.widget_3)
        self.frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(244, 244, 244);\n"
"}\n"
"QPushButton{\n"
"text-transform: uppercase;\n"
"    text-align:center;\n"
"    color:#fff;\n"
"    border:0px;\n"
"    \n"
"    font-size:15px;\n"
"    cursor: pointer;\n"
"    background-color:#2408D4;\n"
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
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bt_novo_procuto = QtWidgets.QPushButton(self.frame)
        self.bt_novo_procuto.setMinimumSize(QtCore.QSize(0, 30))
        self.bt_novo_procuto.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/telainicial/telainicial/cadastrosgeral.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_novo_procuto.setIcon(icon)
        self.bt_novo_procuto.setIconSize(QtCore.QSize(40, 40))
        self.bt_novo_procuto.setObjectName("bt_novo_procuto")
        self.horizontalLayout_5.addWidget(self.bt_novo_procuto)
        self.bt_altera = QtWidgets.QPushButton(self.frame)
        self.bt_altera.setMinimumSize(QtCore.QSize(0, 30))
        self.bt_altera.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/telainicial/telainicial/edita.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_altera.setIcon(icon1)
        self.bt_altera.setIconSize(QtCore.QSize(40, 40))
        self.bt_altera.setObjectName("bt_altera")
        self.horizontalLayout_5.addWidget(self.bt_altera)
        self.bt_apagar = QtWidgets.QPushButton(self.frame)
        self.bt_apagar.setMinimumSize(QtCore.QSize(0, 30))
        self.bt_apagar.setFocusPolicy(QtCore.Qt.NoFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/telainicial/telainicial/apagar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_apagar.setIcon(icon2)
        self.bt_apagar.setIconSize(QtCore.QSize(40, 40))
        self.bt_apagar.setObjectName("bt_apagar")
        self.horizontalLayout_5.addWidget(self.bt_apagar)
        self.bt_imprimir = QtWidgets.QPushButton(self.frame)
        self.bt_imprimir.setFocusPolicy(QtCore.Qt.NoFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/telainicial/telainicial/impressao.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_imprimir.setIcon(icon3)
        self.bt_imprimir.setIconSize(QtCore.QSize(40, 40))
        self.bt_imprimir.setObjectName("bt_imprimir")
        self.horizontalLayout_5.addWidget(self.bt_imprimir)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_4.addWidget(self.frame)
        self.horizontalLayout_4.addWidget(self.widget_3)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.actioneditar = QtWidgets.QAction(FormEstoque)
        self.actioneditar.setIcon(icon1)
        self.actioneditar.setObjectName("actioneditar")
        self.actionexcluri = QtWidgets.QAction(FormEstoque)
        self.actionexcluri.setIcon(icon2)
        self.actionexcluri.setObjectName("actionexcluri")
        self.actionNOVOPRODUTO = QtWidgets.QAction(FormEstoque)
        self.actionNOVOPRODUTO.setIcon(icon)
        self.actionNOVOPRODUTO.setObjectName("actionNOVOPRODUTO")

        self.retranslateUi(FormEstoque)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FormEstoque)
        FormEstoque.setTabOrder(self.tx_BuscarEstoque, self.combox_localizaestoque)
        FormEstoque.setTabOrder(self.combox_localizaestoque, self.tabWidget)
        FormEstoque.setTabOrder(self.tabWidget, self.Tab_Estoque)

    def retranslateUi(self, FormEstoque):
        _translate = QtCore.QCoreApplication.translate
        FormEstoque.setWindowTitle(_translate("FormEstoque", "Estoque"))
        self.lb_TituloEstoque.setText(_translate("FormEstoque", "cadastro estoque"))
        self.labe.setText(_translate("FormEstoque", "Qt itens"))
        self.tx_QuantidaDeProduto.setPlaceholderText(_translate("FormEstoque", "0.00"))
        self.labe_2.setText(_translate("FormEstoque", "Descriçao"))
        self.labe_3.setText(_translate("FormEstoque", "codigo barra"))
        self.tx_BuscarEstoque.setPlaceholderText(_translate("FormEstoque", "localizar estoque"))
        self.labe_4.setText(_translate("FormEstoque", "localizar estoque"))
        self.ch_ativo.setText(_translate("FormEstoque", "ATIVO"))
        self.ch_inativo.setText(_translate("FormEstoque", "INATIVO"))
        self.labe_5.setText(_translate("FormEstoque", "Quantidade produto cadastrado"))
        self.tx_quantidadeprodutoestoque.setPlaceholderText(_translate("FormEstoque", "0.00"))
        self.Tab_Estoque.setSortingEnabled(False)
        item = self.Tab_Estoque.horizontalHeaderItem(0)
        item.setText(_translate("FormEstoque", "CODIGO BARRA"))
        item = self.Tab_Estoque.horizontalHeaderItem(1)
        item.setText(_translate("FormEstoque", "DESCRIÇAO"))
        item = self.Tab_Estoque.horizontalHeaderItem(2)
        item.setText(_translate("FormEstoque", "QUANTIDADE"))
        item = self.Tab_Estoque.horizontalHeaderItem(3)
        item.setText(_translate("FormEstoque", "vl custo R$"))
        item = self.Tab_Estoque.horizontalHeaderItem(4)
        item.setText(_translate("FormEstoque", "vl venda R$"))
        item = self.Tab_Estoque.horizontalHeaderItem(5)
        item.setText(_translate("FormEstoque", "grupo"))
        item = self.Tab_Estoque.horizontalHeaderItem(6)
        item.setText(_translate("FormEstoque", "ativo"))
        item = self.Tab_Estoque.horizontalHeaderItem(7)
        item.setText(_translate("FormEstoque", "localizaçao"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ativos), _translate("FormEstoque", "ativos"))
        self.bt_novo_procuto.setText(_translate("FormEstoque", " novos produtos"))
        self.bt_altera.setText(_translate("FormEstoque", "alterar"))
        self.bt_apagar.setText(_translate("FormEstoque", "apagar"))
        self.bt_imprimir.setText(_translate("FormEstoque", "imprimir"))
        self.actioneditar.setText(_translate("FormEstoque", "editar"))
        self.actionexcluri.setText(_translate("FormEstoque", "excluir"))
        self.actionNOVOPRODUTO.setText(_translate("FormEstoque", "NOVO PRODUTO"))
