# transports/mqtt_backend.py

def init():
    print("[MQTT] Initializing MQTT backend (stub)")

def publish(topic, message):
    print(f"[MQTT] Publishing to {topic}: {message}")

def subscribe(topic, callback):
    print(f"[MQTT] Subscribing to {topic}")
    # Simulate receiving a message
    callback(f"[MQTT] Message from {topic}")
