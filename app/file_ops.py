import os
import pathlib

def save_to_file(filepath, content, lang="en", type="sum"):
    # Create 'dist' directory if it doesn't exist
    current_dir = pathlib.Path(os.path.dirname(os.path.realpath(__file__)))
    dist_dir = current_dir.parent / "output"
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