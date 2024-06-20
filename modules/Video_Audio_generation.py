import urllib.request
import requests
import json
from gtts import gTTS
     

class generateVideo_and_audio:
    def __init__(self, avatar_source):
        self.avatar_source = avatar_source

    def text_to_audio(self, message, audio_output):
        try:
            tts = gTTS(message, lang='en')
            tts.save(audio_output)
            print("audio")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def audio_to_video(self, audio_source, video_output):
        try:
            api_key = "sk-mtesxgXBWPSqgieATsQjHGqcHjsoYevS8WYp5K9DwEUSo7aV"

            files = [
                ("input_face", open(self.avatar_source, "rb")),
                ("input_audio", open(audio_source, "rb")),
            ]
            payload = {
                "selected_model": "Wav2Lip",
            }

            response = requests.post(
                "https://api.gooey.ai/v2/Lipsync/form/",
                headers={
                    "Authorization": "Bearer " + api_key,
                },
                files=files,
                data={"json": json.dumps(payload)},
            )
            assert response.ok, response.content

            result = response.json()
            output_video_link = result["output"]["output_video"]
            urllib.request.urlretrieve(output_video_link, video_output)

            print("video ")

            return True

        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def text_to_video(self, text, audio_output="audio.mp3", video_output="video.mp4"):
        if not text:
            return False
        if not self.text_to_audio(text, audio_output):
            return False
        if not self.audio_to_video(audio_output, video_output):
            return False
        return True
