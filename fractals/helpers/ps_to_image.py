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

def cleanup_postscript_folder(postscript_folder : str) -> list:
    """
    adds the postscript extension to all files with no extension
    also ignores all other files
    returns list of filenames with postscript extension
    """

    # I really wanted to do something weird and hacky with
    # list comprehensions and boolean operation abuse.
    # but I decided against it.
    ps_files = []
    for file_name in os.listdir(postscript_folder):
        name_no_ext, ext = os.path.splitext(file_name)
        if ext not in {"", PS_EXT}:
            continue

        ps_file = f"{postscript_folder}/{name_no_ext}{PS_EXT}"
        os.rename(f"{postscript_folder}/{file_name}", ps_file)
        ps_files.append(ps_file)

    return ps_files

def generate_image_list(postscript_folder : str) -> list:
    """
    returns list of PIL Image objects from postscript files
    sorts images by name
    """

    return [Image.open(ps_file) for ps_file in 
            sorted(cleanup_postscript_folder(postscript_folder))]



def make_gif(draw : Callable, name : str, out_file : str) -> Image:
    """
    combines images in postscript folder as frames of gif
    assumes images are sorted
    """

    def save(interval : int, folder : str):
        """saves turtle screen every interval as postscript file to folder"""
        if drawing_is_running:
            turtle.getcanvas().postscript("{0}{1:04d}{2}".format(name, i, PS_EXT))
            i += 1
            turtle.ontimer(lambda: save(interval, folder), interval)

    drawing_is_running = True
    i = 0
    interval = int(1000 / FPS)
    ontimer(lambda: save(interval, TEMP_FOLDER), interval)
    draw()
    drawing_is_running = False

    images = generate_image_list(TEMP_FOLDER)
    images[0].save(out_file, 
                   save_all = True, 
                   append_images = images[1:], 
                   loop = 0)

    shutil.rmtree(TEMP_FOLDER)

CONVERSION_FUNCTIONS = {
    "pdf": convert_ps_to_pdf,
    "png": convert_ps_to_png,
}

def convert_all_ps(postscript_folder : str, image_folder : str, 
                   filetype : str = "png"):
    """loops through all files in postscripts folder and converts them"""

    filetype = filetype.lower()

    assert filetype in CONVERSION_FUNCTIONS.keys(), \
        f"{filetype} not accepted filetype"

    convert_ps = CONVERSION_FUNCTIONS[filetype]

    Path(image_folder).mkdir(parents = False, exist_ok = True)

    image_paths = [convert_ps(ps_file) for ps_file in 
                   cleanup_postscript_folder(postscript_folder)]

    for file_path in image_paths:
        new_path = image_folder + "/" + os.path.basename(file_path)
        shutil.move(file_path, new_path)


if __name__ == "__main__":
    convert_all_ps(POSTSCRIPT_FOLDER, IMAGE_FOLDER)
    convert_all_ps(POSTSCRIPT_FOLDER, IMAGE_FOLDER, filetype = "pdf")