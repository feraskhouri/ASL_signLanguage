import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define parameters
image_height = 224  # Set your target image height
image_width = 224   # Set your target image width
batch_size = 32     # Define the batch size
train_data_dir = 'resized'  # Path to your training data directory
output_file = 'output_log.txt'  # Output log file

# Create or clear the output log file
with open(output_file, 'w') as f:
    f.write("Dataset Summary:\n\n")

    # Check how many images are in each class directory
    for class_name in os.listdir(train_data_dir):
        class_path = os.path.join(train_data_dir, class_name)
        if os.path.isdir(class_path):
            num_images = len(os.listdir(class_path))
            f.write(f"{class_name}: {num_images} images\n")

# Create the ImageDataGenerator for normalization
datagen = ImageDataGenerator(rescale=1.0/127.5,  # Normalize to [-1, 1]
                             shear_range=0.2,
                             zoom_range=0.2,
                             horizontal_flip=True)

# Create a generator for the training data
train_generator = datagen.flow_from_directory(
    train_data_dir,
    target_size=(image_height, image_width),
    batch_size=batch_size,
    class_mode='categorical'  # or 'binary', based on your task
)

# Write the class indices to the output log file
with open(output_file, 'a') as f:  # Append to the existing log file
    f.write("\nClass indices:\n")
    for class_name, class_index in train_generator.class_indices.items():
        f.write(f"{class_name}: {class_index}\n")
