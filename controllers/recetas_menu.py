from PySide6.QtWidgets import QWidget, QTableWidgetItem
from interface.recetas_menu import DetailWindow
from interface.general_custom_ui import GeneralCustomUi
from controllers.add_recetas import MainWindowForm as AddRecetas 
from controllers.edit_recetas import MainWindowForm as EditRecetas 

from database.proceso import DBProceso
class MainWindowForm(QWidget, DetailWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)

        self.config_table()
        self.set_table_data()

        self.view_button.clicked.connect(self.create_new_recipe)
        
        self.edit_button.clicked.connect(self.edit_recipe)

    def create_new_recipe(self):
        new_receta = AddRecetas()
        new_receta.show()

    def edit_recipe(self):
        edit_receta = EditRecetas()
        edit_receta.show()
        

    def config_table(self):
        column_labels = ("ID", "NOMBRE")
        self.tableWidget.setColumnCount(len(column_labels))
        self.tableWidget.setHorizontalHeaderLabels(column_labels)
        #cambiar de tamano a la celda 
        self.tableWidget.setColumnWidth(1, 600)
        
        #cambiar alto de la celda 
        self.tableWidget.verticalHeader().setDefaultSectionSize(150)
        #ocultar columna 
        self.tableWidget.setColumnHidden(0, True)
        # para que cuando selecciones una celda no se seleccione toda la fila

        #self.recipes_table.setSelectionBehavior(QAbstractItemView.SelectRows)
    

    def populate_table(self, data):
        self.tableWidget.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                
                self.tableWidget.setItem(
                    index_row, index_cell, QTableWidgetItem(str(row))
                )
            #agregar los botones a la tabla
            #self.recipes_table.setCellWidget(
            #    index_row, 9, self.build_action_buttons()
            #)

    #LE MANDAMOS LOS DATOS A LA TABLA QUE VIENEN DESDE LA BASE DE DATOS
    def set_table_data(self):
        data = DBProceso.select_all_name_proceso(self)
        data.pop(0)
        self.populate_table(data)
        
        