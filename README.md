README: Refactoring and Integrating Pre-Trained Gesture Recognition Model
Project Overview

This repository contains the code for a gesture recognition model that has been refactored and integrated into a Flask API. The model is based on the GRT (Gesture Recognition Toolkit) library and provides a user-friendly interface to recognize various gestures.

Prerequisites

Before you can use this application, please ensure you have the following installed:

Python (version 3.6 or later)
GRT
Flask
Other required libraries (listed in requirements.txt)
Installation

Clone the Repository:
Bash
git clone https://github.com/maskedwolf4/Koach_task.git   

Install Dependencies:
pip install -r requirements.txt

Running the Application

Start the Flask Server:
python app.py


Access the API:
The API is available at http://localhost:5000
Send a POST request with the gesture data in the appropriate format (e.g., a list of feature values).
Example Usage

Python
import requests

gesture_data = [1.0, 2.0, 3.0, ...]  # Replace with your gesture data

response = requests.post('http://localhost:5000/recognize_gesture', json=gesture_data)
print(response.json())
Use code with caution.








