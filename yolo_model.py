import os
import torch
from ultralytics import YOLO
from datetime import datetime
from django.conf import settings


# Load your YOLO model
def load_model(
        model_path=r'best.pt'):
    model = YOLO(model_path)
    return model


# Detect ingredients from an image and save the detected image
def detect_ingredients(image_path, model, output_folder='detected_images'):
    output_folder = os.path.join(settings.MEDIA_ROOT, output_folder)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Perform inference
    results = model(image_path)
    detections = results[0].boxes  # Access the detected boxes

    # Extract ingredient names
    ingredients = []
    if detections is not None:
        for box in detections:
            cls_id = int(box.cls)  # Class index
            cls_name = model.names[cls_id]  # Class name
            ingredients.append(cls_name)

    # Save the detected image
    output_image_name = f'detected_{datetime.now().strftime("%Y%m%d_%H%M%S")}.jpg'
    output_image_path = os.path.join(output_folder, output_image_name)
    results[0].save(output_image_path)

    # Return the path relative to the media root
    return list(set(ingredients)), os.path.join('detected_images', output_image_name)
