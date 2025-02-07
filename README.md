# noteAI

noteAI is a Python-based desktop application that enables you to extract text from images using OCR and generate study notes in a question-answer format from PDF files. The application leverages experimental Google Gemini models for both image-to-text and note generation, and it features a clean and intuitive PyQt5 GUI.

## Features

- **Image Text Extraction:**  
  Uses OCR and image captioning to extract text from images ([`app/image2text.py`](app/image2text.py)).

- **Study Note Generation:**  
  Processes PDF files to generate study notes in a Q&A format ([`app/note.py`](app/note.py)).

- **Graphical User Interface:**  
  A user-friendly PyQt5 interface for uploading files and processing ([`app/gui.py`](app/gui.py)).

## Project Structure

```
app/
    __pycache__/
    assets/
        app-icon.png
    .env
    file_ops.py
    gui.py
    image2text.py
    logic.py
    main.py
    note.py
    processing_worker.cpython-312.pyc
    styles.py
    translator.py
```

- **[`app/main.py`](app/main.py):**  
  Entry point for the application that initializes the PyQt5 app, sets the window icon, and launches the GUI.

- **[`app/gui.py`](app/gui.py):**  
  Implements the main GUI for file uploads and processing.

- **[`app/image2text.py`](app/image2text.py):**  
  Contains the logic to extract text from images using Google Gemini's experimental OCR and image captioning capabilities.

- **[`app/note.py`](app/note.py):**  
  Implements the note generation logic from PDF files including the Q&A format.

- **[`app/logic.py`](app/logic.py):**  
  Orchestrates the workflow by integrating image-to-text and note generation processes.

- **[`app/styles.py`](app/styles.py):**  
  Contains the stylesheet definitions for the GUI.

- **[`app/.env`](app/.env):**  
  Stores environment variables such as the Google API key.

## Installation

1. **Clone the Repository:**

   ```sh
   git clone <repository-url>
   cd noteAI
   ```

2. **Set Up a Virtual Environment:**

   ```sh
   python -m venv venv
   # On Unix/macOS:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

   *Dependencies include PyQt5, python-dotenv, Pillow, and Google GenAI client libraries.*

4. **Configure Environment Variables:**

   Edit .env to include your Google API key:
   
   ```
   GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
   ```

## Usage

1. **Run the Application:**

   Start the application by running:

   ```sh
   python app/main.py
   ```

2. **Upload Files via GUI:**

   - Click "📄 Upload PDF" to select a PDF file.
   - Click "🖼 Upload Image" to select an image file.
   - Once both files are uploaded, click "▶ Start Process" to extract text from the image and generate study notes from the PDF.

## Troubleshooting

- Ensure that the app-icon.png exists for the window icon.
- Check that your API key in .env is valid and has necessary permissions.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Built with [PyQt5](https://www.riverbankcomputing.com/software/pyqt/intro) for the GUI.
- Powered by Google's experimental Gemini models for text extraction and note generation.
```

This README provides clear guidance on installation, usage, and project structure while referencing key project files such as [`app/main.py`](app/main.py) and [`app/gui.py`](app/gui.py).