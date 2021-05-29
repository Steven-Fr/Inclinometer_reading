import minimalmodbus, serial
import struct


class InclinometerJdi200:
    def __init__(self, serial_port_name, rs485_address):
        self.instrument = minimalmodbus.Instrument(serial_port_name, rs485_address)
        self.instrument.serial.baudrate = 19200
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = serial.PARITY_EVEN
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout = 0.05
        self.instrument.mode = minimalmodbus.MODE_RTU
        self.instrument.clear_buffers_before_each_transaction = True

    def get_id(self):
        return self.instrument.read_string(24, number_of_registers=8).rstrip(chr(0))

    def get_x(self):
        return self.instrument.read_float(206)

    def get_y(self):
        return self.instrument.read_float(208)

    def get_xy(self):
        data = self.instrument.read_string(206, number_of_registers=4)

        x_float = minimalmodbus._bytestring_to_float(data[0:4])
        y_float = minimalmodbus._bytestring_to_float(data[4:8])

        return x_float, y_float

    def get_sample_for_measurement(self):
        return self.instrument.read_registers(300,1)
    def get_sampling_rate(self):
        return self.instrument.read_registers(301,1)

    def get_filter_on(self):
        return self.instrument.read_registers(320,1)
    def get_length_filter(self):
        return self.instrument.read_registers(321,1)


    def set_sampling_rate(self, sampling_rate):
        """
        0: 4000 Hz
        1: 2000 Hz
        2: 1000 Hz
        3: 500 Hz
        4: 250 Hz
        5: 125 Hz
        6: 62.5 Hz
        7: 31.25 Hz
        8: 15.625 Hz
        9: 7.813 Hz
        10: 3.906 Hz
        """

        max_retry = 3
        while max_retry > 0:
            try:
                # curr_sampling_rate = self.get_sampling_rate()
                # if curr_sampling_rate != sampling_rate:
                return self.instrument.write_register(301, sampling_rate, functioncode=6)
            except:
                self.main_log.info('inclinometer: NoResponseError, will retry {} times'.format(max_retry))
            max_retry -= 1

        raise custom_exceptions.DronexNoResponse()


    def set_samples_per_measurements(self, n_samples):
        """
        1 <= n_samples <= 4096        """

        if n_samples==0:
            n_samples = 1

        max_retry = 3
        while max_retry > 0:
            try:
                # curr_n_samples = self.get_samples_per_measurements()
                # if curr_n_samples != n_samples:
                return self.instrument.write_register(300, n_samples, functioncode=6)
            except:
                self.main_log.info('inclinometer: NoResponseError, will retry {} times'.format(max_retry))
            max_retry -= 1

        raise custom_exceptions.DronexNoResponse()

    def save_inclinometer_parameter(self):

        max_retry = 3
        while max_retry > 0:
            try:
                self.inclinometer.non_volatile_save()
                return
            except:
                self.main_log.info('inclinometer: NoResponseError, will retry {} times'.format(max_retry))
            max_retry -= 1

        raise custom_exceptions.DronexNoResponse()

    def set_filter_on(self, filteron):
        max_retry = 3
        while max_retry > 0:
            try:
                # curr_sampling_rate = self.get_sampling_rate()
                # if curr_sampling_rate != sampling_rate:
                return self.instrument.write_register(320, filteron, functioncode=6)
            except:
                self.main_log.info('inclinometer: NoResponseError, will retry {} times'.format(max_retry))
            max_retry -= 1

        raise custom_exceptions.DronexNoResponse()


    def set_length_filter(self, length_filteron):
        max_retry = 3
        while max_retry > 0:
            try:
                # curr_sampling_rate = self.get_sampling_rate()
                # if curr_sampling_rate != sampling_rate:
                return self.instrument.write_register(321, length_filteron, functioncode=6)
            except:
                self.main_log.info('inclinometer: NoResponseError, will retry {} times'.format(max_retry))
            max_retry -= 1

        raise custom_exceptions.DronexNoResponse()

    def non_volatile_save(self):
        # self.instrument.write_register(312, 20051)  # 20051 is 'ns' in decimal
        self.instrument.write_bit(2, 1)
        pass



