## Graphics Conversion Tool
The aim of this project is to create a simple script that converts pencil drawings into solid line drawings with transparent background.
WIP
The first version can convert an rgb into Notan picture. 

## Installation (Windows)
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

## Usage Example
python reduce_colors.py img_0.jpg
    this will create 3 png fies:
    1. Picture converted to grayscale
    2. Picture converted to Notan
    3. Picture with applied erosion
