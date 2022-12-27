import os
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
speech_client = speech.SpeechClient()

# File Size: < 10mbs, length < 1 minute

#Load the media files
media_file_name_mp3 = 'elevator-pitch.mp3'
with open(media_file_name_mp3, 'rb') as f1:
    byte_data_mp3 = f1.read()
audio_mp3 = speech.RecognitionAudio(content=byte_data_mp3)

#Configure Media Files Output
config_mp3 = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation=True,
    language_code='en-US'
)

## Step 3. Transcribing the RecognitionAudio objects
response_standard_mp3 = speech_client.recognize(
    config=config_mp3,
    audio=audio_mp3
)
print(response_standard_mp3)
