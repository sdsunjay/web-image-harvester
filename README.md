
# Image Download Toolkit

This repository contains a set of tools designed to extract image URLs from HAR files and subsequently download these images from the web. It is perfect for projects where you need to automate the collection of image data from various websites.

## Features

- **Extract URLs**: Parses HAR files to extract image URLs based on specific filtering criteria, organizing them based on time.
- **Download Images**: Downloads images from extracted URLs and saves them locally, organizing them based on download time.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

```bash
python -m pip install requests
```

### Installing

A step-by-step series of examples that tell you how to get a development env running:

1. Clone the repository:
```bash
git clone https://github.com/sdsunjay/web-image-harvester.git
```

2. Navigate to the cloned directory:
```bash
cd web-image-harvester
```

3. Install necessary Python packages:
```bash
pip install -r requirements.txt
```

### Usage

#### Extracting URLs from HAR files

* Obtain your har files
* Put them in a directory of your choosing
* Edit constants.py with the dir locations
* Run the `extract_urls_from_har.py` script

```bash
python extract_urls_from_har.py
```

#### Downloading Images

After extracting URLs, you can download images by running `image_downloader.py`:

```bash
python image_downloader.py
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

- **Sunjay Dhama** - *Initial work* - [sdsunjay](https://github.com/sdsunjay)

See also the list of [contributors](https://github.com/sdsunjay/web-image-harvester/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc
