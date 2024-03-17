import cv2
import streamlit as st
import os
import uuid

# Initialize video capture object with webcam ID (0)
cap = cv2.VideoCapture(0)

st.title("Webcam Image Capture")

# Generate unique keys for buttons
capture_button_key = str(uuid.uuid4())
display_button_key = str(uuid.uuid4())

# Capture image and save to file
if st.button("Capture Image", key=capture_button_key):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # Generate a unique file name
        image_filename = "captured_image.jpg"
        cv2.imwrite(image_filename, frame)
        st.success(f"Image captured and saved to file: {os.path.abspath(image_filename)}")
    else:
        st.error("Error: Failed to capture frame from webcam!")

# Display the image saved to file
if st.button("Display Saved Image", key=display_button_key):
    if os.path.exists("captured_image.jpg"):
        saved_image = cv2.imread("captured_image.jpg")
        st.image(saved_image, channels="BGR")
    else:
        st.error("No image captured yet. Please capture an image first.")

# Release the video capture object
cap.release()
