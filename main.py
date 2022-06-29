import logging
from inclinometer_jdi200 import InclinometerJdi200
import time

camp1 = 800
camp2 = 400
camp3 = 200


if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s',  filename= "main.log")
    id1 = 82
    filtroON = 0
    filtro_lenght = 30

    logging.info('Start')

    inclinometer = InclinometerJdi200('COM3', id1)

    logging.info(f'inclinometer id: {inclinometer.get_id()}')
    inclinometer.set_filter_on(filtroON) #numero di campionamenti
    inclinometer.set_length_filter(filtro_lenght)   #frequenza
    inclinometer.set_samples_per_measurements(1) #numero di campionamenti
    inclinometer.set_sampling_rate(10)   #frequenza
    inclinometer.non_volatile_save()
    logging.info(f'inclinometer base x: {inclinometer.get_x()}')
    logging.info(f'inclinometer base y: {inclinometer.get_y()}')
    logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
    logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
    logging.info(f'filtro on/off {inclinometer.get_filter_on()}')
    logging.info(f'lunghezza filtro: {inclinometer.get_length_filter()}')

    tupla = inclinometer.get_xy()
    print(tupla)
    logging.info(f'inclinometer base xy: {tupla}')
    rollzero = tupla[0]
    pitchzero = tupla[1]
    print(rollzero)
    print(pitchzero)

    x = 0
    while x<200:    #numero di valori 200 200 100 50
        old = str(inclinometer.get_xy())
        new = old.replace(",", "")
        new2 = new.replace(")", "")
        new3 = new2.replace("(","")

        lista = list(new3.split(" "))
        lista = ([float(x) for x in lista])  # trasformo da str a float per fare operazioni

        v_roll = lista[0] - rollzero  # sottraggo l'offset di partenza
        v_roll = format(v_roll, '.20f')  # per evitare di stampare con esponenziale numeri piccoli
        v_pitch = lista[1] - pitchzero
        v_pitch = format(v_pitch, '.20f')
        print(str(v_roll) + "      " + str(v_pitch))
        logging.info(f'{v_roll}' + f'     {v_pitch}')



        #print (new3)
        #logging.info(f'inclinometer xy: {inclinometer.get_xy()}')
        time.sleep(1)  #tempo in secondi  0.5 x 200  1x100 2x50
        x = x+1
