# IoT Stream Simulation Setup

This guide describes the process to simulate an IoT single channel time series data stream using Apache Kafka and ZooKeeper on a Mac. Following these steps will allow you to simulate a data stream for IoT applications, testing consumer and producer scripts in a controlled environment on your Mac. Each terminal command is isolated to its specific function to maintain clarity and ease of troubleshooting

## Initial Setup
Before starting, ensure that you have followed the `installation.md` instructions to install and configure Kafka and ZooKeeper. Make sure your PATH is appropriately configured or use direct paths to execute commands.

## Terminal Windows Setup

### Terminal 1: Run ZooKeeper
- **Directory:** Navigate to the Kafka home directory if not added to PATH.
  ```bash
  cd streaming
- **Command:**  
  ```bash
  bin/zookeeper-server-start.sh config/zookeeper.properties

### Terminal 2: Run Kafka Server
- **Directory: Navigate to the directory containing the Python script.**
    ```bash
    cd streaming
- **Command:**
    ```bash
    bin/kafka-server-start.sh config/server.properties

### Terminal 3: Create Kafka Topic
- **Directory: Navigate to the directory containing the Python script.**
    ```bash
    cd demos
- **Command:**
    ```bash
    python create_new_topic.py

### Terminal 4: Run Kafka Producer
- **Directory:**  
    ```bash
    cd demos
- **Command:**
    ```bash
    python kafka_producer_two_gaussians.py

### Terminal 5: Run Kafka Consumer
- **Directory:**
    ```bash
    cd demos
- **Command:**
    ```bash
    python kafka_consumer_drift_detection.py
- **Note: After stopping the kafka_producer_two_gaussians.py, terminate the consumer using:**
    ```bash
    CTRL-C

### Terminal 6: Stop Kafka and ZooKeeper
- **Directory:**
    ```bash
    cd streaming
- **Commands: First, stop Kafka then ZooKeeper.**
    ```bash
    bin/kafka-server-stop.sh
    bin/zookeeper-server-stop.sh
