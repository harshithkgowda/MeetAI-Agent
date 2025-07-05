#!/usr/bin/env python3
"""
MeetAI-Agent Runner
Run the AI meeting bot with command line arguments
"""

import sys
import os
from meeting_bot import main

def show_usage():
    print("""
🎯 MeetAI-Agent - AI Meeting Bot
    
Usage:
    python run_bot.py --url "MEETING_URL" --role "YOUR_ROLE"
    
Examples:
    python run_bot.py --url "https://meet.google.com/abc-defg-hij" --role "Project Manager presenting quarterly updates"
    
    python run_bot.py --url "https://meet.google.com/xyz-1234-abc" --role "Developer discussing technical implementation"
    
Required:
    --url   : Google Meet URL
    --role  : Your role/purpose in the meeting
    
Make sure you have:
    ✅ GEMINI_API_KEY in your .env file
    ✅ Chrome browser installed
    ✅ VB-Cable for audio routing (see audio_routing.md)
    ✅ Microphone permissions enabled
    """)

if __name__ == "__main__":
    if len(sys.argv) < 5 or "--help" in sys.argv or "-h" in sys.argv:
        show_usage()
        sys.exit(1)
    
    # Check if .env exists
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("Create a .env file with your GEMINI_API_KEY")
        print("Example: GEMINI_API_KEY=your_api_key_here")
        sys.exit(1)
    
    try:
        # Parse arguments manually for simplicity
        url_index = sys.argv.index("--url") + 1
        role_index = sys.argv.index("--role") + 1
        
        meeting_url = sys.argv[url_index]
        user_role = sys.argv[role_index]
        
        print(f"🚀 Starting MeetAI-Agent...")
        print(f"📅 Meeting URL: {meeting_url}")
        print(f"👤 Role: {user_role}")
        print(f"🎤 Make sure your audio routing is set up (see audio_routing.md)")
        
        main(meeting_url, user_role)
        
    except (ValueError, IndexError):
        print("❌ Invalid arguments!")
        show_usage()
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)