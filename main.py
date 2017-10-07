import speech_recognition
from multiprocessing import Pool
from transcribe import transcribe_audio

from ml import modelStatistics
from search import bing_api


def process(recognizer, audio):
    global model, word_list

    # Get text chunk from audio
    transcribed_text_chunk = transcribe_audio.run(recognizer, audio)
    if len(transcribed_text_chunk) > 0:

        if modelStatistics.predict(model, word_list, transcribed_text_chunk):
            phrase_hits = bing_api.search(transcribed_text_chunk)
            print phrase_hits


# MAIN

# Init Multithreading stuff
pool = Pool(processes=1)

# Init Speech Recog
recognizer = speech_recognition.Recognizer()

# Build ML Model
model, word_list = modelStatistics.createModel()

# Driver to receive input
with speech_recognition.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)

    while True:
        print("Speak:")

        # timeout if the time it waits before audio starts
        # phrase_time_limit is to cut it off at those many seconds
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        # Asynchronously process batches of transcribed data
        result = pool.apply_async(process, [recognizer, audio])
