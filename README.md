# PhysMQ

**PhysMQ** is a lightweight, high-performance robotics framework designed for real-time messaging and modular control across multiple devices. Inspired by the strengths of ROS2 but streamlined for simplicity and speed, PhysMQ brings pub-sub architecture to small-scale and hobbyist robotics without the overhead.

## Architecture

https://docs.google.com/presentation/d/1f1eRD8RnnVLCw0jto0wMqtCDd42WziRb9aMDKrXjFuY/edit?usp=sharing
---

## Features

- **Fast and Minimal Pub-Sub Architecture**
  Zero-boilerplate messaging system optimized for embedded systems and distributed robots.

- **Multi-Device Communication**
  Seamlessly connect microcontrollers, SBCs, and desktop machines over serial, Wi-Fi, or Bluetooth.

- **Modular and Reusable Components**
  Build your robot from loosely coupled modules that are easy to plug, swap, and extend.

- **ROS2-Compatible Ideas, Hobbyist-Friendly Implementation**
  Retains the reusability of ROS2 nodes but avoids the complexity and latency.

- **Real-Time Control**
  Designed for ultra-low-latency messaging in control loops and sensor feedback.

---
## NOTE, we depricated the MQTT version in favor of ZeroMQ. This elimates the need for a broker
## the mqtt version is prefized mqtt_

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/physmq.git
cd physmq

### 2. install deps (ZeroMQ)
python3 -m venv venv
source venv/bin/activate
pip install pyzmq

### 3. start subscriber
python3 subscriber.py

### 4. start publisher
python3 publisher.py

### 4. Note topic pub/sub output in console

### 5: ZeroMQ pubsub pattern tutorial:
https://learning-0mq-with-pyzmq.readthedocs.io/en/latest/pyzmq/patterns/pubsub.html




