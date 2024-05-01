# Functionality of IoT Stream Simulation

## Overview
The current functionality of the IoT simulation is defined by two primary scripts:
- `kafka_producer_two_gaussians.py`
- `kafka_consumer_drift_detection.py`

These scripts are designed to demonstrate the ability to detect significant changes in time series probability distributions, which are continuously estimated across the subwindows of a running window.

## Simulation Details
- **Time Series Generation**: The `kafka_producer_two_gaussians.py` is responsible for simulating the underlying processes that generate the time series. This simulated data may differ significantly from what might be observed in a real-world measurement stream.
- **Change Detection**: The `kafka_consumer_drift_detection.py` focuses on detecting abrupt changes within the generated time series.

## Challenges
- **Understanding Underlying Physics**: Without a thorough understanding of the physics behind the measured time series, or prior statistical data, it becomes challenging to establish accurate assumptions for our change detection algorithm.

## Future Work
Further development is needed to align the simulation closer to real-world scenarios and enhance the accuracy of the detection algorithms used.
