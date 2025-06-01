import os
import re
from google import genai

api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)

MODEL_NAME = "gemini-2.0-flash"

def generate_course_outline(course_topic: str):
    prompt = (
        f"Create a course outline for '{course_topic}' including:\n"
        "- A brief introduction (100–150 words)\n"
        "- 6 to 10 module titles with 1-line summaries"
    )
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    outline_text = response.text
    introduction = outline_text.split('\n\n')[0]
    modules = re.findall(r"\d+\. (.+)", outline_text)
    return introduction, modules, outline_text

def generate_module_content(module_title: str) -> str:
    prompt = (
        f"Expand this into a full, self-contained learning module:\n\n"
        f"Title: {module_title}\n\n"
        "Include:\n"
        "- A deep, clear explanation of the topic, like a textbook chapter\n"
        "- Examples and analogies\n"
        "- Definitions of key concepts\n"
        "- Diagrams\n"
        "- Visual descriptions\n"
        "- Summary\n"
        "- 3–5 questions or exercises with answers\n"
        "- Further resources (links, books, videos, etc.)\n"
    )
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"*Error generating content: {e}*"
