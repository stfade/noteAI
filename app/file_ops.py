import os

def save_to_file(filepath, content, lang="en"):
    # Create 'dist' directory if it doesn't exist
    dist_dir = filepath.parent / "dist"
    dist_dir.mkdir(exist_ok=True)
    title = os.path.basename(filepath).split('/')[-1]

    # Write the response text to a file in the 'dist' directory
    output_path = dist_dir / f"{title}-{lang}.txt"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)