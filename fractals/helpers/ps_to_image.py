"""
Helper functions to convert .eps to .png, .gif, and .pdf
"""

from PIL import Image
from typing import Callable
import os
import glob
import shutil
from pathlib import Path
import turtle
from pdf2image import convert_from_path

BASE_FOLDER = os.path.dirname(os.path.realpath(__file__))
PARENT_FOLDER = os.path.dirname(BASE_FOLDER)
POSTSCRIPT_FOLDER = f"{PARENT_FOLDER}/postscripts"
IMAGE_FOLDER = f"{PARENT_FOLDER}/images"
TEMP_FOLDER = f"{BASE_FOLDER}/pleaseignorethistempfolder"
PS_EXT = ".eps"
PDF_EXT = ".pdf"
PNG_EXT = ".png"
FPS = 12

def convert_ps_to_png(ps_file : str) -> str:
    """uses PIL Image library to convert postscript to png"""

    assert ps_file.endswith(PS_EXT), \
        f"{ps_file} does not have {PS_EXT} extension"

    output_file = ps_file.replace(PS_EXT, PNG_EXT)
    img = Image.open(ps_file)
    img.save(output_file)

    return output_file

def convert_ps_to_pdf(ps_file : str) -> str:
    """uses os.system to convert ps file to PDF"""

    assert ps_file.endswith(PS_EXT), \
        f"{ps_file} does not have {PS_EXT} extension"

    os.chdir(os.path.dirname(ps_file))
    base_name = os.path.basename(ps_file)
    os.system(f"ps2pdf {base_name}")

    return ps_file.replace(PS_EXT, PDF_EXT)

def cleanup_folder(folder : str, ext : str = PS_EXT) -> list:
    """
    adds the extension to all files with no extension
    also ignores all other files
    returns list of filenames with extension
    """

    # I really wanted to do something weird and hacky with
    # list comprehensions and boolean operation abuse.
    # but I decided against it.
    files = []
    for file_name in os.listdir(folder):
        name_no_ext, temp_ext = os.path.splitext(file_name)
        if temp_ext not in {"", ext} or \
           os.path.isdir(f"{folder}/{file_name}"):
            continue

        current_file = f"{folder}/{name_no_ext}{ext}"
        os.rename(f"{folder}/{file_name}", current_file)
        files.append(current_file)

    return files

def generate_image_list(folder : str, ext = PS_EXT) -> list:
    """
    returns list of PIL Image objects from image files
    sorts images by name
    """

    # edge case, requires extra library
    if ext == PDF_EXT:
        imagelist = [convert_from_path(file_name)[0] for file_name in 
                sorted(cleanup_folder(folder, ext = ext))]
        imagelist[-1].show()
        return imagelist

    return [Image.open(file_name) for file_name in 
            sorted(cleanup_folder(folder, ext = ext))]



def make_gif(draw : Callable, name : str, out_file : str):
    """
    combines images in postscript folder as frames of gif
    assumes images are sorted
    """

    Path(TEMP_FOLDER).mkdir(parents = True, exist_ok = False)
    drawing_is_running = True

    def save(interval : int, folder : str, index : int):
        """saves turtle screen every interval as postscript file to folder"""
        if drawing_is_running:
            turtle.getcanvas().postscript(file = "{0}/{1}{2:04d}{3}".format(folder, name, index, PS_EXT))
            index += 1
            turtle.ontimer(lambda: save(interval, folder, index), interval)

    interval = int(1000 / FPS)
    turtle.ontimer(lambda: save(interval, TEMP_FOLDER, 0), interval)
    draw()
    drawing_is_running = False

    convert_all_ps(TEMP_FOLDER, TEMP_FOLDER, filetype = "PDF")
    print("if it got here, we didn't heck it up")

    images = generate_image_list(TEMP_FOLDER, ext = PDF_EXT)
    images[0].save(out_file, 
                   save_all = True, 
                   append_images = images[1:], 
                   loop = 0,
                   duration = interval)

    shutil.rmtree(TEMP_FOLDER)

CONVERSION_FUNCTIONS = {
    "pdf": convert_ps_to_pdf,
    "png": convert_ps_to_png,
}

def convert_all_ps(postscript_folder : str, image_folder : str, 
                   filetype : str = "png"):
    """
    loops through all files in postscripts folder and converts them
    """

    filetype = filetype.lower()

    assert filetype in CONVERSION_FUNCTIONS.keys(), \
        f"{filetype} not accepted filetype"

    convert_ps = CONVERSION_FUNCTIONS[filetype]

    image_paths = [convert_ps(ps_file) for ps_file in 
                   cleanup_folder(postscript_folder)]

    Path(image_folder).mkdir(parents = False, exist_ok = True)

    for file_path in image_paths:
        new_path = image_folder + "/" + os.path.basename(file_path)
        shutil.move(file_path, new_path)


if __name__ == "__main__":
    convert_all_ps(POSTSCRIPT_FOLDER, IMAGE_FOLDER)
    convert_all_ps(POSTSCRIPT_FOLDER, IMAGE_FOLDER, filetype = "pdf")