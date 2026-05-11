from PIL import Image
import os
import sys

# Sizes to generate
SIZES = [16, 32, 48, 128]

def resize_icons(input_path):
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    try:
        img = Image.open(input_path).convert("RGBA")
    except Exception as e:
        print(f"Failed to open image: {e}")
        return

    # Create output folder for each input image inside images/output
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_dir = os.path.join("images", "output", base_name)
    os.makedirs(output_dir, exist_ok=True)

    for size in SIZES:
        resized = img.resize((size, size), Image.LANCZOS)
        output_path = os.path.join(
            output_dir,
            f"icon{size}.png"
        )
        resized.save(output_path, format="PNG")
        print(f"Saved: {output_path}")
    print("\nDone.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("python resize_icons.py your_image.png")
    else:
        resize_icons(sys.argv[1])


