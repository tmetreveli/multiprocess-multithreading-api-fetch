# Parallel Data Fetcher

# Overview
Parallel Data Fetcher is a Python-based tool designed to efficiently fetch data from an API in parallel using both multiprocessing and multithreading techniques. This project utilizes the concurrent.futures module to implement parallelism, aiming to improve the speed and efficiency of data retrieval tasks. It is specifically tailored to fetch information from the "https://dummyjson.com/products/" API, handling requests across multiple processes and threads to minimize response time and efficiently manage I/O operations.

# Requirements
Python 3.x

# Installation
1. Ensure you have Python 3.x installed on your system.
2. Install the requests library. This project requires requests to make HTTP calls to the API. Install it using pip:
pip install requirements.txt
3. Clone this repository or download the project files to your local machine.

# Usage
python main.py

# Features
Parallel Processing: Utilizes multiprocessing to distribute tasks across multiple CPU cores.
Thread Pooling: Implements multithreading within each process for concurrent API requests.
Efficient Data Handling: Collects and stores API responses in JSON format, ensuring data is easily accessible and manipulable.
Error Handling: Includes basic error handling to manage timeouts and request failures, ensuring the robustness of data fetching operations.

# Output
The script saves the fetched data into a file named sample.json. Each entry in the JSON file represents a product's data as returned by the "dummyjson" API. The data is formatted for readability, with each product's information indented.

The console output will display the total time taken to load all the data, providing an insight into the efficiency gained through multithreading.
