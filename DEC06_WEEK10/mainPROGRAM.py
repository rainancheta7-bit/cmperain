import serial
import time
import threading

serialInstance = serial.Serial("COM1", 9600, timeout=1)
time.sleep(2)

def send(message):
    serialInstance.write((message + '\n').encode("utf-8"))
    print(f"Napasok na mensahe: {message}")


def receive():
    if serialInstance.in_waiting > 0:
        data = serialInstance.readline().decode("utf-8")
        if data:
            print(f"received: {data}")
            return data
    return None

def receive_continuous():
    while True:
        received_data = receive()
        time.sleep(0.1)

received_thread_instance = threading.Thread(target=receive_continuous, daemon=True)
received_thread_instance.start()

try:
    while True:
        message = input("Enter Message: ")
        if message:
            send(message)
except KeyboardInterrupt:
    print("adieu...")
finally:
    serialInstance.close()