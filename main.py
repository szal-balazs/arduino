import serial
import time
from datetime import datetime as dt


def reading_data():
    arduino = serial.Serial('COM3', 9600)
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    data = str(dt.now()) + "," + decoded_values

    arduino.close()

    return data


def writing_data(data):
    file = open("data.txt", "a")
    file.write(f"{data}")
    file.close()


def main():
    writing_data(reading_data())


if __name__ == "__main__":
    while True:
        main()
        time.sleep(10)
