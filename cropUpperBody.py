import os
import cv2

# Define the input directory and the output directory
input_dir = r'D:\finalProject\vidsToFrames'  # Directory with original images
output_dir = r'D:\finalProject\resized'      # Directory to save resized images

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the new size (width, height)
new_size = (244, 244)  # Adjust the size as needed

# Traverse the input directory
for root, dirs, files in os.walk(input_dir):
    for filename in files:
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Check for image file types
            # Construct the full input file path
            img_path = os.path.join(root, filename)
            
            # Read the image
            img = cv2.imread(img_path)
            
            if img is not None:
                # Resize the image
                resized_img = cv2.resize(img, new_size)
                
                # Determine the relative path to create the same structure in the output directory
                relative_path = os.path.relpath(root, input_dir)
                output_folder = os.path.join(output_dir, relative_path)
                
                # Create the output folder if it doesn't exist
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                
                # Construct the output path
                output_path = os.path.join(output_folder, filename)
                
                # Save the resized image
                cv2.imwrite(output_path, resized_img)
                print(f'Resized image saved: {output_path}')
            else:
                print(f'Error loading image: {img_path}')
