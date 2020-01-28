#!/usr/bin/env python3

# import midi object library and set backend to pygame to allow access to midi ports.

import mido
import pygame.midi as pym
mido.set_backend('mido.backends.pygame')

pym.init()


class FMVel:
    def __init__(self):
        print(mido.get_input_names())
        self.in_port = mido.open_input(self.get_in_port())
        self.out_port = mido.open_output(self.get_out_port())

    @staticmethod
    def get_in_port():  # returns user-selected input port as a string
        port_no = int(input('Choose MIDI in port (index) from above list: '))
        return mido.get_input_names()[port_no]

    @staticmethod
    def get_out_port():  # returns user-selected output port as a string
        port_no = int(input('Choose MIDI out port (index) from above list: '))
        return mido.get_output_names()[port_no]

    @staticmethod
    def extract_velocity(msg):  # extracts note_on velocity value from a mido message and returns it as an int
        return int((str(msg).split()[3]).split('=')[1])

    def send_output(self, velo, msg):  # sends cc to assign velocity then note_on message
        v_msg = mido.Message('control_change', control=41, value=velo)
        self.out_port.send(v_msg)
        self.out_port.send(msg)

    def port_listen(self):  # listens for incoming MIDI message and sends to appropriate output
        msg = self.in_port.receive(block=False)
        if msg and 'note_on' in str(msg):
            self.send_output(self.extract_velocity(msg), msg)
        elif msg:
            self.out_port.send(msg)

    def end_program(self):  # closes MIDI ports and exits the program cleanly
        self.in_port.close()
        self.out_port.close()
        print('Terminated by User')
        exit(0)

    def control_method(self):  # loops FMVel.port_listen method and checks for user input
        while True:
            try:
                self.port_listen()
            except KeyboardInterrupt:
                self.end_program()


if __name__ == '__main__':
    test = FMVel()
    test.control_method()
