from ultralytics import YOLO 
import cv2

model = YOLO("best.pt")

def get_yolo_results(img):
    results = model.predict(img, conf=0.25, stream=True)
    return results

# Open the video file


# Loop through the video frames
# while cap.isOpened():
    # Read a frame from the video
# frame = cv2.imread("download (1).jpeg")

#         # Run YOLOv8 inference on the frame
# results = model(frame)

# # Visualize the results on the frame
# annotated_frame = results[0].plot()

# # Display the annotated frame
# cv2.imshow("YOLOv8 Inference", annotated_frame)

# # Break the loop if 'q' is pressed
# cv2.waitKey(0)


# Release the video capture object and close the display window

cv2.destroyAllWindows()