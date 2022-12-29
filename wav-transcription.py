import os
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
speech_client = speech.SpeechClient()

# File Size: < 10mbs, length < 1 minute

#Load the media files
media_file_name_wav = 'elevator-pitch.wav'
with open(media_file_name_wav, 'rb') as f2:
   byte_data_wav = f2.read()
audio_wav = speech.RecognitionAudio(content=byte_data_wav)

#Configure Media Files Output
config_wav = speech.RecognitionConfig(
   sample_rate_hertz=48000,
   enable_automatic_punctuation=True,
   language_code='en-US',
   audio_channel_count=2
)

#Transcribing the RecognitionAudio objects
response_standard_wav = speech_client.recognize(
   config=config_wav,
   audio=audio_wav
)
print(response_standard_wav.results[0].alternatives[0].transcript)