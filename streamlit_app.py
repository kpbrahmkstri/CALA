from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from app.context_loader import build_combined_context
from app.prompt_builder import build_prompt
from app.agent import ask_openai
from app.weather_fetcher import fetch_weather
from app.calendar_fetcher import fetch_calendar_events
import json
from datetime import date



st.set_page_config(page_title="CALA Assistant", layout="centered")
st.title("🤖 CALA: Context-Aware Life Assistant")

# Sidebar with optional settings
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("CALA is an MCP-based AI assistant that gives life advice using your mood, calendar, and more.")

    # Mood Logging Section
st.subheader("🧘 Mood Tracker")

mood_today = st.radio("How do you feel today?", ["😄 Happy", "😐 Neutral", "😫 Stressed", "😴 Tired"], horizontal=True)

if st.button("Log Mood"):
    mood_value = mood_today.split()[1]  # Extract the word (e.g., "Happy")
    mood_file = "contexts/mood_log.json"

    # Load current mood log
    with open(mood_file, "r") as f:
        mood_data = json.load(f)

    # Append today’s mood
    today_str = date.today().isoformat()
    mood_data["last_7_days"].append({"date": today_str, "mood": mood_value.lower()})

    # Keep only last 7 entries
    mood_data["last_7_days"] = mood_data["last_7_days"][-7:]

    # Optionally, update trend
    recent = [m["mood"] for m in mood_data["last_7_days"]]
    if recent.count("happy") > recent.count("stressed"):
        mood_data["trend"] = "recovering"
    elif recent.count("stressed") > 3:
        mood_data["trend"] = "critical"
    else:
        mood_data["trend"] = "neutral"

    # Save back to file
    with open(mood_file, "w") as f:
        json.dump(mood_data, f, indent=2)

    st.success(f"Mood logged as '{mood_value}' for {today_str}")

calendar_data = fetch_calendar_events()  # Now guaranteed to return events

with open("contexts/calendar_context.json", "w") as f:
    json.dump(calendar_data, f, indent=2)

weather_context_path = "contexts/weather_context.json"

weather_data = fetch_weather("San Francisco")  # or make location dynamic
with open(weather_context_path, "w") as f:
    json.dump(weather_data, f, indent=2)

# Input field
user_query = st.text_input("🗨️ Ask CALA something:", placeholder="e.g., How should I plan my day?")

# Show context (toggle)
show_context = st.checkbox("Show Context", value=False)

# Trigger agent
if st.button("Get Advice") and user_query:
    with st.spinner("Thinking..."):
        context = build_combined_context()
        prompt = build_prompt(context, user_query)
        response = ask_openai(prompt)
        st.success("Here's what CALA recommends:")
        st.write(response)

        if show_context:
            st.subheader("🧠 Loaded Context")
            st.code(context, language="json")
