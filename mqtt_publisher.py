# publisher.py
import paho.mqtt.client as mqtt
import time

BROKER = 'localhost'
TOPIC = 'robot/blink'

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    message = "On"
    client.publish(TOPIC, message)
    print(f"Published: {message}")
    time.sleep(2)

    message = "Off"
    client.publish(TOPIC, message)
    print(f"Published: {message}")
    time.sleep(2)
