import streamlit as st
import openai

st.set_page_config(page_title="Daily Motivation Generator", layout="centered")
openai.api_key = "my-gpt-api-key-here" 
st.title(" Daily Motivation Generator")
st.write("Feeling down or distracted? Get a boost of motivation tailored to your current mood.")


moods = ["Feeling anxious", "Need focus", "Low energy", "Procrastinating", "Feeling sad", "Confident but stuck"]
selected_mood = st.selectbox("Select your current mood:", moods)


if st.button("Generate Motivation"):
    
    with st.spinner("Generating your personalized quote..."):
        
        prompt = (
            f"You are a motivational coach. Give one short, uplifting, and realistic quote for someone who is '{selected_mood.lower()}'.\n"
            f"Keep it simple and honest. No clichés. Just genuine encouragement."
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.8,
                max_tokens=100
            )

            output_text = response["choices"][0]["message"]["content"].strip()

            st.subheader("Your Motivation:")
            st.success(output_text)

        except Exception as e:
            st.error("Something went wrong. Please check your API key or internet connection.")