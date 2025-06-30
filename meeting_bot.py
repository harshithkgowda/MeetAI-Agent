import os
import pyttsx3
import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
from auto_join_meet import join_google_meet

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize TTS
engine = pyttsx3.init()

def speak(text):
    print("🗣️ Speaking:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        print("🎧 Got audio, transcribing...")
        text = recognizer.recognize_google(audio)
        print("📝 Transcribed:", text)
        return text
    except sr.UnknownValueError:
        print("⚠️ Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"⚠️ Request error: {e}")
        return None

def generate_reply(prompt, conversation_history):
    history = [
        {"role": "user", "parts": f"{item['content']}"}
        if item["author"] == "user"
        else {"role": "model", "parts": f"{item['content']}"}
        for item in conversation_history
    ]
    chat = model.start_chat(history=history)
    response = chat.send_message(prompt)
    return response.text

def main(meeting_url, user_role_prompt):
    driver = join_google_meet(meeting_url)

    conversation_history = [
        {"author": "user", "content": f"Your role in the meeting: {user_role_prompt}. Respond professionally and clearly."}
    ]

    try:
        while True:
            user_input = listen()
            if user_input:
                conversation_history.append({"author": "user", "content": user_input})
                reply = generate_reply(user_input, conversation_history)
                conversation_history.append({"author": "assistant", "content": reply})
                speak(reply)
            else:
                print("⚠️ No speech input.")
    except KeyboardInterrupt:
        print("🛑 Stopped by user.")
    finally:
        driver.quit()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run AI Meeting Bot")
    parser.add_argument("--url", type=str, required=True, help="Google Meet URL")
    parser.add_argument("--role", type=str, required=True, help="Your role in the meeting")

    args = parser.parse_args()
    main(args.url, args.role)
