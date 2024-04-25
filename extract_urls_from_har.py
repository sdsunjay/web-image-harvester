import os
import datetime
import json

from constants import CONSTANTS

def extract_urls_from_har(har_path, unwanted_extensions):
    """ Extract and filter URLs from a HAR file based on unwanted extensions. """
    image_urls = set()
    try:
        with open(har_path, 'r') as file:
            har_data = json.load(file)
        for entry in har_data['log']['entries']:
            url = entry['request']['url']
            if url.startswith(CONSTANTS["url_prefix"]) and not any(url.endswith(ext) for ext in unwanted_extensions):
                image_urls.add(url)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error processing file {har_path}: {str(e)}")
    return image_urls

def process_har_files(directory):
    """ Process all HAR files in the specified directory to extract image URLs. """
    all_image_urls = set()
    har_files = [f for f in os.listdir(directory) if f.endswith('.har')]
    for har_file in har_files:
        har_path = os.path.join(directory, har_file)
        print(f"Reading from {har_path}")
        urls = extract_urls_from_har(har_path, CONSTANTS["unwanted_extensions"])
        all_image_urls.update(urls)
    return all_image_urls

def save_urls_to_file(image_urls, file_path):
    """ Save all collected image URLs to a file. """
    try:
        with open(file_path, "w") as file:
            for image_url in image_urls:
                file.write(f"{image_url}\n")
    except IOError as e:
        print(f"Error writing to file {file_path}: {str(e)}")


def main():
    all_image_urls = process_har_files(CONSTANTS["har_directory"])
    now = datetime.datetime.now()
    current_time_string = now.strftime("%y_%m_%d_%H_%M")
    filename = f"./{CONSTANTS['image_urls_dir']}/{current_time_string}_{CONSTANTS['output_file_path']}"
    print(f"Writing to {filename}")
    save_urls_to_file(all_image_urls, filename)

if __name__ == "__main__":
    main()
