# Image File Converter

I'm tired of using random file conversion websites.

This is a small terminal image utility built with Python and [Pillow](https://python-pillow.org/). The program can convert any amount of images between common formats, alongside a few miscellaneous effects.

## Features

- Convert images to different file formats
- Convert images to 128x128 thumbnails
- Apply a pixel jumble effect
- Apply a Gaussian blur

## Requirements

- Python 3.9 or newer
- Pillow

## Setup

Create and activate a virtual environment, then install Pillow:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install Pillow
```

If PowerShell prevents script activation, run the commands from an activated environment or use:

```powershell
.\.venv\Scripts\python.exe -m pip install Pillow
```

## Usage

Run the script with a mode followed by one or more input image paths:

```text
python fileconvert.py <mode> <image1> <image2> ...
```

For example:

```powershell
python fileconvert.py png image1.jpg
python fileconvert.py pdf image1.jpg image2.png
python fileconvert.py thumbnail image1.jpg
python fileconvert.py blur image1.jpg
```

The script prints the output path after each successful operation. Generated files are saved in `out\`:

```text
puppy.jpg       -> out\puppy.png
puppy.jpg       -> out\puppy_thumbnail.jpg
puppy.jpg       -> out\puppy_blur.jpg
```

## Available modes

| Mode | Result |
| --- | --- |
| `png` | Convert to PNG |
| `jpg` | Convert to JPEG |
| `webp` | Convert to WEBP |
| `pdf` | Convert to PDF |
| `gif` | Convert to GIF |
| `bmp` | Convert to Bitmap |
| `thumbnail` | Create a 128 × 128 pixel thumbail |
| `jumble` | Apply a randomized pixel-spread effect |
| `blur` | Apply a Gaussian blur |

To display the usage message, run the script without enough arguments:

```powershell
python fileconvert.py
```