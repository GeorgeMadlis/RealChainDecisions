from kafka import KafkaConsumer
import json
import collections
import numpy as np
from river import drift
from utils import load_config


def run_consumer():
    """_summary_
    """
    conf = load_config('conf/config_variables.yml')
    consumer = KafkaConsumer(
        conf['topic'],
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    try:
        with open('messages.csv', 'w') as file:  # Open the file in write mode
            adwin = drift.ADWIN()
            for i, message in enumerate(consumer):
                data = message.value
                try:
                    val = data['value']
                    mess_nr = data['number']
                    # print(f"Value accessed: {val}")
                except KeyError:
                    val=None
                    mess_nr = None
                    print("Key 'value' not found in dictionary")
                except TypeError:
                    val=None
                    mess_nr = None
                    print("dd is not a dictionary")
                if val:
                    adwin.update(val)
                if adwin.drift_detected:
                    print(f"Change detected at index, {mess_nr}, input value, {val}")
                    file.write(f"Change detected at index, {mess_nr}, input value, {val}\n")
                else:
                    # print(f"No changes detected, {mess_nr}, input value, {val}")
                    print(f"{mess_nr}, value, {val}")
                    file.write(f"No changes detected, {mess_nr}, input value, {val}\n")
                    file.flush()

    except KeyboardInterrupt:
        print("Consumer shutdown requested")
    finally:
        consumer.close()
        print("Consumer has been closed gracefully")


# To start the consumer
if __name__ == "__main__":
    run_consumer()
