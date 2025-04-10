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

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/physmq.git
cd physmq

### 2. install deps
python3 -m venv mqtt-venv
source mqtt-venv/bin/activate
pip install paho-mqtt

### 3. install broker
sudo apt-get install mosquitto mosquitto-clients

### 4. start broker and check that broker has started
sudo systemctl start mosquitto 
sudo systemctl status mosquitto

### 5. enable broker on boot (optional)
sudo systemctl enable mosquitto



