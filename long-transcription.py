import os
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'
speech_client = speech.SpeechClient()

#Transcribing a long media file
media_uri = 'gs://speech-to-text-audio-filess/the-dilemma.wav'
long_audi_wav = speech.RecognitionAudio(uri=media_uri)

config_wav = speech.RecognitionConfig(
   sample_rate_hertz=48000,
   enable_automatic_punctuation=True,
   language_code='en-US',
   audio_channel_count=2
)

config_wav_enhanced = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    enable_automatic_punctuation=True,
    language_code='en-US',
    use_enhanced=True,
    model='video'
)

operation = speech_client.long_running_recognize(
    config=config_wav,
    audio=long_audi_wav
)
response = operation.result(timeout=90)
print(response)

for result in response.results:
    print(result.alternatives[0].transcript)
    #print(result.alternatives[0].confidence)
    #print()