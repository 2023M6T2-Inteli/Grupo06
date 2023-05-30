from ultralytics import YOLO 
import cv2

model = YOLO("best.pt")

def get_yolo_results():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        results = model(frame)

        annotated_frame = results[0].plot()

        # cv2.imshow("YOLOv8 Inference", annotated_frame)

        if not ret:
            break

        # Converte o frame para o formato JPEG
        ret, buffer = cv2.imencode('.jpg', annotated_frame)

        # Gera o frame como bytes
        frame_bytes = buffer.tobytes()

        # Retorna o frame como resposta de streaming
        yield (
            b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n'
        )
    # imagem = cv2.imread(img)
    # results = model(imagem)
    # annotated_frame = results[0].plot()
    # cv2.imshow("YOLOv8 Inference", annotated_frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()



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

# cv2.destroyAllWindows()