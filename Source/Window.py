from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from Views.View import View


class Window:
    __app: QApplication
    __window: QMainWindow
    __stackedWidget: QStackedWidget

    def createWindow(ancho: int, alto: int):
        Window.__window = QMainWindow()
        Window.__window.setFixedWidth(ancho)
        Window.__window.setFixedHeight(alto)
        #Window.__window.showFullScreen()

        Window.__stackedWidget = QStackedWidget()
        Window.__window.setCentralWidget(Window.__stackedWidget)
        
        Window.__window.show()

    def setViewActual(view: View):
        if Window.__stackedWidget.count() > 0:
            Window.__stackedWidget.removeWidget(Window.__stackedWidget.currentWidget())     

        Window.__stackedWidget.addWidget(view)
        Window.__stackedWidget.setCurrentWidget(view)  

    def getWidth():
        return Window.__window.width()

    def getHeight():
        return Window.__window.height()
