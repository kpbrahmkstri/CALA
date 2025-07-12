import os
from dotenv import load_dotenv
import json

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def load_context(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def build_combined_context() -> str:
    base_dir = "contexts"
    context_files = [
        "user_profile.json",
        "mood_log.json",
        "calendar_context.json",
        "weather_context.json"
    ]
    context_blocks = []
    for file in context_files:
        content = load_context(os.path.join(base_dir, file))
        context_blocks.append(f"{file.replace('.json', '').upper()}:\n{json.dumps(content, indent=2)}")
    return "\n\n".join(context_blocks)