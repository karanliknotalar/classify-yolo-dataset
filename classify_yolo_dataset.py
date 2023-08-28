import glob
import os
import random
from sys import platform
from tkinter import Tk

import cv2

import optionss as ops

work_path = os.path.dirname(os.path.realpath(__file__))
ORIGINAL = "original"
BOXED = "boxed"
SHOW = "show"


def create_dir_if_not_exist(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def clear_cmd():
    if platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def plot_one_box(x, image, color=None, label=None, line_thickness=None):
    tl = line_thickness or round(
        0.002 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(image, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(image, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(image, label, (c1[0], c1[1] - 2), 0, tl / 3,
                    [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)


def draw_box_on_image(image_name, classes, colors, class_name, save_type, single_class=False):
    save_type = save_type
    box_count = 0

    image_path = glob.glob(rf"{ops.IMG_FILES_DIR}/{image_name}.*")[0]
    txt_path = glob.glob(rf"{ops.LABEL_FILES_DIR}/{image_name}.*")[0]

    lines_in_txt = open(txt_path) if os.path.exists(txt_path) else []
    image = cv2.imread(image_path)

    if save_type == BOXED or save_type == SHOW:
        try:
            height, width, channels = image.shape
        except Exception as e:
            print('no shape info.', e)
            return 0

        labels = []
        for line in lines_in_txt:
            staff = line.split()
            class_idx = int(staff[0])

            if save_type is SHOW and not single_class:
                print(f"Txt Label Line: {' '.join(staff)} |>|>|> Class Name: {classes[class_idx]}")
            elif save_type is SHOW and single_class and classes[class_idx] == class_name:
                print(f"Txt Label Line: {' '.join(staff)} |>|>|> Class name: {classes[class_idx]}")

            if single_class and classes[class_idx] != class_name:
                continue

            x_center, y_center, w, h = float(staff[1]) * width, float(staff[2]) * height, float(
                staff[3]) * width, float(
                staff[4]) * height
            x1 = round(x_center - w / 2)
            y1 = round(y_center - h / 2)
            x2 = round(x_center + w / 2)
            y2 = round(y_center + h / 2)
            labels.append(classes[class_idx])
            plot_one_box([x1, y1, x2, y2], image, color=colors[class_idx], label=classes[class_idx],
                         line_thickness=None)
            box_count += 1

        image = cv2.resize(image, ops.SAVE_IMAGE_SIZE)

    if save_type == SHOW:
        tk = Tk()
        screen_width, screen_height = tk.winfo_screenwidth(), tk.winfo_screenheight()
        im_height, im_width, im_channels = image.shape

        x = int((screen_width / 2) - (im_width / 2))
        y = int((screen_height / 2) - (im_height / 2))

        print(f"Showing IMG/TXT name: {image_name}\n")

        cv2.namedWindow(image_name)
        cv2.moveWindow(image_name, x, y)
        cv2.imshow(image_name, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return box_count

    save_type = ("single_" if single_class else "") + save_type
    save_dir = f"{work_path}/{save_type}_saved_image/{class_name}"
    create_dir_if_not_exist(save_dir)
    cv2.imwrite(f"{save_dir}/{image_name}.jpg", image)
    cv2.destroyAllWindows()

    return box_count


def make_class_list_for_img_file(class_index_number):
    temp = []
    for txt_file in glob.glob(rf"{ops.LABEL_FILES_DIR}/*.txt"):
        with open(txt_file, mode="r") as f:
            lines = f.readlines()
            file_name, ext = os.path.splitext(os.path.basename(txt_file))
            for line in lines:
                orj_number = int(line.split()[0])
                if orj_number == class_index_number:
                    temp.append(file_name)
    return temp


def start_process(save_type=None, single_class=False):
    class_list = ops.CLASS_LIST
    random.seed(42)
    colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(class_list))]

    image_total = 0
    box_total = 0

    for index, class_name in enumerate(class_list):

        image_list = tuple(set(make_class_list_for_img_file(index)))
        image_total += len(image_list)

        for image_name in image_list:
            box_counts = draw_box_on_image(image_name, class_list, colors, class_name, save_type, single_class)
            box_total += box_counts
            image_total += 1

            if save_type is not SHOW:
                print('Processed Box Count:', box_total, 'Processed Image Count:', image_total)


def run_process(process_type, single_class=None):
    start_process(process_type, single_class)
    print(f"The {process_type} images were saved in the program directory.")
    input(f"\nPress any key for continue...")


if __name__ == '__main__':
    clear_cmd()
    while True:
        print(" Menu ".center(50, "#"))
        print("")
        print("1 - Classify original images save")
        print("2 - Classify boxed draw images save")
        print("3 - Classify boxed draw images save (draw box only for relevant class)")
        print("4 - Classify boxed draw images SHOW")
        print("5 - Classify boxed draw images SHOW (draw box only for relevant class)")
        print("6 - Augment Dataset")
        print("0 - Exit")
        print("")

        input_opt = input("Select: ")

        if input_opt.isnumeric():
            if input_opt == "1":
                run_process(ORIGINAL)
            if input_opt == "2":
                run_process(BOXED)
            if input_opt == "3":
                run_process(BOXED, True)
            if input_opt == "4":
                run_process(SHOW)
            if input_opt == "5":
                run_process(SHOW, True)
            if input_opt == "6":
                import augment_dataset
            if input_opt == "0":
                break
        else:
            clear_cmd()
