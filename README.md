# Classify Box Drawn Picture or Original Picture
Split the dataset into folders with class names. In the final, there are pictures of that class in each folder.
 
# Augment Dataset by 3x
You can also easily triple your dataset and thus increase your training accuracy.

## Options edit and Usage

Open optionss.py and edit dir paths.

1. Run `pip install opencv-python` and `pip install Pillow`
2. Open `options.py` and set your directory paths.
    1. ###### Example Options
       > `SAVE_IMAGE_SIZE` = **(500, 500)**\
       `IMG_FILES_DIR` = **r"C:\Users\ASUS\Desktop\anydatasets.v5i.yolov8\valid\images**"\
       `LABEL_FILES_DIR` = **r"C:\Users\ASUS\Desktop\anydatasets.v5i.yolov8\valid\labels"**\
       `CLASS_LIST` = **['dog', 'cat', 'people', 'coffe']**

3. Run `python classify_yolo_dataset.py` in your terminal.
4. You can also use the following command to increase the dataset.  Run `python augment_dataset.py` Thus, you can triple your existing data set by inverting both horizontally and vertically.

## Note

Your images will be saved in the directory where the program is running according to your selection.

