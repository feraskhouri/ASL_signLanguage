import cv2
import numpy as np
import os

# Define parameters
sequence_length = 20  # Desired number of frames per word
frame_size = (244, 244)  # Frame dimensions

def load_all_word_frames(frames_path="path/to/frames"):
    """
    Load frames for all words by iterating through each word folder.

    Parameters:
        frames_path (str): The path where all frames are stored.

    Returns:
        data (dict): Dictionary where keys are word IDs and values are lists of frames.
    """
    data = {}
    
    # Iterate over each folder (each folder represents a word)
    for word_id in os.listdir(frames_path):
        word_folder = os.path.join(frames_path, word_id)
        
        # Check if it is a directory
        if not os.path.isdir(word_folder):
            continue
        
        # Load frames for the current word
        frames = []
        frame_files = sorted([f for f in os.listdir(word_folder) if f.endswith('.jpg') or f.endswith('.png')])
        
        for file_name in frame_files:
            frame_path = os.path.join(word_folder, file_name)
            frame = cv2.imread(frame_path).astype(np.float32)
            frame = cv2.resize(frame, frame_size)
            frame = (frame / 127.5) - 1.0  # Normalize to [-1, 1]
            frames.append(frame)
            
            # Stop if we've reached the sequence length
            if len(frames) == sequence_length:
                break
        
        # Pad if there are fewer frames than the sequence length
        while len(frames) < sequence_length:
            frames.append(np.zeros((frame_size[0], frame_size[1], 3), dtype=np.float32))
        
        # Convert frames to an array and add to the dictionary
        data[word_id] = np.stack(frames)
    
    return data

# Example usage
frames_path = "resized"  # Update this to your actual data path
data = load_all_word_frames(frames_path)
print("Loaded data for words:", len(data))  # Should print the number of folders (words) processed
print("Example word shape:", data[list(data.keys())[0]].shape)  # Shape should be (sequence_length, 244, 244, 3)
