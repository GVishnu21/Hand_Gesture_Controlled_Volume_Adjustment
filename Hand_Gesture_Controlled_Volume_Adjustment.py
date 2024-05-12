import cv2
import mediapipe as mp
import pyautogui

# Constants
DISTANCE_THRESHOLD = 50

# Initialize webcam
webcam = cv2.VideoCapture(0)

# Initialize mediapipe Hands
my_hands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

while True:
    # Read frame from webcam
    _, image = webcam.read()
    image = cv2.flip(image, 1)

    # Get frame dimensions
    frame_height, frame_width, _ = image.shape

    # Convert image to RGB format
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process hand landmarks
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            # Draw hand landmarks on the image
            drawing_utils.draw_landmarks(image, hand)
            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                # Detect specific landmarks for volume control
                if id == 8:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    start_x = x
                    start_y = y

                if id == 4:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 0, 255), thickness=3)
                    end_x = x
                    end_y = y

        # Calculate distance between two points
        distance = ((end_x - start_x) ** 2 + (end_y - start_y) ** 2) ** 0.5 // 4

        # Adjust volume based on distance threshold
        if distance > DISTANCE_THRESHOLD:
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

    # Display image with volume control visualization
    cv2.imshow("Hand volume control using Python", image)

    # Wait for ESC key to exit
    key = cv2.waitKey(10)
    if key == 27:
        break

# Release webcam and close all OpenCV windows
webcam.release()
cv2.destroyAllWindows()
