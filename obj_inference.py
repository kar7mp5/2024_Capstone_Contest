# obj_inference.py
import roboflow
from roboflow import Roboflow
roboflow.login()

from  dotenv import load_dotenv
import os

import random


load_dotenv()
API_KEY = os.environ.get("ROBOFLOW_KEY")

# Initialize Roboflow with API key
rf = Roboflow(api_key=API_KEY)
project = rf.workspace().project("bottle-cap-nbpv9")
dataset = project.version(1).download("yolov8")


# Load the YOLOv8 model from the local directory
model = project.version(dataset.version).model

# Select a test image
test_set_loc = 'test_img/'  # Path where test images are located
random_test_image = random.choice(os.listdir(test_set_loc))
print("Running inference on " + random_test_image)

# Execute prediction
pred = model.predict(os.path.join(test_set_loc, random_test_image))
print(pred)

# Visualize prediction results
# Save the results as an image
output_image_path = 'output_image.png'
pred.save(output_image_path)

# Print the path to the saved image
print(f"Image saved to: {output_image_path}")
