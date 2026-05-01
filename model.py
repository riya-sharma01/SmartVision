import torch
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification

# Load pretrained deepfake model
model_name = "dima806/deepfake_vs_real_image_detection"

processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)

model.eval()

def predict(image_path):
    image = Image.open(image_path).convert("RGB")

    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probs = torch.nn.functional.softmax(logits, dim=1)

        confidence, pred = torch.max(probs, dim=1)

    label_map = {0: "Real", 1: "Fake"}# model-specific
    label = label_map[pred.item()]
    confidence = confidence.item() * 100

    return label, round(confidence, 2)