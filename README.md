In this lab you will work in groups to build your own object detection system using YOLO. You may choose your own group members. The goal is to experience how real computer vision projects are developed collaboratively, from data collection to a working detection model.
Imagine you are designing vision for a small robot that must recognize everyday objects placed on a table. Your group’s task is to train a model that can detect three object types: a red cup, a blue bottle, and a phone.
 
You may create your own dataset by taking between 150 and 300 photos with a phone or laptop camera. Capture the objects from different angles and distances, in different lighting conditions, and with varied backgrounds. Sometimes photograph a single object, and sometimes place multiple objects together so they overlap or partially hide each other. This variation is important because it teaches the model to recognize objects in realistic conditions rather than memorizing one view.
 
If you do not have access to a camera, you can download images from the web instead. Search for openly licensed images and gather a similar number of pictures for each object category. Make sure the images show variation in viewpoint, scale, lighting, and background so the dataset remains realistic and balanced.
 
Next, label your images by drawing bounding boxes around each object and assigning the correct class name. You can use annotation tools such as LabelImg or Roboflow. Export the annotations in YOLO format and organize your dataset into training and validation folders for both images and labels. This structure allows the model to learn from one set of images and be evaluated on another.
After your dataset is ready, set up a Python deep learning environment and install the required libraries. You will use the official YOLO implementation provided by Ultralytics. Once installed, connect your dataset by creating a configuration file that defines where your images are stored, how many object classes you have, and the names of those classes.
 
Train the model using pretrained weights so the network can build on previously learned visual features. During training, the system learns to draw bounding boxes, classify objects, and estimate detection confidence. Monitor metrics such as loss, precision, recall, and mean Average Precision to understand how performance improves over time.
 
When training is complete, evaluate the model on images it has never seen. Study incorrect detections, missed objects, and inaccurate bounding boxes to understand the model’s weaknesses. Finally, run your trained detector on a webcam or video feed and observe real-time predictions. This demonstrates the speed advantage of YOLO, originally introduced by Joseph Redmon, where detection happens in a single pass through the network.
 
Document your group’s work by describing how you collected your dataset, showing example labeled images, reporting training results, and reflecting on how well your detector performs in real scenarios.


**Dataset Collection:**
Images to be collected for the following
       a. Red cups
       b. Blue bottles
       c. Phones

We used Wiki media (https://commons.wikimedia.org/wiki/Category:Images) to download images for the above 3 classes. We downloaded them to our local machines and uploaded each of our images to a shared google drive to gather all images in one place.

We then used Roboflow (https://roboflow.com) to label these images as Red cups, Blue bottles and phones by using the Annotate feature. The annotated images were put in the Train dataset and those images without relevant objects were put into test dataset.