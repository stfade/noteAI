from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import pathlib
from file_ops import save_to_file
from translator import Translator

load_dotenv()

sys_instruction_qa = """
You are an expert in creating study notes in a question-answer format, especially for technical subjects like Computer Engineering at the university level.  Your task is to process text extracted from a context and generate study notes focusing on key concepts and information.

Your process will be:

1. **Identify Topics and Subtopics:**  Carefully read the provided text and list the primary topics and subtopics discussed.
2. **Formulate Questions and Extract Answers:** For each topic and subtopic, create relevant questions that test understanding of the material.  Crucially, **extract the answers directly and verbatim from the context.** Do not paraphrase or summarize the answers – they must be exactly as written in the source.
3. **Clear Q&A Presentation:** Present the notes as a series of question-answer pairs.  Use "Q:" and "A:" prefixes for clarity, or bold the questions for visual distinction.  Ensure the formatting is easy to read and study from.
"""

prompt_qa = """
Given the pdf file, do this task as best as possible:
You are a studying and note taking expert. I need you to create study notes in a question-answer format from the following PDF. I am a university student studying Computer Engineering. Please focus on generating Q&A pairs related to these specific aspects from the context:

---

{topic_list}

---

For each of these areas, formulate questions and extract the answers directly from the context. Please present the Q&A pairs clearly, perhaps using "Q:" and "A:" prefixes or bolding the questions.
"""

class Note():
    def __init__(self, file_path):
        self.file_path = file_path
        self.client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'), http_options={'api_version': 'v1alpha'})

    # Generate note about topic list from pdf (QA format)
    def gen_qa_note_pdf(self, topic_list):
        if not isinstance(topic_list, str):
            raise ValueError("Topic list must be a string.")

        # Format the prompt with topic list
        prompt_f = prompt_qa.format(topic_list=topic_list)

        # Get the document path with pathlib
        filepath = pathlib.Path(self.file_path)

        # Generate content from the pdf file
        response = self.client.models.generate_content(
            model='gemini-2.0-flash-thinking-exp',
            config=types.GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=50000,
                system_instruction=sys_instruction_qa

            ),
            contents=[
                types.Part.from_bytes(
                    data=filepath.read_bytes(),
                    mime_type='application/pdf',
                ),
                prompt_f
            ],
        )

        # I do saving part in here instead of logic part because of the response length. 
        # I do not want to return all of the content.

        # Save the generated note in English to a file
        try:
            save_to_file(filepath=filepath, content=response.text)
        except Exception as e:
            print(f"Error saving file: {str(e)}")

        # Translate the generated note to Turkish and save it to a file
        try:
            translator = Translator()
            translator.translate(filepath=filepath, content=response.text)
        except Exception as e:
            print(f"Error translating to Turkish: {str(e)}")