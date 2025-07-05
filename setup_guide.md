# 🚀 MeetAI-Agent Setup Guide

## ⚠️ Important Notice

This project is designed to run in a Python environment with system-level access for audio processing and browser automation. The current WebContainer environment has limitations:

- Python is available but with limited package installation capabilities (no pip for third-party packages)
- No system-level audio access
- Limited browser automation capabilities
- No VB-Cable or system audio routing

## For Local Development (Recommended)

### 1. Prerequisites
- Python 3.8+ installed on your local machine
- Chrome browser
- VB-Cable for audio routing

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up Environment Variables
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your Gemini API key from: https://makersuite.google.com/app/apikey

### 4. Set up Audio Routing (IMPORTANT!)
Follow the instructions in `audio_routing.md` to set up VB-Cable for proper audio routing between the bot and your meeting software.

### 5. Test Components
```bash
python test_components.py
```

### 6. Run the Bot
```bash
python run_bot.py --url "https://meet.google.com/your-meeting-id" --role "Your role in the meeting"
```

## WebContainer Environment Limitations

In this current environment, you can:
- View and edit the code
- Understand the project structure
- Test basic Python syntax (limited to standard library)

You cannot:
- Install third-party Python packages
- Access system audio devices
- Run browser automation
- Use the full meeting bot functionality

## Alternative Testing in WebContainer

For basic testing of Python logic (without external dependencies):

```bash
# Test basic Python functionality
python3 -c "print('Python is working')"

# View project structure
ls -la

# Check Python version
python3 --version
```

## Example Usage (Local Environment Only)

```bash
# For a project status meeting
python run_bot.py --url "https://meet.google.com/abc-defg-hij" --role "Project Manager providing weekly status update"

# For a client presentation
python run_bot.py --url "https://meet.google.com/xyz-1234-abc" --role "Sales representative presenting product demo"
```

## Troubleshooting

### Common Issues:

1. **"pip command not found" in WebContainer**
   - This is expected - WebContainer doesn't support pip for third-party packages
   - Download the project and run it locally for full functionality

2. **"GEMINI_API_KEY not found"**
   - Make sure you have a `.env` file with your API key
   - Get your key from Google AI Studio

3. **Audio not working**
   - Install VB-Cable from https://vb-audio.com/Cable/
   - Follow audio routing setup in `audio_routing.md`
   - This requires local installation

4. **Chrome profile issues**
   - Update the Chrome profile path in `auto_join_meet.py`
   - Make sure Chrome is installed locally

5. **Microphone permissions**
   - Allow microphone access in your browser
   - Check system microphone permissions

### Testing Individual Components (Local Only):

- **Test TTS**: `python -c "from tts import speak; speak('Hello world')"`
- **Test Speech**: `python -c "from listen import listen_and_transcribe; print(listen_and_transcribe())"`
- **Test Gemini**: `python -c "from gemini_chat import get_gemini_response; print(get_gemini_response('Hello'))"`

## Getting Started Locally

1. **Download this project** to your local machine
2. **Install Python 3.8+** if not already installed
3. **Install required packages**: `pip install -r requirements.txt`
4. **Set up audio routing** following `audio_routing.md`
5. **Configure your API key** in `.env`
6. **Test with a practice meeting** first

## Safety Notes

- The bot will only respond to speech input and generate appropriate responses
- It uses your specified role to maintain context
- Press Ctrl+C to stop the bot at any time
- The bot will automatically leave the meeting when stopped

## Next Steps

1. Download and set up locally for full functionality
2. Test with a practice meeting first
3. Adjust the role prompt for better responses
4. Consider adding custom scripts for specific meeting types