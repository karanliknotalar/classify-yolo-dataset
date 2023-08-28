import glob
import math
import shutil
from os import path, makedirs, system, remove
from sys import platform

from PIL import Image

import optionss as ops

VERTICAL = "vertical"
HORIZONTAL = "horizontal"


def clear_cmd():
    if platform == "win32":
        system("cls")
    else:
        system("clear")


def flip_label(label, flip):
    class_id, x_center, y_center, width, height = map(float, label.split())

    if flip == VERTICAL:
        x_center = 1.0 - x_center

    if flip == HORIZONTAL:
        y_center = 1.0 - y_center

    return f"{int(class_id)} {x_center} {y_center} {width} {height}"


def augment_dataset(file_name, flip):
    output_img_dir = path.join("augmented_dataset", "images")
    output_txt_dir = path.join("augmented_dataset", "labels")

    # If not exists, we create the output folders.
    makedirs(output_img_dir) if not path.exists(output_img_dir) else ""
    makedirs(output_txt_dir) if not path.exists(output_txt_dir) else ""

    # we get image and label file path.
    image_path = glob.glob(rf"{ops.IMG_FILES_DIR}/{file_name}.*")[0]
    txt_path = glob.glob(rf"{ops.LABEL_FILES_DIR}/{file_name}.*")[0]

    # flip and save the image.
    image = Image.open(image_path)
    flipped_img = image.transpose(Image.FLIP_TOP_BOTTOM if flip == HORIZONTAL else Image.FLIP_LEFT_RIGHT)
    flipped_img.save(path.join(output_img_dir, file_name + "_" + flip + path.splitext(path.basename(image_path))[1]))
    image.close()
    flipped_img.close()

    # If there is a file with the same name,
    # it should delete the remaining file from the previous operation to recreate it.
    if path.exists(path.join(output_txt_dir, file_name + "_" + flip + ".txt")):
        remove(path.join(output_txt_dir, file_name + "_" + flip + ".txt"))

    # We are reading the lines in the label file.
    lines_in_txt = open(txt_path) if path.exists(txt_path) else []

    # by looping the read lines in order, we make the direction calculation and save it.
    for line in lines_in_txt:
        flipped_label = flip_label(line, flip)
        with open(path.join(output_txt_dir, file_name + "_" + flip + ".txt"), mode="a+") as f:
            f.write(flipped_label + "\n")

    # We also include the original files.
    shutil.copy(image_path, path.join(output_img_dir, file_name + path.splitext(path.basename(image_path))[1]))
    shutil.copy(txt_path, path.join(output_txt_dir, file_name + ".txt"))


def start_process(flip):
    print(f"\nProcessing... ({flip})")
    # we get the filename from the label file.
    # already both the label file and the image file have the same name
    label_list = glob.glob(rf"{ops.LABEL_FILES_DIR}/*.txt")
    total_item_count = len(label_list)
    counter = 0
    for txt_file in label_list:
        counter += 1
        print(f"\rCompleted ({flip}): {counter}/{total_item_count} | "
              f"{math.ceil((counter / total_item_count) * 100)}%",
              end="")
        file_name, ext = path.splitext(path.basename(txt_file))
        augment_dataset(file_name, flip)

    input(f"\nProcess Done: {flip}. Press any key for continue...")


def start_app():
    clear_cmd()
    while True:
        print(" Menu ".center(50, "#"))
        print("")
        print("1 - Augment VERTICAL")
        print("2 - Augment HORIZONTAL")
        print("3 - Augment VERTICAL AND HORIZONTAL")
        print("0 - Exit")
        print("")

        input_opt = input("Select: ")

        if input_opt.isnumeric():
            if input_opt == "1":
                start_process(VERTICAL)
            if input_opt == "2":
                start_process(HORIZONTAL)
            if input_opt == "3":
                start_process(VERTICAL)
                start_process(HORIZONTAL)
            if input_opt == "0":
                break
        else:
            clear_cmd()


start_app()
