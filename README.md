# AI-Driven Threat Detection System
This project is an AI-driven threat detection system designed to analyze network traffic and identify potential anomalies. It uses a machine learning model (Isolation Forest) to detect suspicious activities within a network by distinguishing between normal and abnormal traffic patterns.

## Project Structure
- ai_threat_detection.py: The main script that trains and tests the anomaly detection model using synthetic network traffic data.
- generate_synthetic_network_data.py: Script to generate synthetic network traffic data for training and testing the model.
- generate_synthetic_traffic.py: Script to generate synthetic network packets and save them in a .pcap file (Packet Capture).

## Prerequisites
- Python 3.x
- Required Python libraries:
- numpy
- pandas
- scikit-learn
- scapy
You can install the required libraries using pip: `pip install numpy pandas scikit-learn scapy`
`pip install scapy`

## How to Run the Project
1. Generate Synthetic Network Traffic Data:
- Run the `generate_synthetic_network_data.py` script to create synthetic network traffic data.
- This will generate a CSV file (synthetic_network_data.csv) containing both normal and abnormal traffic data.
- `python generate_synthetic_network_data.py`
2. Train and Test the Model:
- Run the `ai_threat_detection.py` script to train the Isolation Forest model on the synthetic data and evaluate its performance.
- The script will output the training and testing accuracy along with a classification report.
- `python ai_threat_detection.py`
3. Generate Synthetic Network Packets:
- Run the `generate_synthetic_traffic.py` script to create synthetic network packets and save them in a `.pcap` file.
- This file can be used for further analysis or as input to network monitoring tools.
- `python generate_synthetic_traffic.py`

## Project Overview
`ai_threat_detection.py`
- Purpose: Trains an Isolation Forest model to detect anomalies in network traffic.
- Key Steps:
1. Generates synthetic normal and abnormal network traffic data.
2. Splits the data into training and testing sets.
3. Trains the model on the training data.
4. Evaluates the model using the testing data.
5. Outputs accuracy and classification metrics.
`generate_synthetic_network_data.py`
- Purpose: Generates synthetic network traffic data, combining normal and abnormal patterns, and saves it as a CSV file.
`generate_synthetic_traffic.py`
- Purpose: Creates synthetic network packets using random IP addresses and TCP ports, saving them as a `.pcap` file for analysis.

## Usage
This project can be a starting point for developing more advanced network security systems. It demonstrates how machine learning models can be applied to network traffic data to detect potential threats in real-time.

## Potential Enhancements
To elevate the project to an intermediate level:
- Integrate real network traffic data for more realistic testing.
- Implement additional machine learning models and compare their performance.
- Include feature engineering techniques to extract more meaningful features from the network data.
- Build a real-time detection system that monitors live network traffic.
- Add a GUI to visualize the detection results.

## Author
Melisa Sever
