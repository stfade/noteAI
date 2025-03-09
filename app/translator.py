from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from utils import save_to_file

TEMPERATURE = 0.9
MAX_OUTPUT_TOKENS = 128000

load_dotenv()

sys_instruction = """
Role: AI English-to-Turkish Translator
Objective: Translate English text into clear and natural Turkish while maintaining tone, intent, and cultural nuances.
Output Format: Direct Turkish translation
Contextual Boundaries:

Preserve the original meaning and fluency.
Adapt cultural references appropriately.
Ensure idiomatic expressions sound natural in Turkish.
Rules:
Do not explain or provide notes to a human reader.
Maintain clarity and readability.
Highlight ambiguous phrases that require contextual clarification.
Do not translate terms.
Output Format: Translated Turkish text without additional commentary
Revision Log: Updates in phrasing, tone, or handling of ambiguous terms based on feedback.
"""

prompt = """
Translate the following English text into clear and natural Turkish. 
Ensure the translation maintains the original tone, intent, and cultural nuances. 
If the text contains idioms, proverbs, or culturally specific references, provide an equivalent expression in Turkish. 
Highlight any ambiguous phrases where context might affect accuracy. Do not add notes or explanations for humans.
Please do not translate terms.
---

{english_text}
"""

class Translator():
    def __init__(self):
        self.client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'), http_options={'api_version': 'v1alpha'})

    # Translate English text to Turkish using the AI model and save the output to a file
    def translate(self, filepath, content, type):
        if not isinstance(content, str):
            raise ValueError("Content must be a string.")

        # Format the prompt with topic list
        prompt_f = prompt.format(english_text=content)

        response = self.client.models.generate_content(
            model='gemini-2.0-flash-thinking-exp',
            config=types.GenerateContentConfig(
                temperature=TEMPERATURE,
                max_output_tokens=MAX_OUTPUT_TOKENS,
                system_instruction=sys_instruction
            ),
            contents=[
                prompt_f
            ]
        )

        # Save the translated note to a file
        try:
            save_to_file(filepath=filepath, content=response.text, lang="tr", type=type)
        except Exception as e:
            print(f"Error saving file: {str(e)}")
