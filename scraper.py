import os
import requests
from bs4 import BeautifulSoup

def download_video(full_url, save_path):
    print("Attempting to download from URL:", full_url)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    response = requests.get(full_url, headers=headers, stream=True)
    
    if response.status_code == 200:
        with open(save_path, 'wb') as video_file:
            for chunk in response.iter_content(chunk_size=8192):
                video_file.write(chunk)
        print(f"Video downloaded successfully and saved as '{save_path}'")
    else:
        print(f"Failed to download video. Status code: {response.status_code}")

def fetch_and_download_videos(base_url, start_page, end_page):
    for page_num in range(start_page, end_page + 1):
        page_url = f"{base_url}{page_num}/"
        print(f"Fetching page: {page_url}")
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
        }
        
        # Fetch the page HTML
        page_response = requests.get(page_url, headers=headers)
        if page_response.status_code == 404:
            print(f"Page {page_url} does not exist. Skipping.")
            continue  # Skip to the next page if it returns 404
        elif page_response.status_code != 200:
            print(f"Failed to retrieve page {page_num}. Status code: {page_response.status_code}")
            continue
        
        # Parse the HTML to find the video src
        soup = BeautifulSoup(page_response.content, "html.parser")
        video_tag = soup.find("video", class_="v-asl")
        
        # Check different potential video src locations
        video_src = None
        if video_tag and video_tag.get("src"):
            video_src = video_tag["src"]
        elif video_tag:
            # Try finding src in a <source> tag within <video>
            source_tag = video_tag.find("source")
            if source_tag and source_tag.get("src"):
                video_src = source_tag["src"]
        
        if video_src:
            # Adjust the URL based on the extracted src
            # Check for relative paths and build the correct URL
            if video_src.startswith('/'):
                full_video_url = f"https://www.handspeak.com{video_src}"  # Prefix with the base URL
            else:
                full_video_url = video_src  # It's already a full URL
            
            print(f"Found video source: {video_src}")  # Debugging line
            print(f"Constructed video URL: {full_video_url}")  # Debugging line
            
            video_filename = video_src.split("/")[-1]
            save_path = os.path.join("downloads", video_filename)
            
            # Download the video
            download_video(full_video_url, save_path)
        else:
            print(f"No video found on page {page_url} with expected structures.")

# Set parameters
base_url = "https://www.handspeak.com/word/"
start_page = 301  # Starting page number
end_page = 12000  # Ending page number

# Run the download function
fetch_and_download_videos(base_url, start_page, end_page)
