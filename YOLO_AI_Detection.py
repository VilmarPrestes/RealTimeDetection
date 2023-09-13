#do a "pip install ultralytics" first

from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model.predict(source = "0", show = True)
print(results)