# Futsal Player Detector for BiH Premier Futsal League

## Project Overview

This project aims to develop a computer vision application capable of detecting and tracking futsal players in video footage from the BiH Premier Futsal League. The primary goal is to provide a tool that can analyze match videos and automatically identify player positions, which can be useful for tactical analysis, performance review, or generating automated highlights.

## Current Status

As of now, the core focus has been on the foundational machine learning components:
1.  **Dataset Creation:** A custom dataset of futsal images has been meticulously annotated to train the object detection model.
2.  **Initial Model Training:** A preliminary object detection model has been trained on this dataset, demonstrating promising initial results for player detection.

The next phase will involve developing the user-friendly application interface that allows video uploads and displays the tracked output.

## Dataset

The custom dataset used for training this model was created and managed using Roboflow. It consists of [Number] images with annotations for 'player' objects. This dataset is crucial for teaching the model to recognize futsal players in various scenarios, lighting conditions, and player poses.


## Training Details

The initial model training was conducted in a Google Colab environment, leveraging its GPU capabilities for efficient deep learning. The training process involved [briefly mention model architecture, e.g., "fine-tuning a YOLOv9 model"] on the custom futsal player dataset.

* **Google Colab Training Notebook:** [Futsal Player Detector - Initial Training](https://www.google.com/url?sa=E&source=gmail&q=https://colab.research.google.com/drive/1uc1ttOqH3OAx4RXGrnaJeNoHrwgvKRPN?usp=sharing)
    

## Future Work (Application Development)

The subsequent steps for this project include:
* Developing a user interface (UI) to allow users to upload futsal match videos.
* Integrating the trained object detection model to process the uploaded videos.
* Generating an output video with bounding boxes and tracking IDs around detected players.
* Potentially implementing additional features like player counting or basic movement analysis.

## Technologies Used (So far)

* **Python**
* **YOLOv9**
* **Roboflow** (For dataset management and annotation)
* **Google Colab** (For training environment)

## Getting Started (for future development/contribution)

_This section will be expanded once the application development begins._

1.  Clone this repository:
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    ( `requirements.txt` file will be created later with all project dependencies)

## Contact

Ali Ljaljak - aljaljak2@etf.unsa.ba

---