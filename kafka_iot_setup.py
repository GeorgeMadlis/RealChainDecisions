import time
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from kafka import KafkaProducer
import json

"""
To connect IoT devices for collecting in situ soil moisture data and 
integrate them with Apache Kafka installed on your Mac, 
follow these steps. This example assumes you have a soil moisture 
sensor like the one typically used in IoT projects for agriculture.

Step 1: Set Up Your IoT Device
Connect the Soil Moisture Sensor to an IoT device: This could be an 
Arduino, Raspberry Pi, or any other compatible microcontroller. 
Here's a general setup:
Connect the sensor's power pin to the 5V out on your microcontroller.
Connect the ground pin to the ground on your microcontroller.
Connect the output pin of the sensor to an analog input pin on your 
microcontroller for data reading.
2. Program the IoT Device: Write a script to read the soil moisture value 
from the sensor and send it to Kafka. Below is an example using a 
hypothetical sensor connected to a Raspberry Pi:
"""

# Create the MCP3008 object using SPI
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MCP3008
mcp = MCP.MCP3008(spi, cs)

# Create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda x: json.dumps(x).encode('utf-8'))

while True:
    moisture_level = chan.value
    producer.send('soilMoistureTopic', {'moisture_level': moisture_level})
    time.sleep(10)  # Delay for 10 seconds
    break
# ----------------------------
# Create a Topic: Open a terminal and navigate to your Kafka directory to create a topic named soilMoistureTopic:
# Bash command:
# bin/kafka-topics.sh --create --topic soilMoistureTopic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# 2. Set Up a Kafka Consumer: Create a consumer to listen to the soil moisture data. Here’s how you can do this in Python:
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'soilMoistureTopic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    print(f"Received data: {message.value}")

""" 
Step 3: Running the System
Start Zookeeper and Kafka if not already running.
Run your IoT device script to start sending data to Kafka.
Run your consumer script to start receiving and processing the soil moisture data.
"""
# =============================================
""" 
You're right in wondering about how Kafka, running locally on your machine, can 
communicate with your IoT device. In this setup, Kafka itself doesn't directly 
"find" the IoT device. Instead, the IoT device needs to be programmed to send 
data to the Kafka broker running on your local machine or network. 
Here’s how you can set this up:

1. Assign a Static IP or Use Hostname: First, ensure your IoT device is connected 
to the same network as your Kafka server. It's helpful if your IoT device has a 
static IP address or a resolvable hostname within your local network. 
This way, the IP address or hostname will remain consistent every time the device boots up.
2. Configure the IoT Device: Program your IoT device (e.g., a Raspberry Pi or 
Arduino with networking capabilities) to push data to Kafka. This typically 
involves using a Kafka client library compatible with your IoT platform and 
specifying the Kafka broker’s network address 
in the device’s code.Example for a Raspberry Pi in Python:

"""
from kafka import KafkaProducer
import json

# Assuming your Kafka server is on your local machine with default port
producer = KafkaProducer(bootstrap_servers='192.168.1.100:9092', # replace with your Kafka server IP
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Example data from your sensor
data = {'moisture_level': 1024}
producer.send('soilMoistureTopic', value=data)
producer.flush()

""" 
1. Configure Kafka to Accept Connections: Make sure your Kafka server’s configuration allows connections not just from 
localhost but also from other machines on your network. This involves setting the listeners property in your Kafka 
configuration to something like PLAINTEXT://your.machine.ip.address:9092.
Network Configuration: Ensure that there are no network firewalls blocking the communication between your IoT device 
and the Kafka broker.
In this setup, Kafka acts as a server waiting for messages, and the IoT device acts as a client that sends messages to Kafka. 
The IP address you provide in your IoT device's code should match the IP address of the machine where your Kafka broker is running.


"""