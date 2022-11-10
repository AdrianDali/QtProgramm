from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTime
from interface.edit_recetas_window import MainWindow
from interface.general_custom_ui import GeneralCustomUi
from database.proceso import DBProceso
class MainWindowForm(QWidget, MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.combo_receta()
        self.comboBox.currentTextChanged.connect(self.moveEvent)
    
    def moveEvent(self):
        recipe = self.comboBox.currentText()
        print(recipe)
        proceso = DBProceso.select_proceso(self, recipe)
        print(proceso) 
        self.nombre_line_edit_43.setText(recipe)
        self.spinBox.setValue(proceso[0][0])
        self.spinBox_2.setValue(proceso[0][1])
        self.spinBox_3.setValue(proceso[0][2])
        self.spinBox_4.setValue(proceso[0][3])
        self.spinBox_5.setValue(proceso[0][4])
        self.spinBox_6.setValue(proceso[0][5])
        self.spinBox_7.setValue(proceso[0][6])
        self.spinBox_8.setValue(proceso[0][7])

        self.doubleSpinBox.setValue(proceso[0][0])
        self.doubleSpinBox_2.setValue(proceso[0][1])
        self.doubleSpinBox_3.setValue(proceso[0][2])
        self.doubleSpinBox_4.setValue(proceso[0][3])
        self.doubleSpinBox_5.setValue(proceso[0][5])
        self.doubleSpinBox_6.setValue(proceso[0][6])

   
        
        hour_01 = self.get_hour(proceso[0][8])
        self.timeEdit_22.setTime(QTime(int(hour_01[0]), int(hour_01[1])))
        self.doubleSpinBox_7.setValue(proceso[0][9])
        hour_02 = self.get_minute(proceso[0][10])
        self.timeEdit_3.setTime(QTime(int(hour_02[0]), int(hour_02[1])))

        self.nombre_line_edit_42.setText(str(proceso[0][11]))
        self.doubleSpinBox_8.setValue(proceso[0][12])
        self.doubleSpinBox_9.setValue(proceso[0][13])

        hour_03 = self.get_hour(proceso[0][14])
        self.timeEdit_4.setTime(QTime(int(hour_03[0]), int(hour_03[1])))

        self.doubleSpinBox_11.setValue(proceso[0][15])
        self.doubleSpinBox_10.setValue(proceso[0][16])
        self.doubleSpinBox_12.setValue(proceso[0][17])
        
        hour_04 = self.get_minute(proceso[0][18])
        self.timeEdit_5.setTime(QTime(int(hour_04[0]), int(hour_04[1])))

        self.doubleSpinBox_13.setValue(proceso[0][19])
        self.doubleSpinBox_14.setValue(proceso[0][20])
        self.doubleSpinBox_16.setValue(proceso[0][21])
        self.doubleSpinBox_15.setValue(proceso[0][22])

        hour_05 = self.get_hour(proceso[0][23])
        self.timeEdit_6.setTime(QTime(int(hour_05[0]), int(hour_05[1])))

        self.doubleSpinBox_17.setValue(proceso[0][25])
        self.doubleSpinBox_18.setValue(proceso[0][26])
        
        hour_06 = self.get_minute(proceso[0][27])
        self.timeEdit_7.setTime(QTime(int(hour_06[0]), int(hour_06[1])))

        self.doubleSpinBox_19.setValue(proceso[0][28])

        hour_06 = self.get_minute(proceso[0][29])
        self.timeEdit_8.setTime(QTime(int(hour_06[0]), int(hour_06[1])))

        hour_07 = self.get_hour(proceso[0][30])
        self.timeEdit_9.setTime(QTime(int(hour_07[0]), int(hour_07[1])))
        #####

    def get_minute(self, time):
        slc = str(time).split(':')
        #se borra el de los segundos
        slc.pop(2)
        print(slc)
        return(slc)

    def get_hour(self, time):
        slc = str(time).split(':')
        #se borra el de los segundos
        slc.pop(0)
        print(slc)
        return(slc)

    def combo_receta(self):
        self.comboBox.addItems(DBProceso.select_all_name_proceso(self))
