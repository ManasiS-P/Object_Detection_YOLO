from ultralytics import YOLO
import cv2

# Load trained model
model = YOLO("/Users/suhaspatil/manasi/Lexicon_Training_Labs/YOLO/Object_Detection_YOLO/runs/detect/yolo_training/weights/best.pt")

# Video path
video_path = "../Data/test/video/test_video.mp4"

cap = cv2.VideoCapture(video_path)

while cap.isOpened():

    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame, conf=0.25)

    # Draw detections
    annotated_frame = results[0].plot()

    # Show frame
    cv2.imshow("YOLO Video Detection", annotated_frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()