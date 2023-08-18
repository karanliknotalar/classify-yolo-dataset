# Draw or Original Classify Yolo Dataset

Split your existing dataset into folders with classes. While doing this, make it as an original picture or a box-drawn
picture and save it.

## Options and Usage

Open optionss.py and edit dir paths.

1. Run `pip install opencv-python`
2. Open `options.py` and set your directory paths.
    1. ###### Example Options
       > `SAVE_IMAGE_SIZE` = **(500, 500)**\
       `IMG_FILES_DIR` = **r"C:\Users\ASUS\Desktop\anydatasets.v5i.yolov8\valid\images**"\
       `LABEL_FILES_DIR` = **r"C:\Users\ASUS\Desktop\anydatasets.v5i.yolov8\valid\labels"**\
       `CLASS_LIST` = **['dog', 'cat', 'people', 'coffe']**\

3. Run `python classify_yolo_dataset.py` in your terminal.

## Note

Your images will be saved in the directory where the program is running according to your selection.

