import json
import time
import numpy as np
from kafka import KafkaProducer
from utils import load_config


def run_producer():
    """_summary_
    """
    conf = load_config('conf/config_variables.yml')
    producer = KafkaProducer(bootstrap_servers='localhost:9092',
                             value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    # Define parameters for Gaussian distributions
    mu_one, sigma_one = conf['mu_one'], conf['sigma_one']  # Mean and standard deviation for distribution One
    mu_two, sigma_two = conf['mu_two'], conf['sigma_two']  # Mean and standard deviation for distribution Two

    try:
        for i in range(conf['n_timeseries']+1):
            if 0 <= i <= int(conf['n_timeseries']/2):
                value = np.random.normal(mu_one, sigma_one)
            elif (int(conf['n_timeseries']/2)+1) <= i <= conf['n_timeseries']:
                value = np.random.normal(mu_two, sigma_two)
            
            data = {'value': value, 'number': i}
            producer.send(conf['topic'], value=data)
            time.sleep(1)  # Sleep to simulate time delay for data generation

    except KeyboardInterrupt:
        print("Producer shutdown requested")
    finally:
        producer.flush()
        producer.close()
        print("Producer has been closed gracefully")


# To start the producer
if __name__ == "__main__":
    run_producer()
