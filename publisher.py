import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

topic = "ledController"
state = "ON"

time.sleep(1)  # Let subscribers connect

while True:
    message = f"{topic} {state}"
    print(f"Sent: {message}")
    socket.send_string(message)
    time.sleep(2)
    state = "OFF" if state == "ON" else "ON"
