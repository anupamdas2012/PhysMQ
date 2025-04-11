import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")

topic_filter = "ledController"
socket.setsockopt_string(zmq.SUBSCRIBE, topic_filter)

for _ in range(5):  # Just to see a few messages
    string = socket.recv_string()
    topic, messagedata = string.split()
    print(f"Topic: {topic}, Message: {messagedata}")
