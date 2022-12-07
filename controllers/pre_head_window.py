from PySide6.QtWidgets import QWidget,QGraphicsScene
from PySide6.QtCore import QRectF
from PySide6.QtGui import QPen,QBrush
from PySide6.QtGui import QPainter 
from interface.pre_head_window import MainWindow
from interface.general_custom_ui import GeneralCustomUi
from controllers.recetas_menu import MainWindowForm as RecetasMenu
import pyqtgraph as pg
from controllers.capture_cicle_window import MainWindowForm as CaptureCicleWindow

class MainWindowForm(QWidget, MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)

        self.add_edit_button.clicked.connect(self.add_edit_button_clicked)
        self.bargraph  = pg.BarGraphItem(x=[1,2,3,4,5], height=[1,2,3,4,5], width=0.6, brush='r')
        #self.graphicsView.addItem(self.bargraph)
        self.view_button_5.clicked.connect(self.view_button_5_clicked)

    def view_button_5_clicked(self):
        self.capture_cicle_window = CaptureCicleWindow()
        self.capture_cicle_window.show()

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    
    def add_edit_button_clicked(self):
        menu = RecetasMenu()
        menu.show()

    
        