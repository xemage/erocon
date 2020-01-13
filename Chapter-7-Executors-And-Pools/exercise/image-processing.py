from concurrent.futures import ProcessPoolExecutor
from PIL import Image
import fnmatch
import os
import pathlib

def get_png_files(folder):
    files = []
    for file in os.listdir(folder):
        if fnmatch.fnmatch(file, '*.png'):
            files.append(os.path.join(folder, file))
    return files

def to_black_and_white(file_path):
    
    print("Process {} will try to convert image {}".format(os.getpid(), file_path))

    p = pathlib.Path(file_path)
    old_folder = p.parents[0]
    print("Process {} - old path {}".format(os.getpid(), old_folder))
    
    old_suffix = p.suffix
    print("Process {} - old suffix {}".format(os.getpid(), old_suffix))

    old_file_name = p.stem
    print("Process {} - old file name {}".format(os.getpid(), old_file_name))
    new_file_name = "{}-converted{}".format(old_file_name, old_suffix)
    print("Process {} - new file name {}".format(os.getpid(), new_file_name))

    new_file_path = pathlib.Path(old_folder, new_file_name)
    print("Process {} - new file path {}".format(os.getpid(), new_file_name))

    image_file = Image.open(file_path) # open colour image
    image_file = image_file.convert('1') # convert image to black and white
    image_file.save(new_file_path)
    

def main():
    input_folder = pathlib.Path("./temp/input").resolve()

    image_files = get_png_files(input_folder)

    print("Starting ProcessPoolExecutor")
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        future = executor.map(to_black_and_white, image_files)

    print("All images converted.")


if __name__ == "__main__":
    main()