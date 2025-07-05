# 🚀 MeetAI-Agent Setup Guide

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set up Environment Variables
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your Gemini API key from: https://makersuite.google.com/app/apikey

### 3. Set up Audio Routing (IMPORTANT!)
Follow the instructions in `audio_routing.md` to set up VB-Cable for proper audio routing between the bot and your meeting software.

### 4. Test Components
```bash
python test_components.py
```

### 5. Run the Bot
```bash
python run_bot.py --url "https://meet.google.com/your-meeting-id" --role "Your role in the meeting"
```

## Example Usage

```bash
# For a project status meeting
python run_bot.py --url "https://meet.google.com/abc-defg-hij" --role "Project Manager providing weekly status update"

# For a client presentation
python run_bot.py --url "https://meet.google.com/xyz-1234-abc" --role "Sales representative presenting product demo"
```

## Troubleshooting

### Common Issues:

1. **"GEMINI_API_KEY not found"**
   - Make sure you have a `.env` file with your API key
   - Get your key from Google AI Studio

2. **Audio not working**
   - Install VB-Cable from https://vb-audio.com/Cable/
   - Follow audio routing setup in `audio_routing.md`

3. **Chrome profile issues**
   - Update the Chrome profile path in `auto_join_meet.py`
   - Make sure Chrome is installed

4. **Microphone permissions**
   - Allow microphone access in your browser
   - Check system microphone permissions

### Testing Individual Components:

- **Test TTS**: `python -c "from tts import speak; speak('Hello world')"`
- **Test Speech**: `python -c "from listen import listen_and_transcribe; print(listen_and_transcribe())"`
- **Test Gemini**: `python -c "from gemini_chat import get_gemini_response; print(get_gemini_response('Hello'))"`

## Safety Notes

- The bot will only respond to speech input and generate appropriate responses
- It uses your specified role to maintain context
- Press Ctrl+C to stop the bot at any time
- The bot will automatically leave the meeting when stopped

## Next Steps

1. Test with a practice meeting first
2. Adjust the role prompt for better responses
3. Consider adding custom scripts for specific meeting types