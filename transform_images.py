import os
from PIL import Image
import pyheif



def compress_image(input_path:str, output_path:str, width:int=1280,heigth:str=720):
    # Open the image
    image = Image.open(input_path)
    
    # Resize the image while preserving the aspect ratio
    image.thumbnail((width, heigth))
    
    # Compress and save the image with reduced quality
    image.save(output_path, optimize=True, quality=80)  # Adjust the quality value as desired
    
    # Get the file size of the compressed image
    file_size = round((os.path.getsize(output_path) / 1024), 2)  # Size in kilobytes
    print(f"Compressed image saved with file size: {file_size} KB")


def compress_files(path:str):
    imgs = os.listdir(path)
    for img in imgs:
        input_path = os.path.join(path,img)
        output_path = os.path.join(path,img)
        compress_image(input_path,output_path,width=1280,heigth =720)

compress_files('./test_imgs')




def heic_to_png(heic_file:str, png_file:str,path:str):
    heic_path = os.path.join(path, heic_file)
    png_path = os.path.join(path, png_file)
    heif_image = pyheif.read(heic_path)
    image = Image.frombytes(
        heif_image.mode,
        heif_image.size,
        heif_image.data,
        "raw",
        heif_image.mode,
        heif_image.stride,
    )
    image.save(png_path, "PNG")


def get_file(path:str):
    heic_files = os.listdir(path)
    png_files = [os.path.splitext(file)[0] + '.png' for file in heic_files]
    return heic_files, png_files


def transform_HEICPNG(path:str):
    heic_files, png_files = get_file(path)
    for ind, file in enumerate(heic_files):
        heic_to_png(file, png_files[ind],path)




def drop_non_png_files(folder_path:str):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if not filename.endswith('.png'):
            os.remove(file_path)

transform_HEICPNG('./test_imgs')
drop_non_png_files('./test_imgs')
