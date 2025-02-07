from image2text import Image2Text
from note import Note
import os

def process_logic(pdf_path, image_path):
    # pdf_path = "//wsl.localhost/Ubuntu/home/user0/Projects/AI/noteAI/part-1.pdf"
    # image_path = "//wsl.localhost/Ubuntu/home/user0/Projects/AI/noteAI/a.png"

    try:
        image2text = Image2Text() # Image2Text model
        generator = Note(file_path=pdf_path) # Note generator model

        try:
            print(f"Processing image...")  
            # Get text from image (Topic list extraction from image)
            image_text = image2text.get_text(image_path)
            # print(f"{image_text=}")

        except Exception as e:
            print(f"Error getting text from the image: {str(e)}")
            return

        try:
            print(f"Generating note ...")
            # Generate note with extracted text
            generator.gen_qa_note_pdf(image_text)

            print(f"Note generated successfully.")

        except Exception as e:
            print(f"Error generating note: {str(e)}")
            return

    except Exception as e:
            print(f"Error getting text from the model: {str(e)}")