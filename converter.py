from PIL import Image
import os

def convert_jpg_to_png(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            # Open the .jpg file
            img = Image.open(os.path.join(input_folder, filename))
            # Convert the image to .png
            png_filename = os.path.splitext(filename)[0] + '.png'
            img.save(os.path.join(output_folder, png_filename))
            print(f"Converted {filename} to {png_filename}")

# Example usage
input_folder = 'JPEG files'
output_folder = 'PNG files'
convert_jpg_to_png(input_folder, output_folder)
