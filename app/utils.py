import os
import sys
import pathlib

def save_to_file(filepath, content, lang="en", type="sum"):
    # Create 'output' directory if it doesn't exist
    current_dir = pathlib.Path(get_resource_path())
    dist_dir = current_dir / "output"
    dist_dir.mkdir(exist_ok=True)
    title = os.path.basename(filepath).split('/')[-1]

    try:
        # Write the response text to a file in the 'output' directory
        output_path = dist_dir / f"{title}-{type}-{lang}.txt"
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"File saved successfully: {output_path}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

def get_resource_path(relative_path = ""):
    """Get absolute path for assets in a bundled application."""
    if getattr(sys, 'frozen', False):
        # Running as a PyInstaller executable
        base_path = sys._MEIPASS
    else:
        # Running in normal Python environment
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)