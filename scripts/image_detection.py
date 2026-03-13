from ultralytics import YOLO
import cv2


model = YOLO("/Users/suhaspatil/manasi/Lexicon_Training_Labs/YOLO/Object_Detection_YOLO/runs/detect/yolo_training/weights/best.pt")


image_path = "/Users/suhaspatil/manasi/Lexicon_Training_Labs/YOLO/Object_Detection_YOLO/Data/test/images/64px-LG_mobile_phone_A3_jpg.rf.e7c9cd7e43d265f993d9a73da9c0888a.jpg"
#image_path = "/Users/suhaspatil/manasi/Lexicon_Training_Labs/YOLO/Object_Detection_YOLO/Data/test/images/128px-GMU_Mason_Votes_Election_Day_023_-3004504980-_jpg.rf.ab8bd99677b2a15a63f28f7f73f75509.jpg"

results = model.predict(
    source=image_path,
    conf=0.25,
    save=True
)


for r in results:
    print(r.boxes.cls)  
    print(r.boxes.conf)  
    img = r.plot()

    cv2.imshow("Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()