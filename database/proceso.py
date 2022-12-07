from database.connection import create_connection

class DBProceso():

    
    def __init__(self, id = 0 ,nombre = " ", sterilant_selection = 0, temperature_setpoint = 0, jacket_differential_offset = 0,maximum_temperature= 0  , hi_temperature_tolerance= 0, lo_temperature_tolerance = 0,
    cycles_start_temperature_tolerance = 0, pressure_units = 0, v_evacuation_pressure = 0, v_anticavitation_pressure = 0, v_gas_interlock_pressure = 0, v_pressure_increment = 0, v_time_increment = 0,
    v_fast_increment_tolerance = 0, v_slow_increment_termination_pressure = 0, v_print_interval = 0, l_leak_test_time = 0, l_leak_test_tolerance = 0, l_print_interval = 0, i_of_dilution_cycles = 0,
    i_inert_gas_pressure = 0, i_inert_pressure_increment = 0, i_inert_time_increment = 0, i_inert_fast_increment_tolerance = 0, i_evacuation_pressure = 0, i_vacuum_pressure_increment = 0, 
    i_vacuum_time_increment = 0,i_vaccum_fast_inc_tolerance = 0,i_vacuum_slow_increment_termination_pressure = 0,i_anticavitation_pressure= 0,i_hi_pressure= 0,i_print_interval= 0,
    h_type= 0,h_pressure_rise= 0,h_pressure_increment= 0,h_time_increment= 0,h_fast_increment_tolerance= 0,h_maximum_time= 0,h_print_interval= 0,hd_type= 0,hd_control_pressure= 0,hd_control_diferential= 0,
    hd_hi_humidity= 0, hd_lo_humidity= 0, hd_maximum_humidity= 0,hd_dwell_time= 0,hd_print_interval= 0,g_gas_pressure= 0,g_pressure_increment= 0,
    g_time_increment= 0, g_fast_increment_tolerance= 0, g_print_interval= 0, g_gas_by_weigh= 0, gd_control_pressure= 0 , gd_control_differential= 0,
    gd_dwell_time= 0, gd_maximum_makeups= 0, gd_long_exposure= 0, gd_short_exposure= 0, gd_hi_pressure= 0, gd_lo_pressure= 0, gd_hi_pressure_abort= 0,
    gd_emission_control_lead_time= 0, gd_print_interval= 0, a_evacuation_pressure= 0, a_anticavitation_pressure= 0 , a_air_interlock_pressure= 0, a_pressure_increment= 0,
    a_time_increment= 0, a_fast_increment_tolerance= 0 , a_slow_increment_termination_pressure= 0 , a_vacuum_hold_time= 0, a_print_interval= 0, 
    gwa_of_wash_cycles= 0,gwa_release_type= 0, gwa_release_pressure= 0 , gwa_evacuation_pressure= 0 ,gwa_anticavitation_pressure= 0,gwa_hi_pressure= 0 ,
    gwa_release_pressure_increment= 0, gwa_release_time_increment= 0 , gwa_fast_inc_tolerance= 0, gwa_release_slow_increment_termination_pressure= 0,
    gwa_release_hold_time= 0, gwa_vacuum_pressure_increment= 0 , gwa_vacuum_time_increment= 0 , gwa_vacuum_fast_inc_tolerance= 0 , gwa_vacuum_slow_increment_termination_pressure= 0, 
    gwa_vacuum_hold_time= 0, gwa_print_interval= 0, gwb_of_wash_cycles= 0 , gwb_release_type= 0 , gwb_release_pressure= 0 , 
    gwb_evacuation_pressure= 0, gwb_anticavitation_pressure= 0, gwb_hi_pressure= 0 , gwb_release_pressure_increment= 0,
    gwb_release_time_increment= 0, gwb_release_fast_inc_tolerance= 0, gwb_release_slow_increment_termination_pressure= 0,gwb_release_hold_time= 0, 
    gwb_vacuum_pressure_increment= 0, gwb_vacuum_time_increment= 0, gwb_vacuum_fast_inc_tolerance= 0, gwb_slow_increment_termination_pressure= 0 ,
    gwb_vacuum_hold_time= 0, gwb_print_interval= 0, r_release_pressure= 0, r_pressure_increment= 0,r_time_increment= 0, r_fast_increment_tolerance= 0, r_slow_increment_termination_pressure= 0,
    r_print_interval= 0
    ):   
        print("objeto creado")
        self._id = id
        self._nombre = nombre
        self._sterilant_selection = sterilant_selection
        self._temperature_setpoint = temperature_setpoint
        self._jacket_differential_offset = jacket_differential_offset 
        self._maximum_temperature = maximum_temperature
        self._hi_temperature_tolerance = hi_temperature_tolerance
        self._lo_temperature_tolerance = lo_temperature_tolerance
        self._cycles_start_temperature_tolerance = cycles_start_temperature_tolerance
        self._pressure_units = pressure_units
        self._v_evacuation_pressure = v_evacuation_pressure
        self._v_anticavitation_pressure = v_anticavitation_pressure
        self._v_gas_interlock_pressure = v_gas_interlock_pressure
        self._v_pressure_increment = v_pressure_increment 
        self._v_time_increment = v_time_increment 
        self._v_fast_increment_tolerance = v_fast_increment_tolerance 
        self._v_slow_increment_termination_pressure = v_slow_increment_termination_pressure 
        self._v_print_interval = v_print_interval 
        self._l_leak_test_time = l_leak_test_time
        self._l_leak_test_tolerance = l_leak_test_tolerance 
        self._l_print_interval = l_print_interval 
        self._i_of_dilution_cycles = i_of_dilution_cycles
        self._i_inert_gas_pressure = i_inert_gas_pressure
        self._i_inert_pressure_increment = i_inert_pressure_increment 
        self._i_inert_time_increment = i_inert_time_increment 
        self._i_inert_fast_increment_tolerance = i_inert_fast_increment_tolerance 
        self._i_evacuation_pressure = i_evacuation_pressure 
        self._i_vacuum_pressure_increment = i_vacuum_pressure_increment
        self._i_vacuum_time_increment = i_vacuum_time_increment 
        self._i_vaccum_fast_inc_tolerance = i_vaccum_fast_inc_tolerance
        self._i_vacuum_slow_increment_termination_pressure = i_vacuum_slow_increment_termination_pressure
        self._i_anticavitation_pressure = i_anticavitation_pressure
        self._i_hi_pressure = i_hi_pressure 
        self._i_print_interval = i_print_interval 
        self._h_type = h_type
        self._h_pressure_rise = h_pressure_rise
        self._h_pressure_increment = h_pressure_increment
        self._h_time_increment = h_time_increment 
        self._h_fast_increment_tolerance = h_fast_increment_tolerance
        self._h_maximum_time = h_maximum_time
        self._h_print_interval = h_print_interval
        self._hd_type = hd_type
        self._hd_control_pressure = hd_control_pressure
        self._hd_control_diferential   = hd_control_diferential
        self._hd_hi_humidity = hd_hi_humidity
        self._hd_lo_humidity = hd_lo_humidity 
        self._hd_maximum_humidity = hd_maximum_humidity
        self._hd_dwell_time = hd_dwell_time
        self._hd_print_interval = hd_print_interval
        self._g_gas_pressure = g_gas_pressure
        self._g_pressure_increment = g_pressure_increment
        self._g_time_increment = g_time_increment
        self._g_fast_increment_tolerance = g_fast_increment_tolerance
        self._g_print_interval = g_print_interval
        self._g_gas_by_weigh = g_gas_by_weigh
        self._gd_control_pressure = gd_control_pressure
        self._gd_control_differential = gd_control_differential
        self._gd_dwell_time = gd_dwell_time
        self._gd_maximum_makeups = gd_maximum_makeups
        self._gd_long_exposure = gd_long_exposure
        self._gd_short_exposure = gd_short_exposure
        self._gd_hi_pressure = gd_hi_pressure
        self._gd_lo_pressure = gd_lo_pressure
        self._gd_hi_pressure_abort = gd_hi_pressure_abort
        self._gd_emission_control_lead_time = gd_emission_control_lead_time
        self._gd_print_interval = gd_print_interval
        self._a_evacuation_pressure = a_evacuation_pressure
        self._a_anticavitation_pressure = a_anticavitation_pressure
        self._a_air_interlock_pressure = a_air_interlock_pressure
        self._a_pressure_increment = a_pressure_increment
        self._a_time_increment = a_time_increment
        self._a_fast_increment_tolerance = a_fast_increment_tolerance
        self._a_slow_increment_termination_pressure = a_slow_increment_termination_pressure
        self._a_vacuum_hold_time = a_vacuum_hold_time
        self._a_print_interval  = a_print_interval
        self._gwa_of_wash_cycles = gwa_of_wash_cycles
        self._gwa_release_type = gwa_release_type
        self._gwa_release_pressure = gwa_release_pressure
        self._gwa_evacuation_pressure = gwa_evacuation_pressure
        self._gwa_anticavitation_pressure = gwa_anticavitation_pressure
        self._gwa_hi_pressure = gwa_hi_pressure
        self._gwa_release_pressure_increment = gwa_release_pressure_increment
        self._gwa_release_time_increment = gwa_release_time_increment
        self._gwa_fast_inc_tolerance = gwa_fast_inc_tolerance
        self._gwa_release_slow_increment_termination_pressure = gwa_release_slow_increment_termination_pressure
        self._gwa_release_hold_time = gwa_release_hold_time
        self._gwa_vacuum_pressure_increment = gwa_vacuum_pressure_increment
        self._gwa_vacuum_time_increment = gwa_vacuum_time_increment
        self._gwa_vacuum_fast_inc_tolerance = gwa_vacuum_fast_inc_tolerance
        self._gwa_vacuum_slow_increment_termination_pressure = gwa_vacuum_slow_increment_termination_pressure
        self._gwa_vacuum_hold_time = gwa_vacuum_hold_time
        self._gwa_print_interval = gwa_print_interval
        self._gwb_of_wash_cycles = gwb_of_wash_cycles
        self._gwb_release_type = gwb_release_type
        self._gwb_release_pressure = gwb_release_pressure
        self._gwb_evacuation_pressure = gwb_evacuation_pressure
        self._gwb_anticavitation_pressure = gwb_anticavitation_pressure
        self._gwb_hi_pressure = gwb_hi_pressure
        self._gwb_release_pressure_increment = gwb_release_pressure_increment
        self._gwb_release_time_increment = gwb_release_time_increment
        self._gwb_release_fast_inc_tolerance = gwb_release_fast_inc_tolerance
        self._gwb_release_slow_increment_termination_pressure = gwb_release_slow_increment_termination_pressure
        self._gwb_release_hold_time = gwb_release_hold_time
        self._gwb_vacuum_pressure_increment = gwb_vacuum_pressure_increment
        self._gwb_vacuum_time_increment = gwb_vacuum_time_increment
        self._gwb_vacuum_fast_inc_tolerance = gwb_vacuum_fast_inc_tolerance
        self._gwb_slow_increment_termination_pressure = gwb_slow_increment_termination_pressure
        self._gwb_vacuum_hold_time = gwb_vacuum_hold_time
        self._gwb_print_interval = gwb_print_interval
        self._r_release_pressure = r_release_pressure
        self._r_pressure_increment = r_pressure_increment
        self._r_time_increment = r_time_increment
        self._r_fast_increment_tolerance = r_fast_increment_tolerance
        self._r_slow_increment_termination_pressure = r_slow_increment_termination_pressure
        self._r_print_interval  = r_print_interval
    
    def select_all_name_proceso(self):
        try:
            sql = "SELECT nombre FROM esterilizadora.parametros order by id"
            
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            recetas = cursor.fetchall()
            lista = ["Seleccionar"]
            for receta in recetas:
                lista.append(receta[0])
                cursor.close()
            #print(lista)
            return lista 
        except Exception as e:
            print(e)
            return False
        
    def insert_receta(self): # 166 26 // 169 48 // 172 68 // 176 92 // 115 
        sql = """INSERT INTO parametros(`id`,`nombre`,`sterilant_selection`,`temperature_setpoint`,`jacket_differential_offset`,`maximum_temperature`,`hi_temperature_tolerance`,
            `lo_temperature_tolerance`,`cycles_start_temperature_tolerance`,`pressure_units`,`v_evacuation_pressure`,`v_anticavitation_pressure`,`v_gas_interlock_pressure`,
            `v_pressure_increment`,`v_time_increment`,`v_fast_increment_tolerance`,`v_slow_increment_termination_pressure`,`v_print_interval`,`l_leak_test_time`,
            `l_leak_test_tolerance`,`l_print_interval`,`i_of_dilution_cycles`,`i_inert_gas_pressure`,`i_inert_pressure_increment`,`i_inert_time_increment`,`i_inert_fast_increment_tolerance`, 
            `i_evacuation_pressure`, `i_vacuum_pressure_increment`, `i_vacuum_time_increment`,`i_vaccum_fast_inc_tolerance`,`i_vacuum_slow_increment_termination_pressure`,
            `i_anticavitation_pressure`, `i_hi_pressure`,`i_print_interval`,`h_type`,`h_pressure_rise`,`h_pressure_increment`,`h_time_increment`,`h_fast_increment_tolerance`,`h_maximum_time`,
            `h_print_interval`,`hd_type`,`hd_control_pressure`,`hd_control_diferential`,`hd_hi_humidity`,`hd_lo_humidity`,`hd_maximum_humidity`,`hd_dwell_time`,
            `hd_print_interval`,`g_gas_pressure`,`g_pressure_increment`,`g_time_increment`,`g_fast_increment_tolerance`,`g_print_interval`,`g_gas_by_weight`,
            `gd_control_pressure`,`gd_control_differential`,`gd_dwell_time`,`gd_maximum_makeups`,`gd_long_exposure`,`gd_short_exposure`,`gd_hi_pressure`,
            `gd_lo_pressure`,`gd_hi_pressure_abort`,`gd_emission_control_lead_time`,`gd_print_interval`,`a_evacuation_pressure`,`a_anticavitation_pressure`,
            `a_air_interlock_pressure`,`a_pressure_increment`,`a_time_increment`,`a_fast_increment_tolerance`,`a_slow_increment_termination_pressure`,`a_vacuum_hold_time`,`a_print_interval`,
            `gwa_of_wash_cycles`,`gwa_release_type`,`gwa_release_pressure`,`gwa_evacuation_pressure`,`gwa_anticavitation_pressure`,`gwa_hi_pressure`,`gwa_release_pressure_increment`,
            `gwa_release_time_increment`,`gwa_fast_inc_tolerance`,`gwa_release_slow_increment_termination_pressure`,`gwa_release_hold_time`,`gwa_vacuum_pressure_increment`,
            `gwa_vacuum_time_increment`,`gwa_vacuum_fast_inc_tolerance`,`gwa_vacuum_slow_increment_termination_pressure`,`gwa_vacuum_hold_time`,`gwa_print_interval`,
            `gwb_of_wash_cycles`,`gwb_release_type`,`gwb_release_pressure`,`gwb_evacuation_pressure`,`gwb_anticavitation_pressure`,`gwb_hi_pressure`,`gwb_release_pressure_increment`,
            `gwb_release_time_increment`,`gwb_release_fast_inc_tolerance`,`gwb_release_slow_increment_termination_pressure`,`gwb_release_hold_time`,`gwb_vacuum_pressure_increment`,
            `gwb_vacuum_time_increment`,`gwb_vacuum_fast_inc_tolerance`,`gwb_slow_increment_termination_pressure`,`gwb_vacuum_hold_time`,`gwb_print_interval`,`r_release_pressure`,`r_pressure_increment`,`r_time_increment`,
            `r_fast_increment_tolerance`,`r_slow_increment_termination_pressure`,`r_print_interval`)VALUES
            ({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}, 
             {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},
             {},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}
            )""".format(self._id,self._nombre,
            self._sterilant_selection,self._temperature_setpoint,self._jacket_differential_offset,self._maximum_temperature,self._hi_temperature_tolerance,self._lo_temperature_tolerance,
            self._cycles_start_temperature_tolerance,self._pressure_units,self._v_evacuation_pressure,self._v_anticavitation_pressure,self._v_gas_interlock_pressure,self._v_pressure_increment,
            self._v_time_increment,self._v_fast_increment_tolerance,self._v_slow_increment_termination_pressure,self._v_print_interval,self._l_leak_test_time,self._l_leak_test_tolerance,
            self._l_print_interval,self._i_of_dilution_cycles,self._i_inert_gas_pressure,self._i_inert_pressure_increment,self._i_inert_time_increment,self._i_inert_fast_increment_tolerance,
            self._i_evacuation_pressure,self._i_vacuum_pressure_increment,self._i_vacuum_time_increment,self._i_vaccum_fast_inc_tolerance,self._i_vacuum_slow_increment_termination_pressure,
            self._i_anticavitation_pressure,self._i_hi_pressure,self._i_print_interval,self._h_type,self._h_pressure_rise,self._h_pressure_increment,self._h_time_increment,self._h_fast_increment_tolerance,
            self._h_maximum_time,self._h_print_interval,self._hd_type,self._hd_control_pressure,self._hd_control_diferential,self._hd_hi_humidity,self._hd_lo_humidity,self._hd_maximum_humidity,
            self._hd_dwell_time,self._hd_print_interval,self._g_gas_pressure,self._g_pressure_increment,self._g_time_increment,self._g_fast_increment_tolerance,self._g_print_interval,self._g_gas_by_weigh,
            self._gd_control_pressure,self._gd_control_differential,self._gd_dwell_time,self._gd_maximum_makeups,self._gd_long_exposure,self._gd_short_exposure,self._gd_hi_pressure,self._gd_lo_pressure,
            self._gd_hi_pressure_abort,self._gd_emission_control_lead_time,self._gd_print_interval,self._a_evacuation_pressure,self._a_anticavitation_pressure,self._a_air_interlock_pressure,
            self._a_pressure_increment,self._a_time_increment,self._a_fast_increment_tolerance,self._a_slow_increment_termination_pressure,self._a_vacuum_hold_time,self._a_print_interval,
            self._gwa_of_wash_cycles,self._gwa_release_type,self._gwa_release_pressure,self._gwa_evacuation_pressure,self._gwa_anticavitation_pressure,self._gwa_hi_pressure,
            self._gwa_release_pressure_increment,self._gwa_release_time_increment,self._gwa_fast_inc_tolerance,self._gwa_release_slow_increment_termination_pressure,self._gwa_release_hold_time,
            self._gwa_vacuum_pressure_increment,self._gwa_vacuum_time_increment,self._gwa_vacuum_fast_inc_tolerance,self._gwa_vacuum_slow_increment_termination_pressure,self._gwa_vacuum_hold_time,
            self._gwa_print_interval,self._gwb_of_wash_cycles,self._gwb_release_type,self._gwb_release_pressure,self._gwb_evacuation_pressure,self._gwb_anticavitation_pressure,self._gwb_hi_pressure,
            self._gwb_release_pressure_increment,self._gwb_release_time_increment,self._gwb_release_fast_inc_tolerance,self._gwb_release_slow_increment_termination_pressure,self._gwb_release_hold_time,
            self._gwb_vacuum_pressure_increment,self._gwb_vacuum_time_increment,self._gwb_vacuum_fast_inc_tolerance,self._gwb_slow_increment_termination_pressure,self._gwb_vacuum_hold_time,
            self._gwb_print_interval,self._r_release_pressure,self._r_pressure_increment,self._r_time_increment,self._r_fast_increment_tolerance,self._r_slow_increment_termination_pressure,
            self._r_print_interval)
        try: 
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            print("LOGRADO")
            cursor.close()
        except Exception as e:
            raise 

    def select_proceso(self, value):
        sql= """SELECT 
    v_evacuation_pressure,
    v_anticavitation_pressure,
    v_gas_interlock_pressure,
    v_pressure_increment,
    v_time_increment,
    v_fast_increment_tolerance,
    v_slow_increment_termination_pressure,
    v_print_interval,
    l_leak_test_time,
    l_leak_test_tolerance,
    l_print_interval,
    i_of_dilution_cycles,
    i_inert_gas_pressure,
    i_inert_pressure_increment,
    i_inert_time_increment,
    i_inert_fast_increment_tolerance,
    i_evacuation_pressure,
    i_vacuum_pressure_increment,
    i_vacuum_time_increment,
    i_vaccum_fast_inc_tolerance,
    i_vacuum_slow_increment_termination_pressure,
    i_anticavitation_pressure,
    i_hi_pressure,
    i_print_interval,
    h_type,
    h_pressure_rise,
    h_pressure_increment,
    h_time_increment,
    h_fast_increment_tolerance,
    h_maximum_time,
    h_print_interval,
    hd_type,
    hd_control_pressure,
    hd_control_diferential,
    hd_hi_humidity,
    hd_lo_humidity,
    hd_maximum_humidity,
    hd_dwell_time,
    hd_print_interval,
    g_gas_pressure,
    g_pressure_increment,
    g_time_increment,
    g_fast_increment_tolerance,
    g_print_interval,
    g_gas_by_weight,
    gd_control_pressure,
    gd_control_differential,
    gd_dwell_time,
    gd_maximum_makeups,
    gd_long_exposure,
    gd_short_exposure,
    gd_hi_pressure,
    gd_lo_pressure,
    gd_hi_pressure_abort,
    gd_emission_control_lead_time,
    gd_print_interval,
    a_evacuation_pressure,
    a_anticavitation_pressure,
    a_air_interlock_pressure,
    a_pressure_increment,
    a_time_increment,
    a_fast_increment_tolerance,
    a_slow_increment_termination_pressure,
    a_vacuum_hold_time,
    a_print_interval,
    gwa_of_wash_cycles,
    gwa_release_type,
    gwa_release_pressure,
    gwa_evacuation_pressure,
    gwa_anticavitation_pressure,
    gwa_hi_pressure,
    gwa_release_pressure_increment,
    gwa_release_time_increment,
    gwa_fast_inc_tolerance,
    gwa_release_slow_increment_termination_pressure,
    gwa_release_hold_time,
    gwa_vacuum_pressure_increment,
    gwa_vacuum_time_increment,
    gwa_vacuum_fast_inc_tolerance,
    gwa_vacuum_slow_increment_termination_pressure,
    gwa_vacuum_hold_time,
    gwa_print_interval,
    gwb_of_wash_cycles,
    gwb_release_type,
    gwb_release_pressure,
    gwb_evacuation_pressure,
    gwb_anticavitation_pressure,
    gwb_hi_pressure,
    gwb_release_pressure_increment,
    gwb_release_time_increment,
    gwb_release_fast_inc_tolerance,
    gwb_release_slow_increment_termination_pressure,
    gwb_release_hold_time,
    gwb_vacuum_pressure_increment,
    gwb_vacuum_time_increment,
    gwb_vacuum_fast_inc_tolerance,
    gwb_slow_increment_termination_pressure,
    gwb_vacuum_hold_time,
    gwb_print_interval,
    r_release_pressure,
    r_pressure_increment,
    r_time_increment,
    r_fast_increment_tolerance,
    r_slow_increment_termination_pressure,
    r_print_interval
    FROM esterilizadora.parametros where nombre = '{}' """.format(value)
        object_proceso = []
        try:
            #self.cursor.execute(sql)
            #proceso = self.cursor.fetchone()
            #object_proceso = [proceso[0],proceso[1],proceso[2],proceso[3],proceso[4],
            #proceso[5],proceso[6],proceso[7],proceso[8],proceso[9],proceso[10],proceso[11],
            #proceso[12],proceso[13],proceso[14],proceso[15],proceso[16],proceso[17],proceso[18],
            #proceso[19],proceso[20],proceso[21],proceso[22],proceso[23],proceso[24],proceso[25],
            ##proceso[26],proceso[27],proceso[28],proceso[29],proceso[30],proceso[31],proceso[32],
            #proceso[33],proceso[34],proceso[35],proceso[36],proceso[37],proceso[38],proceso[39],
            #proceso[40],proceso[41],proceso[42],proceso[43],proceso[44],proceso[45],proceso[46],
            #proceso[47],proceso[48],proceso[49],proceso[50],proceso[51],proceso[52],proceso[53],
            #proceso[54],proceso[55],proceso[56],proceso[57],proceso[58],proceso[59],proceso[60],
            #proceso[61],proceso[62],proceso[63],proceso[64],proceso[65],proceso[66],proceso[67],
            #proceso[68],proceso[69],proceso[70],proceso[71],proceso[72],proceso[73],proceso[74],
            #proceso[75],proceso[76],proceso[77],proceso[78], proceso[79],proceso[80],proceso[81],
            #proceso[82],proceso[83],proceso[84],proceso[85],proceso[86],proceso[87],proceso[88],
            #proceso[89],proceso[90],proceso[91],proceso[92],proceso[93],proceso[94],proceso[95],
            #proceso[96],proceso[97],proceso[98],proceso[99],proceso[100],proceso[101],proceso[102],proceso[103], proceso[104]]
            
            #print("Proceso: ",proceso[10])

            #return object_proceso
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            recetas = cursor.fetchall()

            #print(recetas)
            lista = []
            
            for receta in recetas:
                
            
                lista.append(receta)
                   
            cursor.close()
            #print(lista)
            return lista 


        except Exception as e:
            print(e)
            return object_proceso

    def delete_receta(self):
        sql = "DELETE FROM esterilizadora.parametros WHERE id = {}".format(self.id)
        try:
            connection = create_connection()
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()

            return True
        except Exception as e:
            print(e)
            return False


#con = DBProceso()
#ren =con.select_proceso("Receta01")
#print(ren)
#name = con.select_all_name_proceso()
#print(name)

