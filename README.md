# Daily Motivation Generator using GPT-3.5

This is a simple AI project I made for the GenAI course submission. The idea is pretty straightforward — the user selects their mood (like anxious, low energy, procrastinating etc.) and the app shows a short motivational quote that matches the feeling.
It uses OpenAI’s GPT-3.5 API to generate the quotes in real time and displays them using a clean Streamlit interface.

# What the App Does
- You choose your mood from a dropdown (around 5–6 options).
- It sends that to GPT with a basic prompt.
- GPT-3.5 returns a short, motivational quote that’s related to how you’re feeling.
- The app then shows it on the screen.
I tried to keep it minimal and useful.

# Tools Used
- Python
- Streamlit (for the frontend)
- OpenAI API (gpt-3.5-turbo)
- Basic prompt engineering

#  How to Run the App
- Clone this repo or download the code
- Install the libraries:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
