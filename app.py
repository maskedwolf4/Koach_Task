from flask import Flask, Response, request, jsonify
import cv2
import numpy as np
from grt import GRT

app = Flask(__name__)

# Loading the pre-trained GRT model
grt_model = GRT()

# Function to preprocess the video frames
def preprocess_frame(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Apply thresholding to segment out the hand
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return thresh

# Function to recognize gestures
def recognize_gesture(frame):
    # Preprocess the frame
    preprocessed_frame = preprocess_frame(frame)
    # Recognize the gesture using the GRT model
    gesture = grt_model.recognize(preprocessed_frame)
    return gesture

# Route for the gesture recognition endpoint
@app.route('/recognize_gesture', methods=['POST'])
def recognize_gesture_endpoint():
    # Get the video frame from the request
    frame = request.get_json()['frame']
    # Convert the frame to a NumPy array
    frame = np.array(frame)
    # Recognize the gesture
    gesture = recognize_gesture(frame)
    # Return the recognized gesture as JSON
    return jsonify({'gesture': gesture})

# Route for the video feed endpoint
@app.route('/video_feed', methods=['GET'])
def video_feed_endpoint():
    # Return a response with the video feed
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Function to generate video frames
def gen_frames():
    # Initialize the video capture device
    cap = cv2.VideoCapture(0)
    while True:
        # Read a frame from the video capture device
        ret, frame = cap.read()
        if not ret:
            break
        # Yield the frame
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + cv2.imencode('.jpg', frame)[1].tobytes() + b'\r\n')

if __name__ == '__main__':
    app.run(debug=True)