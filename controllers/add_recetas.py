from PySide6.QtWidgets import QWidget
from interface.add_edit_recetas_window import MainWindow
from interface.general_custom_ui import GeneralCustomUi
from database.proceso import DBProceso
class MainWindowForm(QWidget, MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.edit_button_3.clicked.connect(self.edit_button_2_clicked)

    def edit_button_2_clicked(self):

        nombre = self.nombre_line_edit_43.text();
        sterilant_selection = self.spinBox.value();
        temperature_setpoint = self.spinBox_2.value();
        jacket_differential_offset = self.spinBox_3.value(); # noqa: E501
        maximum_temperature = self.spinBox_4.value(); # noqa: E501
        hi_temperature_tolerance = self.spinBox_5.value(); # noqa: E501
        lo_temperature_tolerance = self.spinBox_6.value(); # noqa: E501
        cycle_start_temperature_tolerance = self.spinBox_7.value(); # noqa: E501
        pressure_units = self.spinBox_8.value(); # noqa: E501

        print("nombre: ", nombre)
        print("sterilant_selection: ", sterilant_selection)
        print("temperature_setpoint: ", temperature_setpoint)
        print("jacket_differential_offset: ", jacket_differential_offset) # noqa: E501
        print("maximum_temperature: ", maximum_temperature) # noqa: E501
        print("hi_temperature_tolerance: ", hi_temperature_tolerance) # noqa: E501
        print("lo_temperature_tolerance: ", lo_temperature_tolerance) # noqa: E501
        print("cycle_start_temperature_tolerance: ", cycle_start_temperature_tolerance) # noqa: E501
        print("pressure_units: ", pressure_units) # noqa: E501


        v_evacuation_pressure = self.doubleSpinBox.value();
        v_anti_cavitation_pressure = self.doubleSpinBox_2.value(); # 2 is the index of the spin box
        v_gas_interlock_pressure = self.doubleSpinBox_3.value(); # 3 is the index of the spin box
        v_pressure_increment = self.doubleSpinBox_4.value(); # 4 is the index of the spin box
        v_time_increment = self.timeEdit.text(); # 5 is the index of the spin box
        v_fast_increment_tolerance = self.doubleSpinBox_5.value(); # 6 is the index of the spin box
        v_slow_increment_termination_pressure = self.doubleSpinBox_6.value(); # 7 is the index of the spin box
        v_print_interval = self.timeEdit_2.text(); # 8 is the index of the spin box

        print("v_evacuation_pressure: ", v_evacuation_pressure) # noqa: E501
        print("v_anti_cavitation_pressure: ", v_anti_cavitation_pressure) # noqa: E501
        print("v_gas_interlock_pressure: ", v_gas_interlock_pressure) # noqa: E501
        print("v_pressure_increment: ", v_pressure_increment) # noqa: E501
        print("v_time_increment: ", v_time_increment) # noqa: E501
        print("v_fast_increment_tolerance: ", v_fast_increment_tolerance) # noqa: E501
        print("v_slow_increment_termination_pressure: ", v_slow_increment_termination_pressure) # noqa: E501
        print("v_print_interval: ", v_print_interval) # noqa: E501
        
        l_leak_test_time = self.timeEdit_22.text(); # 9 is the index of the spin box
        l_leak_test_tolerance = self.doubleSpinBox_7.value(); # 10 is the index of the spin box
        l_print_interval = self.timeEdit_3.text(); # 11 is the index of the spin box

        print("l_leak_test_time: ", l_leak_test_time) # noqa: E501
        print("l_leak_test_tolerance: ", l_leak_test_tolerance) # noqa: E501
        print("l_print_interval: ", l_print_interval) # noqa: E501


        i_of_dilution_cycles = self.nombre_line_edit_42.text(); # 12 is the index of the spin box
        i_inert_gas_pressure = self.doubleSpinBox_8.value(); # 13 is the index of the spin box
        i_inert_pressure_increment = self.doubleSpinBox_9.value(); # 14 is the index of the spin box
        i_inert_time_increment = self.timeEdit_4.text(); # 15 is the index of the spin box
        i_inert_fast_increment_tolerance = self.doubleSpinBox_11.value(); # 16 is the index of the spin box
        i_evacuation_pressure = self.doubleSpinBox_10.value(); # 17 is the index of the spin box
        i_vacuum_pressure_increment = self.doubleSpinBox_12.value(); # 18 is the index of the spin box
        i_vacuum_time_increment = self.timeEdit_5.text(); # 19 is the index of the spin box
        i_vacuum_fast_increment_tolerance = self.doubleSpinBox_13.value(); # 20 is the index of the spin box
        i_vacuum_slow_increment_termination_pressure = self.doubleSpinBox_14.value(); # 21 is the index of the spin box
        i_anti_cavitation_pressure = self.doubleSpinBox_16.value(); # 22 is the index of the spin box
        i_hi_pressure = self.doubleSpinBox_15.value(); # 23 is the index of the spin box
        i_print_interval = self.timeEdit_6.text(); # 24 is the index of the spin box

        print("i_of_dilution_cycles: ", i_of_dilution_cycles) # noqa: E501
        print("i_inert_gas_pressure: ", i_inert_gas_pressure) # noqa: E501
        print("i_inert_pressure_increment: ", i_inert_pressure_increment) # noqa: E501
        print("i_inert_time_increment: ", i_inert_time_increment) # noqa: E501
        print("i_inert_fast_increment_tolerance: ", i_inert_fast_increment_tolerance) # noqa: E501
        print("i_evacuation_pressure: ", i_evacuation_pressure) # noqa: E501
        print("i_vacuum_pressure_increment: ", i_vacuum_pressure_increment) # noqa: E501
        print("i_vacuum_time_increment: ", i_vacuum_time_increment) # noqa: E501
        print("i_vacuum_fast_increment_tolerance: ", i_vacuum_fast_increment_tolerance) # noqa: E501
        print("i_vacuum_slow_increment_termination_pressure: ", i_vacuum_slow_increment_termination_pressure) # noqa: E501
        print("i_anti_cavitation_pressure: ", i_anti_cavitation_pressure) # noqa: E501
        print("i_hi_pressure: ", i_hi_pressure) # noqa: E501
        print("i_print_interval: ", i_print_interval) # noqa: E501


        #---------------------------------------------------------------------------------------------------------------------------
        h_type = self.nombre_line_edit_55.text(); # 25 is the index of the spin box
        h_pressure_rise  = self.doubleSpinBox_17.value(); # 26 is the index of the spin box
        h_pressure_increment = self.doubleSpinBox_18.value(); # 27 is the index of the spin box
        h_time_increment = self.timeEdit_7.text(); # 28 is the index of the spin box
        h_fast_increment_tolerance = self.doubleSpinBox_19.value(); # 29 is the index of the spin box
        h_maximum_time = self.timeEdit_8.text(); # 30 is the index of the spin box
        h_print_interval = self.timeEdit_9.text(); # 31 is the index of the spin box

        print("h_type: ", h_type) # noqa: E501
        print("h_pressure_rise: ", h_pressure_rise) # noqa: E501
        print("h_pressure_increment: ", h_pressure_increment) # noqa: E501
        print("h_time_increment: ", h_time_increment) # noqa: E501
        print("h_fast_increment_tolerance: ", h_fast_increment_tolerance) # noqa: E501
        print("h_maximum_time: ", h_maximum_time) # noqa: E501
        print("h_print_interval: ", h_print_interval) # noqa: E501


        hd_type = self.nombre_line_edit_62.text(); # 32 is the index of the spin box
        hd_control_pressure = self.doubleSpinBox_20.value(); # 33 is the index of the spin box
        hd_control_differential = self.doubleSpinBox_21.value(); # 34 is the index of the spin box
        hd_hi_humidity = self.doubleSpinBox_22.value(); # 35 is the index of the spin box
        hd_lo_humidity = self.doubleSpinBox_24.value(); # 36 is the index of the spin box
        hd_maximum_humidity = self.doubleSpinBox_23.value(); # 37 is the index of the spin box
        hd_dwell_time = self.timeEdit_24.text(); # 38 is the index of the spin box
        hd_print_interval = self.timeEdit_23.text(); # 39 is the index of the spin box

        print("hd_type: ", hd_type) # noqa: E501
        print("hd_control_pressure: ", hd_control_pressure) # noqa: E501
        print("hd_control_differential: ", hd_control_differential) # noqa: E501
        print("hd_hi_humidity: ", hd_hi_humidity) # noqa: E501
        print("hd_lo_humidity: ", hd_lo_humidity) # noqa: E501
        print("hd_maximum_humidity: ", hd_maximum_humidity) # noqa: E501
        print("hd_dwell_time: ", hd_dwell_time) # noqa: E501
        print("hd_print_interval: ", hd_print_interval) # noqa: E501


        g_gas_pressure = self.doubleSpinBox_25.value(); # 40 is the index of the spin box
        g_pressure_increment = self.doubleSpinBox_26.value(); # 41 is the index of the spin box
        g_time_increment = self.timeEdit_10.text(); # 42 is the index of the spin box
        g_fast_increment_tolerance = self.doubleSpinBox_27.value(); # 43 is the index of the spin box
        g_print_interval = self.timeEdit_11.text(); # 44 is the index of the spin box
        g_gas_by_weight = self.nombre_line_edit_75.text(); # 45 is the index of the spin box

        print("g_gas_pressure: ", g_gas_pressure) # noqa: E501
        print("g_pressure_increment: ", g_pressure_increment) # noqa: E501
        print("g_time_increment: ", g_time_increment) # noqa: E501
        print("g_fast_increment_tolerance: ", g_fast_increment_tolerance) # noqa: E501
        print("g_print_interval: ", g_print_interval) # noqa: E501
        print("g_gas_by_weight: ", g_gas_by_weight) # noqa: E501


        gd_control_pressure = self.doubleSpinBox_28.value(); # 46 is the index of the spin box
        gd_control_differential = self.doubleSpinBox_29.value(); # 47 is the index of the spin box
        gd_dwell_time = self.timeEdit_34.text(); # 48 is the index of the spin boxq
        gd_maximum_makeups = self.doubleSpinBox_31.value(); # 49 is the index of the spin box
        gd_long_exposure  = self.timeEdit_12.text(); # 50 is the index of the spin box
        gd_short_exposure = self.timeEdit_35.text(); # 51 is the index of the spin box
        gd_hi_pressure = self.doubleSpinBox_33.value(); # 52 is the index of the spin box
        gd_lo_pressure = self.doubleSpinBox_62.value(); # 53 is the index of the spin box
        gd_hi_pressure_abort =self.doubleSpinBox_63.value();  
        gd_emission_control_lead_time = self.timeEdit_33.text(); # 54 is the index of the spin box
        gd_print_interval = self.timeEdit_13.text(); # 55 is the index of the spin box

        print("gd_control_pressure: ", gd_control_pressure) # noqa: E501
        print("gd_control_differential: ", gd_control_differential) # noqa: E501
        print("gd_dwell_time: ", gd_dwell_time) # noqa: E501
        print("gd_maximum_makeups: ", gd_maximum_makeups) # noqa: E501
        print("gd_long_exposure: ", gd_long_exposure) # noqa: E501
        print("gd_short_exposure: ", gd_short_exposure) # noqa: E501
        print("gd_hi_pressure: ", gd_hi_pressure) # noqa: E501
        print("gd_lo_pressure: ", gd_lo_pressure) # noqa: E501
        print("gd_hi_pressure_abort: ", gd_hi_pressure_abort) # noqa: E501
        print("gd_emission_control_lead_time: ", gd_emission_control_lead_time) # noqa: E501
        print("gd_print_interval: ", gd_print_interval) # noqa: E501

        #gd_evacuation_pressure = self.doubleSpinBox_28.value(); # 46 is the index of the spin box
        ##gd_anti_cavitation_pressure = self.doubleSpinBox_29.value(); # 47 is the index of the spin box
        #gd_air_interlock_pressure = self.doubleSpinBox_30.value(); # 48 is the index of the spin box
        #gd_slow_increment_termination_pressure = self.doubleSpinBox_31.value(); # 49 is the index of the spin box
        #gd_pressure_increment = self.doubleSpinBox_32.value(); # 50 is the index of the spin box
        #gd_time_increment  = self.timeEdit_12.text(); # 51 is the index of the spin box
        #gd_fast_increment_tolerance = self.doubleSpinBox_33.value(); # 52 is the index of the spin box
        #gd_vacuum_hold_time = self.timeEdit_25.text(); # 53 is the index of the spin box
        #gd_print_interval = self.timeEdit_13.text(); # 54 is the index of the spin box


        a_evacuation_pressure = self.doubleSpinBox_34.value(); # 55 is the index of the spin box
        a_anti_cavitation_pressure = self.doubleSpinBox_35.value(); # 56 is the index of the spin box
        a_air_interlock_pressure = self.doubleSpinBox_36.value(); # 57 is the index of the spin box
        a_pressure_increment = self.doubleSpinBox_37.value(); # 58 is the index of the spin box
        a_time_increment = self.timeEdit_14.text(); # 59 is the index of the spin box
        a_fast_increment_tolerance = self.doubleSpinBox_38.value(); # 60 is the index of the spin box
        a_slow_increment_termination_pressure = self.doubleSpinBox_39.value(); # 61 is the index of the spin box
        a_vacumm_hold_time = self.timeEdit_26.text(); # 62 is the index of the spin box
        a_print_interval = self.timeEdit_15.text(); # 63 is the index of the spin box

        print("a_evacuation_pressure: ", a_evacuation_pressure) # noqa: E501
        print("a_anti_cavitation_pressure: ", a_anti_cavitation_pressure) # noqa: E501
        print("a_air_interlock_pressure: ", a_air_interlock_pressure) # noqa: E501
        print("a_pressure_increment: ", a_pressure_increment) # noqa: E501
        print("a_time_increment: ", a_time_increment) # noqa: E501
        print("a_fast_increment_tolerance: ", a_fast_increment_tolerance) # noqa: E501
        print("a_slow_increment_termination_pressure: ", a_slow_increment_termination_pressure) # noqa: E501
        print("a_vacumm_hold_time: ", a_vacumm_hold_time)
        print("a_print_interval: ", a_print_interval)




        gwa_of_wash_cycles = self.nombre_line_edit_357.text(); # 73 is the index of the spin box
        gwa_release_type = self.nombre_line_edit_143.text(); # 74 is the index of the spin box
        gwa_release_pressure = self.doubleSpinBox_40.value(); # 75 is the index of the spin box
        gwa_evacuation_pressure = self.doubleSpinBox_41.value(); # 76 is the index of the spin box
        gwa_anti_cavitation_pressure = self.doubleSpinBox_42.value(); # 77 is the index of the spin box
        gwa_hi_pressure = self.doubleSpinBox_43.value(); # 78 is the index of the spin box
        gwa_release_pressure_increment = self.doubleSpinBox_44.value(); # 79 is the index of the spin box
        gwa_release_time_increment = self.timeEdit_16.text(); # 80 is the index of the spin box
        gwa_fast_increment_tolerance = self.doubleSpinBox_45.value(); # 81 is the index of the spin box
        gwa_release_slow_increment_termination_pressure = self.doubleSpinBox_46.value(); # 82 is the index of the spin box
        gwa_release_hold_time = self.timeEdit_27.text(); # 83 is the index of the spin box
        gwa_vacumm_pressure_increment = self.doubleSpinBox_47.value(); # 84 is the index of the spin box
        gwa_vacumm_time_increment = self.timeEdit_17.text(); # 85 is the index of the spin box
        gwa_vaccum_fast_increment_tolerance = self.doubleSpinBox_48.value(); # 86 is the index of the spin box
        gwa_vacuum_slow_increment_termination_pressure = self.doubleSpinBox_49.value(); # 87 is the index of the spin box
        gwa_vacuum_hold_time = self.timeEdit_28.text(); # 88 is the index of the spin box
        gwa_print_interval = self.timeEdit_18.text(); # 89 is the index of the spin box

        print("gwa_of_wash_cycles: ", gwa_of_wash_cycles) # noqa: E501
        print("gwa_release_type: ", gwa_release_type) # noqa: E501
        print("gwa_release_pressure: ", gwa_release_pressure) # noqa: E501
        print("gwa_evacuation_pressure: ", gwa_evacuation_pressure) # noqa: E501
        print("gwa_anti_cavitation_pressure: ", gwa_anti_cavitation_pressure) # noqa: E501
        print("gwa_hi_pressure: ", gwa_hi_pressure) # noqa: E501
        print("gwa_release_pressure_increment: ", gwa_release_pressure_increment) # noqa: E501
        print("gwa_release_time_increment: ", gwa_release_time_increment) # noqa: E501
        print("gwa_fast_increment_tolerance: ", gwa_fast_increment_tolerance) # noqa: E501
        print("gwa_release_slow_increment_termination_pressure: ", gwa_release_slow_increment_termination_pressure) # noqa: E501
        print("gwa_release_hold_time: ", gwa_release_hold_time) # noqa: E501
        print("gwa_vacumm_pressure_increment: ", gwa_vacumm_pressure_increment) # noqa: E501
        print("gwa_vacumm_time_increment: ", gwa_vacumm_time_increment) # noqa: E501
        print("gwa_vaccum_fast_increment_tolerance: ", gwa_vaccum_fast_increment_tolerance) # noqa: E501
        print("gwa_vacuum_slow_increment_termination_pressure: ", gwa_vacuum_slow_increment_termination_pressure) # noqa: E501
        print("gwa_vacuum_hold_time: ", gwa_vacuum_hold_time) # noqa: E501
        print("gwa_print_interval: ", gwa_print_interval) # noqa: E501
        


        gwb_of_wash_cycles = self.nombre_line_edit_366.text(); # 73 is the index of the spin box
        gwb_release_type = self.nombre_line_edit_164.text(); # 74 is the index of the spin box
        gwb_release_pressure = self.doubleSpinBox_50.value(); # 75 is the index of the spin box
        gwb_evacuation_pressure = self.doubleSpinBox_51.value(); # 76 is the index of the spin box
        gwb_anti_cavitation_pressure = self.doubleSpinBox_52.value(); # 77 is the index of the spin box
        gwb_hi_pressure = self.doubleSpinBox_53.value(); # 78 is the index of the spin box
        gwb_release_pressure_increment = self.doubleSpinBox_54.value(); # 79 is the index of the spin box
        gwb_release_time_increment = self.timeEdit_19.text(); # 80 is the index of the spin box
        gwb_release_fast_increment_tolerance = self.doubleSpinBox_55.value(); # 81 is the index of the spin box
        gwb_release_slow_increment_termination_pressure = self.doubleSpinBox_56.value(); # 82 is the index of the spin box
        gwb_release_hold_time = self.timeEdit_59.text(); # 83 is the index of the spin box
        gwb_vacumm_pressure_increment = self.doubleSpinBox_57.value(); # 84 is the index of the spin box
        gwb_vacumm_time_increment = self.timeEdit_20.text(); # 85 is the index of the spin box
        gwb_vaccum_fast_increment_tolerance = self.doubleSpinBox_58.value(); # 86 is the index of the spin box
        gwb_vaccum_slow_increment_termination_pressure = self.doubleSpinBox_59.value(); # 87 is the index of the spin box
        gwb_vaccum_hold_time = self.timeEdit_29.text(); # 88 is the index of the spin box
        gwb_print_interval = self.timeEdit_21.text(); # 89 is the index of the spin box

        print("gwb_of_wash_cycles: ", gwb_of_wash_cycles) # noqa: E501
        print("gwb_release_type: ", gwb_release_type) # noqa: E501
        print("gwb_release_pressure: ", gwb_release_pressure) # noqa: E501
        print("gwb_evacuation_pressure: ", gwb_evacuation_pressure) # noqa: E501
        print("gwb_anti_cavitation_pressure: ", gwb_anti_cavitation_pressure) # noqa: E501
        print("gwb_hi_pressure: ", gwb_hi_pressure) # noqa: E501
        print("gwb_release_pressure_increment: ", gwb_release_pressure_increment) # noqa: E501
        print("gwb_release_time_increment: ", gwb_release_time_increment) # noqa: E501
        print("gwb_release_fast_increment_tolerance: ", gwb_release_fast_increment_tolerance) # noqa: E501
        print("gwb_release_slow_increment_termination_pressure: ", gwb_release_slow_increment_termination_pressure) # noqa: E501
        print("gwb_release_hold_time: ", gwb_release_hold_time) # noqa: E501
        print("gwb_vacumm_pressure_increment: ", gwb_vacumm_pressure_increment) # noqa: E501
        print("gwb_vacumm_time_increment: ", gwb_vacumm_time_increment) # noqa: E501
        print("gwb_vaccum_fast_increment_tolerance: ", gwb_vaccum_fast_increment_tolerance) # noqa: E501
        print("gwb_vaccum_slow_increment_termination_pressure: ", gwb_vaccum_slow_increment_termination_pressure) # noqa: E501
        print("gwb_vaccum_hold_time: ", gwb_vaccum_hold_time) # noqa: E501
        print("gwb_print_interval: ", gwb_print_interval) # noqa: E501





        r_release_pressure = self.doubleSpinBox_60.value(); # 89 is the index of the spin box 
        r_pressure_increment = self.doubleSpinBox_61.value(); # 90 is the index of the spin box
        r_time_increment = self.timeEdit_30.text(); # 91 is the index of the spin box
        r_fast_increment_tolerance = self.doubleSpinBox_64.value(); # 92 is the index of the spin box
        r_slow_increment_termination_pressure = self.doubleSpinBox_65.value(); # 93 is the index of the spin box
        r_print_interval  = self.timeEdit_31.text(); # 94 is the index of the spin box

        print("r_release_pressure: ", r_release_pressure) # noqa: E501
        print("r_pressure_increment: ", r_pressure_increment) # noqa: E501
        print("r_time_increment: ", r_time_increment) # noqa: E501
        print("r_fast_increment_tolerance: ", r_fast_increment_tolerance) # noqa: E501
        print("r_slow_increment_termination_pressure: ", r_slow_increment_termination_pressure) # noqa: E501
        print("r_print_interval: ", r_print_interval) # noqa: E501


        new = DBProceso(nombre = nombre, sterilant_selection= sterilant_selection , temperature_setpoint= temperature_setpoint, 
        jacket_differential_offset= jacket_differential_offset, maximum_temperature= maximum_temperature,
        hi_temperature_tolerance= hi_temperature_tolerance , lo_temperature_tolerance = lo_temperature_tolerance, cycles_start_temperature_tolerance= cycle_start_temperature_tolerance , 
        pressure_units= pressure_units, v_evacuation_pressure= v_evacuation_pressure, v_anticavitation_pressure= v_anti_cavitation_pressure,
        v_gas_interlock_pressure = v_gas_interlock_pressure , v_pressure_increment= v_pressure_increment, v_time_increment= v_time_increment, v_fast_increment_tolerance= v_fast_increment_tolerance,
        v_slow_increment_termination_pressure = v_slow_increment_termination_pressure, v_print_interval= v_print_interval, 
        l_leak_test_time= l_leak_test_time, l_leak_test_tolerance= l_leak_test_tolerance, l_print_interval= l_print_interval,
        i_of_dilution_cycles= i_of_dilution_cycles, i_inert_gas_pressure= i_inert_gas_pressure, i_inert_pressure_increment= i_inert_pressure_increment,
        i_inert_time_increment= i_inert_time_increment, i_inert_fast_increment_tolerance= i_inert_fast_increment_tolerance , i_evacuation_pressure= i_evacuation_pressure, i_vacuum_pressure_increment= i_vacuum_pressure_increment ,
        i_vacuum_time_increment = i_vacuum_time_increment, i_vaccum_fast_inc_tolerance = i_vacuum_fast_increment_tolerance, i_vacuum_slow_increment_termination_pressure= i_vacuum_slow_increment_termination_pressure, 
        i_anticavitation_pressure = i_anti_cavitation_pressure, i_hi_pressure = i_hi_pressure , i_print_interval = i_print_interval, 
        h_type= h_type, h_pressure_rise= h_pressure_rise, h_pressure_increment= h_pressure_increment, h_time_increment= h_time_increment, h_fast_increment_tolerance= h_fast_increment_tolerance, h_maximum_time= h_maximum_time, h_print_interval= h_print_interval,  
        hd_type = hd_type, hd_control_pressure = hd_control_pressure , hd_control_diferential= hd_control_differential , hd_hi_humidity= hd_hi_humidity, hd_lo_humidity= hd_lo_humidity, hd_maximum_humidity= hd_maximum_humidity , hd_dwell_time= hd_dwell_time, hd_print_interval= hd_print_interval , 
        g_gas_pressure = g_gas_pressure, g_pressure_increment = g_pressure_increment , g_time_increment = g_time_increment , g_fast_increment_tolerance= g_fast_increment_tolerance , g_print_interval= g_print_interval, g_gas_by_weigh= g_gas_by_weight, 
        gd_control_pressure= gd_control_pressure, gd_control_differential= gd_control_differential, gd_dwell_time= gd_dwell_time, gd_maximum_makeups= gd_maximum_makeups , gd_long_exposure= gd_long_exposure, gd_short_exposure= gd_short_exposure, gd_hi_pressure= gd_hi_pressure , gd_lo_pressure= gd_lo_pressure, gd_hi_pressure_abort= gd_hi_pressure_abort, 
        gd_emission_control_lead_time= gd_emission_control_lead_time, gd_print_interval=gd_print_interval,
        a_evacuation_pressure= a_evacuation_pressure, a_anticavitation_pressure=a_anti_cavitation_pressure, a_air_interlock_pressure=a_air_interlock_pressure, a_pressure_increment=a_pressure_increment, a_time_increment= a_time_increment , a_fast_increment_tolerance= a_fast_increment_tolerance , a_slow_increment_termination_pressure= a_slow_increment_termination_pressure, 
        a_vacuum_hold_time= a_vacumm_hold_time, a_print_interval= a_print_interval,
        gwa_of_wash_cycles= gwa_of_wash_cycles, gwa_release_type = gwa_release_type , gwa_release_pressure= gwa_release_pressure, gwa_evacuation_pressure= gwa_evacuation_pressure, gwa_anticavitation_pressure= gwa_anti_cavitation_pressure, gwa_hi_pressure= gwa_hi_pressure, gwa_release_pressure_increment= gwa_release_pressure_increment, 
        gwa_release_time_increment= gwa_release_time_increment, gwa_fast_inc_tolerance= gwa_fast_increment_tolerance, gwa_release_slow_increment_termination_pressure= gwa_release_slow_increment_termination_pressure, gwa_release_hold_time= gwa_release_hold_time, gwa_vacuum_pressure_increment= gwa_vacumm_pressure_increment, gwa_vacuum_time_increment= gwa_vacumm_time_increment,
        gwa_vacuum_fast_inc_tolerance= gwa_vaccum_fast_increment_tolerance , gwa_vacuum_slow_increment_termination_pressure= gwa_vacuum_slow_increment_termination_pressure, gwa_vacuum_hold_time= gwa_vacuum_hold_time, gwa_print_interval= gwa_print_interval,   
        
        gwb_of_wash_cycles= gwb_of_wash_cycles, gwb_release_type = gwb_release_type , gwb_release_pressure= gwb_release_pressure, gwb_evacuation_pressure= gwb_evacuation_pressure, gwb_anticavitation_pressure= gwb_anti_cavitation_pressure, gwb_hi_pressure= gwb_hi_pressure, gwb_release_pressure_increment= gwb_release_pressure_increment, 
        gwb_release_time_increment= gwb_release_time_increment, gwb_release_fast_inc_tolerance= gwb_release_fast_increment_tolerance, gwb_release_slow_increment_termination_pressure= gwb_release_slow_increment_termination_pressure, gwb_release_hold_time= gwb_release_hold_time, gwb_vacuum_pressure_increment= gwb_vacumm_pressure_increment, gwb_vacuum_time_increment= gwb_vacumm_time_increment,
        gwb_vacuum_fast_inc_tolerance= gwb_vaccum_fast_increment_tolerance , gwb_slow_increment_termination_pressure= gwb_vaccum_slow_increment_termination_pressure, gwb_vacuum_hold_time= gwb_vaccum_hold_time, gwb_print_interval= gwb_print_interval,   

        r_release_pressure= r_release_pressure, r_pressure_increment = r_pressure_increment , r_time_increment = r_time_increment,r_fast_increment_tolerance = r_fast_increment_tolerance , r_slow_increment_termination_pressure = r_slow_increment_termination_pressure, r_print_interval = r_print_interval  
         )

        new.insert_receta()

       
        #self.nombre_line_edit_31.setEnabled(True)
        #self.nombre_line_edit_31.setText("hola")