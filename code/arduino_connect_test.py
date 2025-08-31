import serial
import time
import random

# Replace 'COM3' with the appropriate port for your Arduino
arduino = serial.Serial('COM3', 9600)

while True:
    # Randomly select a command (G, R, Y, or A)
    command = random.choice(['G', 'R', 'Y', 'A'])

    # Send the selected command to Arduino
    arduino.write(command.encode())

    # Wait for a short duration before sending the next command
    time.sleep(2)
