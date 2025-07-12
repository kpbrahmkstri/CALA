# 🤖 CALA: Context-Aware Life Assistant (Powered by MCP)

CALA is an intelligent, context-aware AI life assistant built using OpenAI models and the **Model Context Protocol (MCP)** pattern. It provides **personalized, human-like advice** based on structured context — such as your mood, calendar events, environment, and life goals.

> 🧠 This project showcases real-world MCP usage — modular context construction, multi-source reasoning, and adaptive LLM response — ideal for portfolio or production reference.

---

## 🚀 Features

- 🧩 **Modular Context Design** — loads user profile, mood logs, schedule, and weather as structured MCP context files.
- 🎯 **Personalized Prompting** — dynamically adapts advice based on who you are and how you feel.
- 🧠 **LLM-Powered Agent** — uses OpenAI's GPT-4 to generate wellness recommendations, plans, and reflections.
- 🧪 **Easy to Extend** — plug in new context layers (e.g., fitness, location, journaling) without changing logic.

---

## 🧱 Project Structure

├── main.py # Entry point
├── app/
│ ├── context_loader.py # Loads and merges contexts
│ ├── prompt_builder.py # Builds prompts with context
│ ├── agent.py # Calls OpenAI API (v1+)
├── contexts/ # JSON context files
│ ├── user_profile.json
│ ├── mood_log.json
│ ├── calendar_context.json
│ ├── weather_context.json
├── .env # OpenAI API key
├── requirements.txt
├── .gitignore
├── README.md