# Hand Gesture Controlled Volume Adjustment

This project utilizes computer vision and gesture recognition techniques to control the volume of a system using hand gestures captured by a webcam. The system detects specific hand gestures, such as raising or lowering fingers, and adjusts the volume accordingly in real-time.

  Key Features:
- Utilizes the Mediapipe library for hand tracking and landmark detection.
- Implements OpenCV for real-time webcam video processing.
- Interacts with the system's volume control using the PyAutoGUI library.
- Provides visual feedback by overlaying hand landmarks and connecting lines on the video stream.

  How it Works:
- The program captures video frames from the webcam and processes them to detect hand landmarks using the Mediapipe Hands model.
- It identifies specific landmarks on the hand, such as the tip of the index finger and thumb.
- Based on the relative positions of these landmarks, the program calculates the distance between them to determine the desired volume adjustment.
- If the distance exceeds a predefined threshold, the program sends commands to the system to increase or decrease the volume using PyAutoGUI.

  Usage:
- Run the Python script on a system with a webcam and sound output capabilities.
- Raise or lower your hand in front of the webcam to adjust the volume.
- Ensure proper lighting conditions and hand visibility for accurate gesture detection.

  Dependencies:
- Python 3.x
- OpenCV
- Mediapipe
- PyAutoGUI

Note: This project is for educational and experimental purposes and may require adjustments for optimal performance on different systems.
