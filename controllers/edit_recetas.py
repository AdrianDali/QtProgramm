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
        #self.spinBox_5.setValue(proceso[0][4])
        self.spinBox_6.setValue(proceso[0][5])
        self.spinBox_7.setValue(proceso[0][6])
        #self.spinBox_8.setValue(proceso[0][7])

        self.doubleSpinBox.setValue(proceso[0][0])
        self.doubleSpinBox_2.setValue(proceso[0][1])
        self.doubleSpinBox_3.setValue(proceso[0][2])
        self.doubleSpinBox_4.setValue(proceso[0][3])
        
        print(proceso[0][4])
        hour_00 = self.get_minute(proceso[0][4])
        self.timeEdit.setTime(QTime(int(hour_00[0]), int(hour_00[1])))
        
        self.doubleSpinBox_5.setValue(proceso[0][5])
        self.doubleSpinBox_6.setValue(proceso[0][6])

        hour_001 = self.get_minute(proceso[0][7])
        self.timeEdit_2.setTime(QTime(int(hour_001[0]), int(hour_001[1])))


   
        
        hour_01 = self.get_hour(proceso[0][8])
        self.timeEdit_22.setTime(QTime(int(hour_01[0]), int(hour_01[1])))
        self.doubleSpinBox_7.setValue(proceso[0][9])
        hour_02 = self.get_minute(proceso[0][10])
        self.timeEdit_3.setTime(QTime(int(hour_02[0]), int(hour_02[1])))

        self.nombre_line_edit_42.setText(str(proceso[0][11]))
        self.doubleSpinBox_8.setValue(proceso[0][12])
        self.doubleSpinBox_9.setValue(proceso[0][13])

        hour_03 = self.get_minute(proceso[0][14])
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

        

        hour_05 = self.get_minute(proceso[0][23])
        self.timeEdit_6.setTime(QTime(int(hour_05[0]), int(hour_05[1])))

        self.nombre_line_edit_55.setText(str(proceso[0][24]))

        self.doubleSpinBox_17.setValue(proceso[0][25])
        self.doubleSpinBox_18.setValue(proceso[0][26])
        
        hour_06 = self.get_minute(proceso[0][27])
        self.timeEdit_7.setTime(QTime(int(hour_06[0]), int(hour_06[1])))

        self.doubleSpinBox_19.setValue(proceso[0][28])

        hour_06 = self.get_minute(proceso[0][29])
        self.timeEdit_8.setTime(QTime(int(hour_06[0]), int(hour_06[1])))

        hour_07 = self.get_minute(proceso[0][30])
        self.timeEdit_9.setTime(QTime(int(hour_07[0]), int(hour_07[1])))
        #####

        self.nombre_line_edit_62.setText(str(proceso[0][31]))
        self.doubleSpinBox_20.setValue(proceso[0][32])
        self.doubleSpinBox_21.setValue(proceso[0][33])
        self.doubleSpinBox_22.setValue(proceso[0][34])
        self.doubleSpinBox_24.setValue(proceso[0][35])
        self.doubleSpinBox_23.setValue(proceso[0][36])

        hour_08 = self.get_minute(proceso[0][37])
        self.timeEdit_24.setTime(QTime(int(hour_08[0]), int(hour_08[1])))

        hour_09 = self.get_minute(proceso[0][38])
        self.timeEdit_23.setTime(QTime(int(hour_09[0]), int(hour_09[1])))

        #########
        self.doubleSpinBox_25.setValue(proceso[0][39])
        self.doubleSpinBox_26.setValue(proceso[0][40])

        hour_10 = self.get_minute(proceso[0][41])
        self.timeEdit_10.setTime(QTime(int(hour_10[0]), int(hour_10[1])))

        self.doubleSpinBox_27.setValue(proceso[0][42])

        hour_11 = self.get_minute(proceso[0][43])
        self.timeEdit_11.setTime(QTime(int(hour_11[0]), int(hour_11[1])))

        self.nombre_line_edit_75.setText(str(proceso[0][44]))

        ##############
        self.doubleSpinBox_28.setValue(proceso[0][45])
        self.doubleSpinBox_29.setValue(proceso[0][46])

        hour_012 = self.get_hour(proceso[0][47])
        self.timeEdit_34.setTime(QTime(int(hour_012[0]), int(hour_012[1])))

        self.doubleSpinBox_31.setValue(proceso[0][48])

        hour_013 = self.get_hour(proceso[0][49])
        self.timeEdit_12.setTime(QTime(int(hour_013[0]), int(hour_013[1])))

        hour_014 = self.get_hour(proceso[0][50])
        self.timeEdit_35.setTime(QTime(int(hour_014[0]), int(hour_014[1])))

        self.doubleSpinBox_33.setValue(proceso[0][51])
        self.doubleSpinBox_62.setValue(proceso[0][52])
        self.doubleSpinBox_63.setValue(proceso[0][53])

        hour_015 = self.get_hour(proceso[0][54])
        self.timeEdit_33.setTime(QTime(int(hour_015[0]), int(hour_015[1])))

        hour_016 = self.get_hour(proceso[0][55])
        self.timeEdit_13.setTime(QTime(int(hour_016[0]), int(hour_016[1])))


           ######################

        self.doubleSpinBox_34.setValue(proceso[0][56])
        self.doubleSpinBox_35.setValue(proceso[0][57])
        self.doubleSpinBox_36.setValue(proceso[0][58])
        self.doubleSpinBox_37.setValue(proceso[0][59])

        hour_15 = self.get_minute(proceso[0][60])
        self.timeEdit_14.setTime(QTime(int(hour_15[0]), int(hour_15[1])))

        self.doubleSpinBox_38.setValue(proceso[0][61])
        self.doubleSpinBox_39.setValue(proceso[0][62])

        hour_16 = self.get_hour(proceso[0][63])
        self.timeEdit_26.setTime(QTime(int(hour_16[0]), int(hour_16[1])))

        hour_17 = self.get_minute(proceso[0][64])
        self.timeEdit_15.setTime(QTime(int(hour_17[0]), int(hour_17[1])))
        ############################

        self.nombre_line_edit_357.setText(str(proceso[0][65]))
        self.nombre_line_edit_143.setText(str(proceso[0][66]))


        self.doubleSpinBox_40.setValue(proceso[0][67])
        self.doubleSpinBox_41.setValue(proceso[0][68])
        self.doubleSpinBox_42.setValue(proceso[0][69])
        self.doubleSpinBox_43.setValue(proceso[0][70])
        self.doubleSpinBox_44.setValue(proceso[0][71])

        hour_18 = self.get_minute(proceso[0][72])
        self.timeEdit_16.setTime(QTime(int(hour_18[0]), int(hour_18[1])))

        self.doubleSpinBox_45.setValue(proceso[0][73])
        self.doubleSpinBox_46.setValue(proceso[0][74])

        hour_19 = self.get_hour(proceso[0][75])
        self.timeEdit_27.setTime(QTime(int(hour_19[0]), int(hour_19[1])))

        self.doubleSpinBox_47.setValue(proceso[0][76])

        hour_20 = self.get_minute(proceso[0][77])
        self.timeEdit_17.setTime(QTime(int(hour_20[0]), int(hour_20[1])))

        self.doubleSpinBox_48.setValue(proceso[0][78])
        self.doubleSpinBox_49.setValue(proceso[0][79])

        hour_21 = self.get_hour(proceso[0][80])
        self.timeEdit_28.setTime(QTime(int(hour_21[0]), int(hour_21[1])))

        hour_22 = self.get_minute(proceso[0][81])
        self.timeEdit_18.setTime(QTime(int(hour_22[0]), int(hour_22[1])))
        ############################


        ############################

        self.nombre_line_edit_366.setText(str(proceso[0][82]))
        self.nombre_line_edit_164.setText(str(proceso[0][83]))


        self.doubleSpinBox_50.setValue(proceso[0][84])
        self.doubleSpinBox_51.setValue(proceso[0][85])
        self.doubleSpinBox_52.setValue(proceso[0][86])
        self.doubleSpinBox_53.setValue(proceso[0][87])
        self.doubleSpinBox_54.setValue(proceso[0][88])

        hour_18 = self.get_minute(proceso[0][89])
        self.timeEdit_19.setTime(QTime(int(hour_18[0]), int(hour_18[1])))

        self.doubleSpinBox_55.setValue(proceso[0][90])
        self.doubleSpinBox_56.setValue(proceso[0][91])

        hour_19 = self.get_hour(proceso[0][92])
        self.timeEdit_59.setTime(QTime(int(hour_19[0]), int(hour_19[1])))

        self.doubleSpinBox_57.setValue(proceso[0][93])

        hour_20 = self.get_minute(proceso[0][94])
        self.timeEdit_20.setTime(QTime(int(hour_20[0]), int(hour_20[1])))

        self.doubleSpinBox_58.setValue(proceso[0][95])
        self.doubleSpinBox_59.setValue(proceso[0][96])

        hour_21 = self.get_hour(proceso[0][97])
        self.timeEdit_29.setTime(QTime(int(hour_21[0]), int(hour_21[1])))

        hour_22 = self.get_minute(proceso[0][98])
        self.timeEdit_21.setTime(QTime(int(hour_22[0]), int(hour_22[1])))
        ############################

        self.doubleSpinBox_60.setValue(proceso[0][99])
        self.doubleSpinBox_61.setValue(proceso[0][100])

        hour_23 = self.get_hour(proceso[0][101])
        self.timeEdit_30.setTime(QTime(int(hour_23[0]), int(hour_23[1])))

        self.doubleSpinBox_64.setValue(proceso[0][102])
        self.doubleSpinBox_65.setValue(proceso[0][103])

        hour_24 = self.get_minute(proceso[0][104])
        self.timeEdit_31.setTime(QTime(int(hour_24[0]), int(hour_24[1])))


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
