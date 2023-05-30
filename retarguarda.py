
from funcoesclass.main import*
from assets.file import*

if __name__ == '__main__':
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    banco=db.pega_dados(''' select id from param  ''')
    if not banco:
        FormConfigParam().exec_()
    else:
        w = telaincial() 
        w.show()
        sys.exit(app.exec_())
        