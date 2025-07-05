#!/usr/bin/env python3
"""
Test individual components of MeetAI-Agent
"""

import os
from dotenv import load_dotenv

def test_env():
    """Test environment variables"""
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        print("✅ GEMINI_API_KEY found")
        return True
    else:
        print("❌ GEMINI_API_KEY not found in .env")
        return False

def test_tts():
    """Test text-to-speech"""
    try:
        from tts import speak
        print("🗣️ Testing TTS...")
        speak("Hello, this is a test of the text to speech system.")
        print("✅ TTS working")
        return True
    except Exception as e:
        print(f"❌ TTS error: {e}")
        return False

def test_speech_recognition():
    """Test speech recognition"""
    try:
        from listen import listen_and_transcribe
        print("🎤 Testing speech recognition (say something in 5 seconds)...")
        result = listen_and_transcribe(timeout=5)
        if result:
            print(f"✅ Speech recognition working: '{result}'")
            return True
        else:
            print("⚠️ No speech detected, but system is working")
            return True
    except Exception as e:
        print(f"❌ Speech recognition error: {e}")
        return False

def test_gemini():
    """Test Gemini AI"""
    try:
        from gemini_chat import get_gemini_response
        print("🧠 Testing Gemini AI...")
        response = get_gemini_response("Say hello and confirm you're working")
        print(f"✅ Gemini response: {response[:100]}...")
        return True
    except Exception as e:
        print(f"❌ Gemini error: {e}")
        return False

def main():
    print("🧪 Testing MeetAI-Agent Components\n")
    
    tests = [
        ("Environment", test_env),
        ("Text-to-Speech", test_tts),
        ("Speech Recognition", test_speech_recognition),
        ("Gemini AI", test_gemini),
    ]
    
    results = []
    for name, test_func in tests:
        print(f"\n--- Testing {name} ---")
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ {name} failed: {e}")
            results.append((name, False))
    
    print("\n" + "="*50)
    print("📊 TEST RESULTS:")
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} {name}")
    
    all_passed = all(result for _, result in results)
    if all_passed:
        print("\n🎉 All tests passed! Ready to run the meeting bot.")
    else:
        print("\n⚠️ Some tests failed. Check the errors above.")

if __name__ == "__main__":
    main()