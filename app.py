import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 600), keep_aspect_ratio=True, output_format="JPEG", quality=85):
    """
    Resize and convert all images in a folder.
    
    Parameters:
    - input_folder: str -> Path to folder with images
    - output_folder: str -> Path to save processed images
    - size: tuple -> (width, height)
    - keep_aspect_ratio: bool -> Keep original aspect ratio
    - output_format: str -> "JPEG", "PNG", etc.
    - quality: int -> JPEG quality (1–100)
    """
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    if not images:
        print("❌ No images found in the input folder.")
        return

    print(f"📂 Found {len(images)} images. Processing...\n")
    
    for i, filename in enumerate(images, start=1):
        try:
            img_path = os.path.join(input_folder, filename)
            with Image.open(img_path) as img:
                if keep_aspect_ratio:
                    img.thumbnail(size)
                else:
                    img = img.resize(size)

                base_name = os.path.splitext(filename)[0]
                save_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
                
                img.save(save_path, output_format, quality=quality)
                
                print(f"✅ [{i}/{len(images)}] {filename} resized & saved as {output_format}")
        except Exception as e:
            print(f"⚠️ Skipping {filename} due to error: {e}")
    
    print("\n🎯 Task Completed! All images are saved in:", output_folder)


# === Example Usage ===
if __name__ == "__main__":
    input_folder = "images_input"      # Folder with original images
    output_folder = "images_output"    # Folder to save resized images
    target_size = (800, 600)           # Resize target
    keep_ratio = True                  # Keep aspect ratio
    format_type = "JPEG"               # Output format
    jpeg_quality = 85                  # JPEG Quality (1-100)

    resize_images(input_folder, output_folder, target_size, keep_ratio, format_type, jpeg_quality)
