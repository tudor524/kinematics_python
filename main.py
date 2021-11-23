from pyfirmata import Arduino, SERVO
import serial.tools.list_ports


# establishes connection with your arduino board
def get_ports():
    ports = serial.tools.list_ports.comports()
    return ports


def find_arduino(ports_found):
    com_port = 'None'
    num_connection = len(ports_found)
    for i in range(0, num_connection):
        port = found_ports[i]
        str_port = str(port)
        if 'CH340' in str_port:  # this may need to be adjusted depending on your board type
            split_port = str_port.split(' ')
            com_port = (split_port[4])
    return com_port.translate(str.maketrans({"(": "", ")": ""}))


found_ports = get_ports()
connect_port = find_arduino(found_ports)

if connect_port != 'None':
    board = Arduino(connect_port)


# main functions to actuate the servos
class Servo:
    def __init__(self, angle, pin):
        self.angle = angle
        self.pin = pin

    def home(self):
        board.digital[self.pin].mode = SERVO
        for i in range(self.angle, 0, -1):
            board.digital[self.pin].write(i)

    def rotate_servo(self):
        board.digital[self.pin].mode = SERVO
        for i in range(0, self.angle, 1):
            board.digital[self.pin].write(i)
