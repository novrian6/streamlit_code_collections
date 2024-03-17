import cv2
import streamlit as st

# Initialize video capture object with webcam ID (0)
cap = cv2.VideoCapture(0)

st.title("Webcam Image Capture")

# Main loop to display webcam feed
while True:
  # Capture frame-by-frame
  ret, frame = cap.read()

  # Display the webcam feed on Streamlit
  if ret:
    st.image(frame, channels="BGR")  # Specify BGR channels for OpenCV images
  else:
    st.error("Error: Failed to capture frame from webcam!")
    break

  # Optionally add a quit button to break the loop
  # if st.button("Stop Webcam"):
  #   break

  # Display at a specific frame rate (adjust fps as needed)
  key = cv2.waitKey(1) & 0xFF
  if key == ord('q'):
    break

# Release the video capture object
cap.release()

