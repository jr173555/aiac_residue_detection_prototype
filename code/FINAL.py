from ultralytics import YOLO
import serial
import time
import sys

# Load YOLO model
model = YOLO("C:/1206_aac_train/dataset/runs/detect/train5/weights/best.pt")

results = model.predict(source="0", stream=True, show = True)
arduino = serial.Serial('COM3', 9600)

# for each frame
for result in results:
  class_ids = result.boxes.cls.tolist()
  detected_labels = [result.names[int(i)] for i in class_ids]
  print("Detected:", detected_labels)
  #['person', 'person', 'cat']
  #(if 2 person, 1 cat detected in a frame)
  label_commands = {
      'aac': 'G', 'nail': 'R', 'wood': 'Y', 'aac_nail_wood': 'A', 'none': '0'
  }

  if 'aac' in detected_labels and not 'nail' in detected_labels and not 'wood' in detected_labels:
    command = label_commands['aac']
  elif 'nail' in detected_labels and 'wood' in detected_labels:
    command = label_commands['aac_nail_wood']
  elif 'nail' in detected_labels:
    command = label_commands['nail']
  elif 'wood' in detected_labels:
    command = label_commands['wood']
  else:
    command = label_commands['none']

  print(f"Detected Labels: {detected_labels}")
  print(f"Sending command to Arduino: {command}")

  arduino.write(command.encode())


time.sleep(2)  # Wait for Arduino to initialize