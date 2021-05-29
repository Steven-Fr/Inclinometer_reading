import logging
from inclinometer_jdi200 import InclinometerJdi200
import time
import os, sys
from tkinter import *
import tkinter
from tkinter import messagebox
import tkinter as tk
import re
from os.path import exists



top = tkinter.Tk()
top.title("Reading inclinometer data (© F.Steven) V 1.0.0")
top.geometry('450x380')

status = False
filter_on = 1
def isClicked():
    global status
    global filter_on
    status = not status

    if status:
        filter_on = 0
        b2["text"] = "OFF"

    else:
        filter_on = 1
        b2["text"] = "ON"
    print (filter_on)



def attesa():
    L3 = Label(top, text=     "Wait for the data to be processed" , fg="red",anchor='w')
    L3.pack( padx = 50, pady = 5)
    L3.place ( x = 250, y = 160)
    L3.update_idletasks()
    L3.wait_visibility()

def Check():
    global filter_on
    try:

        id1 = int(E1.get())
        com = E2.get()
        ncamp = int(E3.get())
        srate = int(E4.get())
        nlinee = int(E5.get())
        wtemp = float(E6.get())
        f_on = filter_on
        f_length = int(E8.get())

        logging.basicConfig(filename = "Inclinometer_measurements.txt", filemode = 'w', level=logging.DEBUG, format='%(message)s')

        logging.info('Start')
        inclinometer = InclinometerJdi200("COM"+com, id1)
        inclinometer.set_filter_on(f_on) #numero di campionamenti
        inclinometer.set_length_filter(f_length)   #frequenza
        inclinometer.set_samples_per_measurements(ncamp) #numero di campionamenti
        inclinometer.set_sampling_rate(srate)   #frequenza
        inclinometer.non_volatile_save()


        logging.info(f'inclinometer id: {inclinometer.get_id()}')
        logging.info(f'filter on/off: {inclinometer.get_filter_on()}')
        logging.info(f'filter length: {inclinometer.get_length_filter()}')
        logging.info(f'inclinometer sample for measurement: {inclinometer.get_sample_for_measurement()}')
        logging.info(f'inclinometer sampling rate: {inclinometer.get_sampling_rate()}')
        x = 0
        while x< nlinee:    #numero di valori 200 200 100 50
            old = str(inclinometer.get_xy())
            new = old.replace(",", "")
            new2 = new.replace(")", "")
            new3 = new2.replace("(","")
            time.sleep(wtemp)  #tempo in secondi  0.5 x 200  1x100 2x50
            x = x+1
            logging.info(new3)
        L3 = Label(top, text=     "File di output concluso                " , fg="red",anchor='w')
        L3.pack( padx = 50, pady = 5)
        L3.place ( x = 250, y = 160)

    except:
        L3 = Label(top, text=     "Parameter insertion error         " , fg="red",anchor='w')
        L3.pack( padx = 50, pady = 5)
        L3.place ( x = 250, y = 160)

#label
L1 = Label(top, text="ID inclinometer (last 2 number):")
L1.pack( padx = 200, pady = 5)
L1.place ( x = 10, y = 5)
#entry
E1 = Entry(top, bd =2)
E1.pack(padx = 200, pady = 5)
E1.place(x = 10, y = 35)
#label2
L2 = Label(top, text="Number port COM:")
L2.pack( padx = 200, pady = 5)
L2.place ( x = 10, y = 65)
#entry
E2 = Entry(top, bd =2)
E2.pack(padx = 200, pady = 5)
E2.place(x = 10, y = 95)
#labe3
L3 = Label(top, text="Sample for measurement:")
L3.pack( padx = 200, pady = 5)
L3.place ( x = 10, y = 125)
#entry
E3 = Entry(top, bd =2)
E3.pack(padx = 200, pady = 5)
E3.place(x = 10, y = 155)
#label4
L4 = Label(top, text="Sampling rate (0..10):")
L4.pack( padx = 200, pady = 5)
L4.place ( x = 10, y = 185)
#entry
E4 = Entry(top, bd =2)
E4.pack(padx = 200, pady = 5)
E4.place(x = 10, y = 215)
#label5
L5 = Label(top, text="Number of value save")
L5.pack( padx = 200, pady = 5)
L5.place ( x = 10, y = 245)
#entry
E5 = Entry(top, bd =2)
E5.pack(padx = 200, pady = 5)
E5.place(x = 10, y = 275)
#label6
L6 = Label(top, text="Sampling rate (sec.)")
L6.pack( padx = 200, pady = 5)
L6.place ( x = 10, y = 305)
#entry
E6 = Entry(top, bd =2)
E6.pack(padx = 200, pady = 5)
E6.place(x = 10, y = 335)

#bottone
b = tkinter.Button(top, text= "          Scan               ",bd =4 , command = lambda:[attesa(),Check()])
b.pack(padx = 50, pady = 20)
b.place(x = 250, y = 5)


L7 = Label(top, text="Activate filter")
L7.pack( padx = 200, pady = 5)
L7.place ( x = 250, y = 55)

b2 = tkinter.Button(top, text= "ON",bd =4 , command = isClicked)
b2.pack(padx = 50, pady = 20)
b2.place(x = 330, y = 50)

L8 = Label(top, text="Length filter (3...32)")
L8.pack( padx = 200, pady = 5)
L8.place ( x = 250, y = 90)
E8 = Entry(top, bd =2)
E8.pack(padx = 200, pady = 5)
E8.place(x = 250, y = 120)

def quit():
    top.destroy()
    sys.exit()

#quit
top.protocol('WM_DELETE_WINDOW', quit)


#loop
top.mainloop()
