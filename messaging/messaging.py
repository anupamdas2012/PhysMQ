#pub/sub messaging

class Messaging:
    def __init__(self, backend='mqtt'):
        if backend == 'mqtt':
            from messaging.transports import mqtt_backend as backend_impl
        elif backend == 'zeromq':
            from messaging.transports import zeromq_backend as backend_impl
        else:
            raise ValueError(f"Unsupported backend: {backend}")

        self.backend = backend_impl
        self.backend.init()

    def publish(self, topic, message):
        self.backend.publish(topic, message)

    def subscribe(self, topic, callback):
        self.backend.subscribe(topic, callback)
