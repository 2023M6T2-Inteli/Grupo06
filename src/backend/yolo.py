from ultralytics import YOLO 
import cv2
model = YOLO("best.pt")

def get_yolo_results():
    # Open the video file - webcam
    cap = cv2.VideoCapture(1)

    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        results = model(frame)

        # Visualize the results on the frame
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
