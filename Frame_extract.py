import cv2
import os

# Paths and parameters
video_dir = "downloads"  # Directory with all ASL videos
output_dir = "vidsToFrames"      # Directory to save frames
frames_per_second = 5              # Adjust based on your needs

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to extract frames
def extract_frames(video_path, frames_per_second=5):
    # Get the video's label (name without extension)
    label = os.path.splitext(os.path.basename(video_path))[0]
    
    # Create a directory for each video using its label
    label_dir = os.path.join(output_dir, label)
    if not os.path.exists(label_dir):
        os.makedirs(label_dir)

    cap = cv2.VideoCapture(video_path)
    frame_rate = cap.get(cv2.CAP_PROP_FPS)  # Get the video's FPS
    interval = int(frame_rate / frames_per_second)  # Frame capture interval

    frame_count = 0
    extracted_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Save frame at intervals
        if frame_count % interval == 0:
            frame_filename = os.path.join(label_dir, f"{extracted_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            extracted_count += 1

        frame_count += 1

    cap.release()

# Process all videos
for video_file in os.listdir(video_dir):
    video_path = os.path.join(video_dir, video_file)
    extract_frames(video_path, frames_per_second)
