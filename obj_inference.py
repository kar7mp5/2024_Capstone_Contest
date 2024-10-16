# obj_inference.py
import roboflow
from roboflow import Roboflow
roboflow.login()

import random


def get_obj_inference(API_KEY, image_path):
    """Get object inference result
    
    Args:
        API_KEY (str): Roboflow API KEY
        image_path (str): inference target image path

    Returns:
        prediction (list[dict]): object inference results
    """
    # Initialize Roboflow with API key
    rf = Roboflow(api_key=API_KEY)
    project = rf.workspace().project("bottle-cap-nbpv9")
    dataset = project.version(1).download("yolov8")

    # Load the YOLOv8 model from the local directory
    model = project.version(dataset.version).model

    # Select a test image
    random_test_image = random.choice(os.listdir(image_path))
    print("Running inference on " + random_test_image)

    # Execute prediction
    pred = model.predict(os.path.join(image_path, random_test_image))
    print(pred)

    # Visualize prediction results
    # Save the results as an image
    output_image_path = 'output_image.png'
    pred.save(output_image_path)

    # Print the path to the saved image
    print(f"Image saved to: {output_image_path}")




if __name__=="__main__":
    from  dotenv import load_dotenv
    import os

    load_dotenv()
    API_KEY = os.environ.get("ROBOFLOW_KEY")

    get_obj_inference(API_KEY, "test_image")
