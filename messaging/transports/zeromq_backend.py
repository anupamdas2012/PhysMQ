# transports/zeromq_backend.py

def init():
    print("[ZeroMQ] Initializing ZeroMQ backend (stub)")

def publish(topic, message):
    print(f"[ZeroMQ] Publishing to {topic}: {message}")

def subscribe(topic, callback):
    print(f"[ZeroMQ] Subscribing to {topic}")
    # Simulate receiving a message
    callback(f"[ZeroMQ] Message from {topic}")
