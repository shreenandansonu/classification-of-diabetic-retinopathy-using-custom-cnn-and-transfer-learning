import os
import shutil
import random

# Paths
source_dir = r"F:\Machine Learning\DRP\drp\source images"
base_dir = r"F:\Machine Learning\DRP\drp\dataset"  # New folder for split data

# Percentages
train_split = 0.7
val_split = 0.15
test_split = 0.15

# Make output folders
for split in ["train", "val", "test"]:
    for class_name in os.listdir(source_dir):
        os.makedirs(os.path.join(base_dir, split, class_name), exist_ok=True)

# Loop through each class folder
for class_name in os.listdir(source_dir):
    class_path = os.path.join(source_dir, class_name)
    if os.path.isdir(class_path):
        images = os.listdir(class_path)
        random.shuffle(images)

        # Calculate split indexes
        train_end = int(len(images) * train_split)
        val_end = train_end + int(len(images) * val_split)

        # Split images
        train_files = images[:train_end]
        val_files = images[train_end:val_end]
        test_files = images[val_end:]

        # Copy files
        for img in train_files:
            shutil.copy(os.path.join(class_path, img), os.path.join(base_dir, "train", class_name))
        for img in val_files:
            shutil.copy(os.path.join(class_path, img), os.path.join(base_dir, "val", class_name))
        for img in test_files:
            shutil.copy(os.path.join(class_path, img), os.path.join(base_dir, "test", class_name))

print("✅ Dataset split complete!")
