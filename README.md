
# Action Detection for ASL Signs  

This project focuses on action detection for American Sign Language (ASL) signs using computer vision and deep learning techniques.
It includes data preprocessing, a robust detection pipeline, and a model for gesture recognition.  

## Features  
- **Video Preprocessing**: Converts videos into frames for model input.  
- **Action Detection Model**: Trained using a deep learning pipeline to recognize ASL gestures.  
- **Visualization**: Displays predictions and overlays results on the video.  
- **Customizable**: Works with any labeled ASL dataset.  

## Getting Started  

### Prerequisites  
Ensure the following are installed on your system:  
- **Python**: Version 3.8 or above  
- **GPU Support**: (Optional but recommended) NVIDIA RTX 3060 Ti or similar for faster training/inference.  

Install the required Python libraries:  
```bash  
pip install -r requirements.txt  
```  

### Dataset Preparation  
1. Collect ASL sign language videos.  
2. Preprocess videos into frames at 244x244 resolution and organize them by class folders.  
3. Example structure:  
   ```  
   dataset/  
   ├── sign_hello/  
   │   ├── frame1.jpg  
   │   ├── frame2.jpg  
   ├── sign_thank_you/  
   │   ├── frame1.jpg  
   │   ├── frame2.jpg  
   ```  

### How to Run  
1. Clone this repository and navigate to its directory:  
   ```bash  
   git clone <repo_url>  
   cd <repo_folder>  
   ```  

2. Launch the Jupyter Notebook to preprocess the dataset, train, or evaluate the model:  
   ```bash  
   jupyter notebook Updated_Action_Detection.ipynb  
   ```  

3. Follow the step-by-step code sections within the notebook to:  
   - Preprocess and load data.  
   - Train or fine-tune the model.  
   - Run inference and visualize predictions.  

### Example Code Snippets  

#### Model Training
```python
# Load the preprocessed data
train_loader, val_loader = load_data("path_to_preprocessed_frames")

# Define the model
model = ASLActionDetectionModel(input_shape=(244, 244, 3), num_classes=NUM_CLASSES)

# Train the model
history = model.fit(train_loader, validation_data=val_loader, epochs=20)

# Save the model
model.save("asl_action_model.h5")
```

#### Inference
```python
# Load trained model
from tensorflow.keras.models import load_model
model = load_model("asl_action_model.h5")

# Predict on a single frame
frame = preprocess_frame("path_to_frame.jpg")  # Resize and normalize
prediction = model.predict(frame)
print("Predicted sign:", decode_prediction(prediction))
```

#### Visualization
```python
# Visualize results
import cv2
from matplotlib import pyplot as plt

frame = cv2.imread("path_to_frame.jpg")
result = model.predict(preprocess_frame(frame))

plt.imshow(frame)
plt.title(f"Predicted Sign: {decode_prediction(result)}")
plt.show()
```

---

## Outputs  
- **Metrics**: Evaluation metrics like accuracy, precision, recall, and F1-score.  
- **Predictions**: Predicted ASL sign labels for input frames/videos.  
- **Visualizations**: Graphs of training/validation performance and annotated video frames.  

---

## Contributing  
Contributions are welcome!  
1. Fork the repository.  
2. Create a feature branch: `git checkout -b feature-name`.  
3. Commit your changes: `git commit -m "Add feature description"`.  
4. Push the branch: `git push origin feature-name`.  
5. Open a pull request.  

---

Let me know if this works, or if you'd like more changes! 😊
