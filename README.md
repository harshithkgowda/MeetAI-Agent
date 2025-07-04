﻿# MeetAI-Agent
🎯 AI Meeting Agent With Voice Cloning
💡 Concept
You’re building an AI meeting representative that:

Replicates the user’s voice using ElevenLabs

Speaks a predefined script during online meetings (e.g., Zoom, Meet)

Uses Gemini 1.5 Flash to understand meeting context and generate smart talking points

Does not go off-script or answer unexpected questions — ensuring user stays in control

🧠 Use Case: “I can’t attend this client check-in, but I want the agent to introduce the roadmap using my voice and scripted key points.”

🎬 How It Works (User Journey)
User Logs In

User Chooses Meeting Type (e.g., client intro, status update, pitch)

Inputs Required Info:

Meeting link or invite

Their role in the meeting

What they’re expected to say (in bullets or a script)

Agent Prepares Scripted Dialogue using Gemini 1.5 Flash

Voice is cloned using ElevenLabs

Agent Joins Meeting (audio-only):

Introduces user politely

Delivers speech clearly in user’s voice

Politely declines off-topic or follow-up questions with pre-written “I’ll follow up after the call” lines

Optional: After meeting, user gets a summary or transcript.

🌍 Use Cases
Entrepreneurs managing multiple calls

Students submitting class presentations

Employees attending overlapping meetings

Clients attending RFP briefings

Influencers who can’t attend interviews live

International timezone conflicts

🔍 Similar/Existing Tools (Competitor Analysis)
| Tool                                 | What It Does                  | How You’re Different                             |
| ------------------------------------ | ----------------------------- | ------------------------------------------------ |
| **Synthesia**                        | Avatar video generation       | Not live, no voice interaction                   |
| **Tavus**                            | AI video in your face & voice | Not real-time, not for meetings                  |
| **Otter Assistant**                  | Joins meetings & takes notes  | Doesn’t speak, not voice-cloned                  |
| **Voice AI (Descript, Resemble AI)** | Voice cloning tools           | No meeting agent integration                     |
| **Zoom AI Companion**                | Summarizes meetings           | Doesn’t speak for you                            |
| **Custom ElevenLabs Use**            | Many do voice generation      | You combine it into a full **meeting bot agent** |

🧪 MVP Tech Stack

| Component                         | Tool                                                                      |
| --------------------------------- | ------------------------------------------------------------------------- |
| AI Script Brain                   | **Gemini 1.5 Flash** (for fast context understanding & script generation) |
| Voice Cloning                     | **ElevenLabs** (for natural, emotional replication)                       |
| Meeting Joiner                    | Zoom/Google Meet SDK + headless browser or OBS integration                |
| Interface                         | React.js dashboard                                                        |
| Scheduling                        | Google Calendar API or Cal.com                                            |
| Backend                           | FastAPI or Node.js                                                        |
| Authentication                    | Firebase / Auth0                                                          |
| Storage                           | Supabase / Firebase DB                                                    |
| Speech-to-Text (optional summary) | Whisper or Gemini / Google Cloud STT                                      |

🔐 Safety Features
Voice Consent Required (user must record baseline and approve final output)

Script Lock: Agent will not respond to live questions outside of script

“I’ll follow up” fallback phrases for unhandled inputs

End-user control: User reviews and edits everything before deployment

Meeting logs: Stored securely (optional)

🧠 AI Script Modes

| Mode                     | Behavior                                                               |
| ------------------------ | ---------------------------------------------------------------------- |
| **Auto Assist**          | User inputs rough notes → Gemini 1.5 Flash polishes into formal speech |
| **Strict Script**        | Agent says exactly what user wrote                                     |
| **Conditional** (future) | AI handles some replies if user allows on-topic Q\&A only              |

🏷️ Credit & Founder
🧑‍💻 This idea was created and conceptualized by Harshith K in 2025, based on modern challenges of multi-tasking professionals in a post-remote world.

RepBot 2.0 — now adapted for everyone who can’t be in two meetings at once, but still wants to sound present, professional, and human.

