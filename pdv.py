from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from assets.file import*
from funcoesclass.ClassPdv.Pdv import*
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = PdvVenda()
    w.show()
    sys.exit(app.exec_())
    