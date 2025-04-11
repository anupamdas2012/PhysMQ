# tests/test_messaging.py

from messaging.messaging import Messaging

def handle_message(msg):
    print(f"Received: {msg}")

print("=== Using MQTT ===")
messenger = Messaging(backend='mqtt')
messenger.publish("robot/led", "ON")
messenger.subscribe("robot/led", handle_message)

print("\n=== Using ZeroMQ ===")
messenger = Messaging(backend='zeromq')
messenger.publish("robot/led", "OFF")
messenger.subscribe("robot/led", handle_message)
