import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
source_dir = r"F:\Machine Learning\DRP\drp\test"  
train_dir = r"F:\Machine Learning\DRP\drp\train"
val_dir = r"F:\Machine Learning\DRP\drp\val"

# Create output dirs
for folder in [train_dir, val_dir]:
    os.makedirs(folder, exist_ok=True)

# Loop through each class folder
for class_name in os.listdir(source_dir):
    class_path = os.path.join(source_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    images = os.listdir(class_path)
    train_files, val_files = train_test_split(images, test_size=0.2, random_state=42)

    # Create subfolders for the class in train and val
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(val_dir, class_name), exist_ok=True)

    # Move/copy files
    for file in train_files:
        shutil.copy(os.path.join(class_path, file), os.path.join(train_dir, class_name, file))
    for file in val_files:
        shutil.copy(os.path.join(class_path, file), os.path.join(val_dir, class_name, file))

print("✅ Data split complete!")
