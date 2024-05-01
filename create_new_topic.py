import subprocess
from utils import load_config


def create_kafka_topic_from_config():
    """_summary_
    """

    conf = load_config('conf/config_variables.yml')
    topic = conf['topic']
    kafka_path = conf['kafka_path']

    # Build the shell command to create the Kafka topic
    command = f"{kafka_path}/bin/kafka-topics.sh --create --topic {topic} --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1"

    # Execute the command
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Topic '{topic}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create topic '{topic}': {e}")

if __name__ == "__main__":
    create_kafka_topic_from_config()
