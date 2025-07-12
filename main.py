from app.context_loader import build_combined_context
from app.prompt_builder import build_prompt
from app.agent import ask_openai

def run():
    print("🧠 Welcome to CALA: Context-Aware Life Assistant")
    user_query = input("What would you like help with today?\n> ")
    context = build_combined_context()
    prompt = build_prompt(context, user_query)
    response = ask_openai(prompt)
    print("\n🤖 CALA says:\n")
    print(response)

if __name__ == "__main__":
    run()
