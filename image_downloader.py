import requests
import os
from datetime import datetime
from time import sleep
from random import randint

from constants import CONSTANTS

def create_directory():
    now = datetime.now()
    directory_name = now.strftime("%Y%m%d_%H%M%S")
    path = os.path.join(CONSTANTS['images_output_dir'], directory_name)
    os.makedirs(path, exist_ok=True)
    return path

def download_image(index, url, download_dir):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP request errors

        file_path = os.path.join(download_dir, f"{index}.webp")
        with open(file_path, 'wb') as out_file:
            for chunk in response.iter_content(chunk_size=8192):
                out_file.write(chunk)
        if index % 100 == 0:
            print(f"Downloaded: {index}.webp")
        return True

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return False

def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def is_size_small(size_str):
    try:
        size_part = size_str.split("size=")[1].split("&")[0]
        width, height = map(int, size_part.split('x'))
        return width <= 150 and height <= 150
    except Exception:
        return False

def read_latest_file(directory):
    # Construct the path to the directory
    full_path = os.path.join('.', directory)

    # List all files in the directory
    files = [f for f in os.listdir(full_path) if f.endswith('_all_image_urls.txt')]

    # Check if there are any files
    if not files:
        print("No files found in the directory.")
        return None

    # Sort files based on the timestamp in the filename
    files.sort(key=lambda x: datetime.strptime(x, '%y_%m_%d_%H_%M_all_image_urls.txt'))

    # Get the latest file
    latest_file = files[-1]
    latest_file_path = os.path.join(full_path, latest_file)
    print(f"Reading from {latest_file}")
    return latest_file_path

def main():
    latest_file_path = read_latest_file(CONSTANTS['image_urls_dir'])
    image_urls = read_urls_from_file(latest_file_path)
    urls_ending_in_zero = [v for v in image_urls if v.endswith('0')]
    filtered_urls = [url for url in urls_ending_in_zero if not is_size_small(url)]

    print(f"Total Number of Images To Download: {len(filtered_urls)}")
    download_dir = create_directory()  # Create a directory for downloads
    return
    count = 0
    fail_count = 0

    for index, url in enumerate(filtered_urls, start=1):
        if download_image(count, url, download_dir):
            count += 1
            if count % 50 == 0:
                print(f"Sleeping\nPic number: {count}")
                sleep(randint(3, 5))
        else:
            fail_count += 1
    print(f"Total Number of Images Downloaded: {count}")
    print(f"Number of Failed Downloads: {fail_count}")
if __name__ == "__main__":
    main()

