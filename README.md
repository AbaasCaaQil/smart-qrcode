# smart-qrcode
A simple project for generating and scanning QR codes, utilizing popular libraries for efficient creation and reading of QR data.

# QR Code Generator

This Python script allows users to create QR codes from any input text and save them as images.

## Features
- Allows users to enter data and save it to a file.
- Generates a QR code from the stored data.
- Saves the QR code as an image (.jpg or .png).
- Handles errors gracefully.
- Supports multiple QR code generations in one session.

## Requirements
- Python 3.x
- qrcode library (install using pip install qrcode[pil])

## How to Run
1. Clone the repository:

git clone https://github.com/AbaasCaaQil/qr-code-generator.git

2. Navigate into the project folder:

cd qr-code-generator

3. Run the script:

python qrcode_generator.py

## Example Usage

Enter the file name: my_data.txt
Enter the data to store: Hello, World!
Enter the QR code file name (with .jpg or .png): my_qr.jpg
QR code created successfully as my_qr.jpg
Do you want to create another QR code? (Y/n): n
