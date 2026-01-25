import os
from PIL import Image

source_folder = "./photos/"
output_folder = "./optimized/"
target_width = 800

def resize_images():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith(('.jpg', '.png')):
            img_path = os.path.join(source_folder, filename)
            with Image.open(img_path) as img:
                # Calculate new height to maintain aspect ratio
                aspect_ratio = img.height / img.width
                target_height = int(target_width * aspect_ratio)
                
                # Resize and save
                img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                
                # Save optimized version
                save_path = os.path.join(output_folder, filename)
                img.save(save_path, optimize=True, quality=85)
                print(f"Resized and saved: {filename}")

if __name__ == "__main__":
    resize_images()
