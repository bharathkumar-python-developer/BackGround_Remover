from PIL import Image
import numpy as np
import os

def remove_background_and_set_new(image_path, new_background_color):

    if not os.path.isfile(image_path):
        print(f"Error: File '{image_path}' does not exist.")
        return

    image = Image.open(image_path)
    image = image.convert('RGBA')
    image_data = np.array(image)
    threshold = 100
    mask = np.where((image_data[:, :, 0] > threshold) & 
                    (image_data[:, :, 1] > threshold) & 
                    (image_data[:, :, 2] > threshold),
                    0, 255)
    image_data[:, :, 3] = mask
    background_image = Image.new('RGBA', image.size, new_background_color)
    background_image.paste(image, mask=Image.fromarray(image_data[:, :, 3]))
    background_image.show()
    background_image.save('Edited_Photo.jpg')
image_path = input("Enter the image path: ")

if not image_path.endswith(('.jpg', '.png', '.jpeg')):
    image_path += '.jpg'

red = int(input("Enter the red value (0-255): "))
green = int(input("Enter the green value (0-255): "))
blue = int(input("Enter the blue value (0-255): "))

new_background_color = (red, green, blue)

remove_background_and_set_new(image_path, new_background_color)