'''
######################################################################################################
    print("step")
    logging.info('Start')

    logging.info(f'inclinometer id: {inclinometer.get_id()}')


    inclinometer.set_filter_on(filtroON) #numero di campionamenti
    inclinometer.set_length_filter(filtro_lenght)   #frequenza
    inclinometer.set_samples_per_measurements(1) #numero di campionamenti
    inclinometer.set_sampling_rate(10)   #frequenza
    inclinometer.non_volatile_save()
    logging.info(f'inclinometer base x: {inclinometer.get_x()}')
    logging.info(f'inclinometer base y: {inclinometer.get_y()}')
    logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
    logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
    logging.info(f'inclinometer base x: {inclinometer.get_filter_on()}')
    logging.info(f'inclinometer base y: {inclinometer.get_length_filter()}')
    x = 0
    while x<camp1:    #numero di valori 200 200 100 50
        old = str(inclinometer.get_xy())
        new = old.replace(",", "")
        new2 = new.replace(")", "")
        new3 = new2.replace("(","")
        print (new3)
        logging.info(f'inclinometer xy: {inclinometer.get_xy()}')
        time.sleep(0.5)  #tempo in secondi  0.5 x 200  1x100 2x50
        x = x+1

######################################################################################################
    logging.info('Start')
    logging.info(f'inclinometer id: {inclinometer.get_id()}')
    inclinometer.set_filter_on(filtroON)  # numero di campionamenti
    inclinometer.set_length_filter(filtro_lenght)  # frequenza
    inclinometer.set_samples_per_measurements(5)  # numero di campionamenti
    inclinometer.set_sampling_rate(10)  # frequenza
    inclinometer.non_volatile_save()
    logging.info(f'inclinometer base x: {inclinometer.get_x()}')
    logging.info(f'inclinometer base y: {inclinometer.get_y()}')
    logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
    logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
    logging.info(f'inclinometer base x: {inclinometer.get_filter_on()}')
    logging.info(f'inclinometer base y: {inclinometer.get_length_filter()}')
    x = 0
    print("step")
    while x < camp1:  # numero di valori 200 200 100 50
        old = str(inclinometer.get_xy())
        new = old.replace(",", "")
        new2 = new.replace(")", "")
        new3 = new2.replace("(", "")
        print(new3)
        logging.info(f'inclinometer xy: {inclinometer.get_xy()}')
        time.sleep(0.5)  # tempo in secondi  0.5 x 200  1x100 2x50
        x = x + 1

    ######################################################################################################

    logging.info('Start')

    logging.info(f'inclinometer id: {inclinometer.get_id()}')


    inclinometer.set_filter_on(filtroON) #numero di campionamenti
    inclinometer.set_length_filter(filtro_lenght)   #frequenza
    inclinometer.set_samples_per_measurements(10) #numero di campionamenti
    inclinometer.set_sampling_rate(10)   #frequenza
    inclinometer.non_volatile_save()
    logging.info(f'inclinometer base x: {inclinometer.get_x()}')
    logging.info(f'inclinometer base y: {inclinometer.get_y()}')
    logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
    logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
    logging.info(f'inclinometer base x: {inclinometer.get_filter_on()}')
    logging.info(f'inclinometer base y: {inclinometer.get_length_filter()}')
    x = 0
    print("step")
    while x<camp2:    #numero di valori 200 200 100 50
        old = str(inclinometer.get_xy())
        new = old.replace(",", "")
        new2 = new.replace(")", "")
        new3 = new2.replace("(","")
        print (new3)
        logging.info(f'inclinometer xy: {inclinometer.get_xy()}')
        time.sleep(1)  #tempo in secondi  0.5 x 200  1x100 2x50
        x = x+1

######################################################################################################

    logging.info('Start')


    logging.info(f'inclinometer id: {inclinometer.get_id()}')


    inclinometer.set_filter_on(filtroON) #numero di campionamenti
    inclinometer.set_length_filter(filtro_lenght)   #frequenza
    inclinometer.set_samples_per_measurements(20) #numero di campionamenti
    inclinometer.set_sampling_rate(10)   #frequenza
    inclinometer.non_volatile_save()
    logging.info(f'inclinometer base x: {inclinometer.get_x()}')
    logging.info(f'inclinometer base y: {inclinometer.get_y()}')
    logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
    logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
    logging.info(f'inclinometer base x: {inclinometer.get_filter_on()}')
    logging.info(f'inclinometer base y: {inclinometer.get_length_filter()}')
    x = 0
    print("step")
    while x<camp3:    #numero di valori 200 200 100 50
        old = str(inclinometer.get_xy())
        new = old.replace(",", "")
        new2 = new.replace(")", "")
        new3 = new2.replace("(","")
        print (new3)
        logging.info(f'inclinometer xy: {inclinometer.get_xy()}')
        time.sleep(2)  #tempo in secondi  0.5 x 200  1x100 2x50
        x = x+1

######################################################################################################


    logging.info('Start')

    logging.info(f'inclinometer id: {inclinometer.get_id()}')


    inclinometer.set_filter_on(filtroON) #numero di campionamenti
    inclinometer.set_length_filter(filtro_lenght)   #frequenza
    inclinometer.set_samples_per_measurements(1) #numero di campionamenti
    inclinometer.set_sampling_rate(8)   #frequenza
    inclinometer.non_volatile_save()
    logging.info(f'inclinometer base x: {inclinometer.get_x()}')
    logging.info(f'inclinometer base y: {inclinometer.get_y()}')
    logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
    logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
    logging.info(f'inclinometer base x: {inclinometer.get_filter_on()}')
    logging.info(f'inclinometer base y: {inclinometer.get_length_filter()}')
    x = 0
    print("step")
    while x<camp1:    #numero di valori 200 200 100 50
        old = str(inclinometer.get_xy())
        new = old.replace(",", "")
        new2 = new.replace(")", "")
        new3 = new2.replace("(","")
        print (new3)
        logging.info(f'inclinometer xy: {inclinometer.get_xy()}')
        time.sleep(0.5)  #tempo in secondi  0.5 x 200  1x100 2x50
        x = x+1

######################################################################################################

    logging.info('Start')


    logging.info(f'inclinometer id: {inclinometer.get_id()}')


    inclinometer.set_filter_on(filtroON) #numero di campionamenti
    inclinometer.set_length_filter(filtro_lenght)   #frequenza
    inclinometer.set_samples_per_measurements(5) #numero di campionamenti
    inclinometer.set_sampling_rate(8)   #frequenza
    inclinometer.non_volatile_save()
    logging.info(f'inclinometer base x: {inclinometer.get_x()}')
    logging.info(f'inclinometer base y: {inclinometer.get_y()}')
    logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
    logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
    logging.info(f'inclinometer base x: {inclinometer.get_filter_on()}')
    logging.info(f'inclinometer base y: {inclinometer.get_length_filter()}')
    x = 0
    print("step")
    while x<camp1:    #numero di valori 200 200 100 50
        old = str(inclinometer.get_xy())
        new = old.replace(",", "")
        new2 = new.replace(")", "")
        new3 = new2.replace("(","")
        print (new3)
        logging.info(f'inclinometer xy: {inclinometer.get_xy()}')
        time.sleep(0.5)  #tempo in secondi  0.5 x 200  1x100 2x50
        x = x+1

######################################################################################################

    logging.info('Start')


    logging.info(f'inclinometer id: {inclinometer.get_id()}')


    inclinometer.set_filter_on(filtroON) #numero di campionamenti
    inclinometer.set_length_filter(filtro_lenght)   #frequenza
    inclinometer.set_samples_per_measurements(10) #numero di campionamenti
    inclinometer.set_sampling_rate(8)   #frequenza
    inclinometer.non_volatile_save()
    logging.info(f'inclinometer base x: {inclinometer.get_x()}')
    logging.info(f'inclinometer base y: {inclinometer.get_y()}')
    logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
    logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
    logging.info(f'inclinometer base x: {inclinometer.get_filter_on()}')
    logging.info(f'inclinometer base y: {inclinometer.get_length_filter()}')
    x = 0
    print("step")
    while x<camp2:    #numero di valori 200 200 100 50
        old = str(inclinometer.get_xy())
        new = old.replace(",", "")
        new2 = new.replace(")", "")
        new3 = new2.replace("(","")
        print (new3)
        logging.info(f'inclinometer xy: {inclinometer.get_xy()}')
        time.sleep(1)  #tempo in secondi  0.5 x 200  1x100 2x50
        x = x+1

######################################################################################################

    logging.info('Start')


    logging.info(f'inclinometer id: {inclinometer.get_id()}')


    inclinometer.set_filter_on(filtroON) #numero di campionamenti
    inclinometer.set_length_filter(filtro_lenght)   #frequenza
    inclinometer.set_samples_per_measurements(20) #numero di campionamenti
    inclinometer.set_sampling_rate(8)   #frequenza
    inclinometer.non_volatile_save()
    logging.info(f'inclinometer base x: {inclinometer.get_x()}')
    logging.info(f'inclinometer base y: {inclinometer.get_y()}')
    logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
    logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
    logging.info(f'inclinometer base x: {inclinometer.get_filter_on()}')
    logging.info(f'inclinometer base y: {inclinometer.get_length_filter()}')
    x = 0
    print("step")
    while x<camp3:    #numero di valori 200 200 100 50
        old = str(inclinometer.get_xy())
        new = old.replace(",", "")
        new2 = new.replace(")", "")
        new3 = new2.replace("(","")
        print (new3)
        logging.info(f'inclinometer xy: {inclinometer.get_xy()}')
        time.sleep(2)  #tempo in secondi  0.5 x 200  1x100 2x50
        x = x+1

######################################################################################################


    logging.info('Start')


    logging.info(f'inclinometer id: {inclinometer.get_id()}')


    inclinometer.set_filter_on(filtroON) #numero di campionamenti
    inclinometer.set_length_filter(filtro_lenght)   #frequenza
    inclinometer.set_samples_per_measurements(1) #numero di campionamenti
    inclinometer.set_sampling_rate(6)   #frequenza
    inclinometer.non_volatile_save()
    logging.info(f'inclinometer base x: {inclinometer.get_x()}')
    logging.info(f'inclinometer base y: {inclinometer.get_y()}')
    logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
    logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
    logging.info(f'inclinometer base x: {inclinometer.get_filter_on()}')
    logging.info(f'inclinometer base y: {inclinometer.get_length_filter()}')
    x = 0
    print("step")
    while x<camp1:    #numero di valori 200 200 100 50
        old = str(inclinometer.get_xy())
        new = old.replace(",", "")
        new2 = new.replace(")", "")
        new3 = new2.replace("(","")
        print (new3)
        logging.info(f'inclinometer xy: {inclinometer.get_xy()}')
        time.sleep(0.5)  #tempo in secondi  0.5 x 200  1x100 2x50
        x = x+1

######################################################################################################

    logging.info('Start')


    logging.info(f'inclinometer id: {inclinometer.get_id()}')


    inclinometer.set_filter_on(filtroON) #numero di campionamenti
    inclinometer.set_length_filter(filtro_lenght)   #frequenza
    inclinometer.set_samples_per_measurements(5) #numero di campionamenti
    inclinometer.set_sampling_rate(6)   #frequenza
    inclinometer.non_volatile_save()
    logging.info(f'inclinometer base x: {inclinometer.get_x()}')
    logging.info(f'inclinometer base y: {inclinometer.get_y()}')
    logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
    logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
    logging.info(f'inclinometer base x: {inclinometer.get_filter_on()}')
    logging.info(f'inclinometer base y: {inclinometer.get_length_filter()}')
    x = 0
    print("step")
    while x<camp1:    #numero di valori 200 200 100 50
        old = str(inclinometer.get_xy())
        new = old.replace(",", "")
        new2 = new.replace(")", "")
        new3 = new2.replace("(","")
        print (new3)
        logging.info(f'inclinometer xy: {inclinometer.get_xy()}')
        time.sleep(0.5)  #tempo in secondi  0.5 x 200  1x100 2x50
        x = x+1

######################################################################################################

    logging.info('Start')

    logging.info(f'inclinometer id: {inclinometer.get_id()}')


    inclinometer.set_filter_on(filtroON) #numero di campionamenti
    inclinometer.set_length_filter(filtro_lenght)   #frequenza
    inclinometer.set_samples_per_measurements(10) #numero di campionamenti
    inclinometer.set_sampling_rate(6)   #frequenza
    inclinometer.non_volatile_save()
    logging.info(f'inclinometer base x: {inclinometer.get_x()}')
    logging.info(f'inclinometer base y: {inclinometer.get_y()}')
    logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
    logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
    logging.info(f'inclinometer base x: {inclinometer.get_filter_on()}')
    logging.info(f'inclinometer base y: {inclinometer.get_length_filter()}')
    x = 0
    print("step")
    while x<camp2:    #numero di valori 200 200 100 50
        old = str(inclinometer.get_xy())
        new = old.replace(",", "")
        new2 = new.replace(")", "")
        new3 = new2.replace("(","")
        print (new3)
        logging.info(f'inclinometer xy: {inclinometer.get_xy()}')
        time.sleep(1)  #tempo in secondi  0.5 x 200  1x100 2x50
        x = x+1

######################################################################################################

    logging.info('Start')


    logging.info(f'inclinometer id: {inclinometer.get_id()}')


    inclinometer.set_filter_on(filtroON) #numero di campionamenti
    inclinometer.set_length_filter(filtro_lenght)   #frequenza
    inclinometer.set_samples_per_measurements(20) #numero di campionamenti
    inclinometer.set_sampling_rate(6)   #frequenza
    inclinometer.non_volatile_save()
    logging.info(f'inclinometer base x: {inclinometer.get_x()}')
    logging.info(f'inclinometer base y: {inclinometer.get_y()}')
    logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
    logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
    logging.info(f'inclinometer base x: {inclinometer.get_filter_on()}')
    logging.info(f'inclinometer base y: {inclinometer.get_length_filter()}')
    x = 0
    print("step")
    while x<camp3:    #numero di valori 200 200 100 50
        old = str(inclinometer.get_xy())
        new = old.replace(",", "")
        new2 = new.replace(")", "")
        new3 = new2.replace("(","")
        print (new3)
        logging.info(f'inclinometer xy: {inclinometer.get_xy()}')
        time.sleep(2)  #tempo in secondi  0.5 x 200  1x100 2x50
        x = x+1

######################################################################################################

'''