import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_and_transcribe(timeout=5):
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source, timeout=timeout)
        print("🎧 Got audio, transcribing...")
        try:
            text = recognizer.recognize_google(audio)  # ✅ MUCH faster
            print("📝 Transcribed:", text)
            return text
        except Exception as e:
            print("⚠️ Error:", str(e))
            return ""
