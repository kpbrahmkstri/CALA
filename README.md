# 🤖 CALA: Context-Aware Life Assistant (Powered by MCP)

CALA is an intelligent, context-aware AI life assistant built using OpenAI models and the **Model Context Protocol (MCP)** pattern. It provides **personalized, human-like advice** based on structured context — such as your mood, calendar events, environment, and life goals.

>  This project showcases real-world MCP usage — modular context construction, multi-source reasoning, and adaptive LLM response — ideal for portfolio or production reference.

---

##  Features

-  **Modular Context Design** — loads user profile, mood logs, schedule, and weather as structured MCP context files.
-  **Personalized Prompting** — dynamically adapts advice based on who you are and how you feel.
-  **LLM-Powered Agent** — uses OpenAI's GPT-4 to generate wellness recommendations, plans, and reflections.
-  **Easy to Extend** — plug in new context layers (e.g., fitness, location, journaling) without changing logic.


## ⚙️ Setup Instructions

```bash
1. Clone the repo

git clone https://github.com/kpbrahmkstri/CALA.git

2. Create and activate virtual environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt


4. Set up your OpenAI key
Create a .env file in the root directory:

OPENAI_API_KEY=your-openai-api-key-here


🧪 Run the App
streamlit run streamlit_app.py


