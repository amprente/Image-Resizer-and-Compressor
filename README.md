GPT
Certainly! Below is a brief documentation for the Python script that provides an interface for resizing and compressing images. This documentation includes an overview, prerequisites, usage instructions, and a description of the functions.

Image Resizer and Compressor Tool
Overview
This tool provides a graphical user interface (GUI) to resize and compress images. Users can choose to resize images by percentage or to specific dimensions. The tool supports saving the output in JPEG, PNG, or WebP formats, with adjustable quality settings for JPEG images.

Prerequisites
Python 3.x
PIL library (Pillow)
Tkinter (usually included with Python)
To install Pillow, run:

bash
Copy code
pip install Pillow
Usage
Start the Application:
Launch the script to open the GUI. This can be done by running the Python script from the terminal or command line.

Select the Input Image:
Click the "Browse" button next to the "Input Path" field to choose the image file you want to resize and compress.

Specify the Output Path:
Click the "Browse" button next to the "Output Path" field to specify where the resized and compressed image should be saved.

Set Resize Options:

Select "Resize by Percentage" and enter a percentage to resize the image accordingly.
Alternatively, select "Resize by Width & Height" and enter the desired dimensions.
Set the Image Quality:
Enter a quality value (1-100) which is applicable when saving in JPEG format.

Resize and Compress:
Click the "Resize and Compress" button to process the image. A message will appear indicating the success of the operation and the details of the output image.

Functions Description
resize_and_compress: Resizes and compresses the image based on selected options, saving it to the specified path. It handles both percentage-based and dimension-based resizing.

open_file_dialog: Opens a file dialog to select the input image file.

save_file_dialog: Opens a file dialog to specify the output file path and filename.

perform_resize: Gathers all input values and calls resize_and_compress with the appropriate parameters, displaying the result in a message box.

This tool is designed to be user-friendly and efficient for typical image processing tasks, suitable for both novice users and experienced individuals looking to quickly resize and compress images.