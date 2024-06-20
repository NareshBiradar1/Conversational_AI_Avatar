# AI Conversational Chatbot

This project implements an AI Conversational Chatbot using various AI and multimedia libraries. The chatbot can transcribe audio, generate responses using a conversational AI model, and produce a video with synchronized lip movements.

## Description

The AI Conversational Chatbot uses:
- **Tkinter** for the GUI
- **OpenCV** and **PIL** for video and image processing
- **pygame** for audio playback
- **sounddevice** and **scipy** for audio recording
- **Google Generative AI** for generating chatbot responses
- **gTTS** for text-to-speech conversion
- **Gooey.AI API** for synchronizing audio with a video avatar

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-conversational-chatbot.git
   cd ai-conversational-chatbot

2. Install the required packages:
    ```bash
    Copy code
    pip install -r requirements.txt

## Usage
    Run the main application:

    ```bash
    Copy code
    python main.py

Use the GUI to interact with the chatbot:

- Type a message and click "Ask the AI" to get a response.
- Click "Record Audio" to transcribe spoken input.

## Features

- **Text-based interaction**: Type messages to receive AI responses.
- **Voice interaction**: Record audio and transcribe it to text.
- **Audio-Video Generation**: Generate synchronized video responses with an avatar.

## Examples

- Ask a question by typing into the input field and clicking "Ask the AI".
- Record a question by clicking "Record Audio", then the AI will transcribe and respond with a video.

## Dependencies

The project relies on the following libraries and tools:

- tkinter
- opencv-python
- Pillow
- pygame
- sounddevice
- scipy
- google-generativeai
- speechrecognition
- gtts
- requests

See `requirements.txt` for the full list of dependencies.

## Project Structure

AI Conversational Chatbot/
├── main.py
├── media/
│   ├── audio.mp3
│   ├── avatar2.jpg
│   └── video.mp4
├── modules/
│   ├── app.py
│   ├── gemini_response.py
│   ├── speech_to_text.py
│   └── video_audio_generation.py
└── requirements.txt

### Contributors
Naresh Biradar


